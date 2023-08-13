from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, 
            static_folder="static", 
            static_url_path="/static",
            template_folder="templates"
            )
   
app.secret_key = "your_secret_key"  # 用於加密 session 的密鑰
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test:test@db/testdb'
db = SQLAlchemy(app)

class Member(db.Model):
    __tablename__ = 'member'
    
    username = db.Column(db.String(255), primary_key=True, index=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    follower_count = db.Column(db.Integer, nullable=False, default=0)
    time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())

    def to_json(self):
        member_dict = {
            'username': self.username,
            'name': self.name,
            'password': self.password,
            'follower_count': self.follower_count,
            'time': self.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return member_dict

class Message(db.Model):
    __tablename__ = 'message'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    member_id = db.Column(db.String(255), db.ForeignKey('member.username'), nullable=False)
    content = db.Column(db.String(255), nullable=False)
    like_count = db.Column(db.Integer, nullable=False, default=0)
    time = db.Column(db.DateTime, nullable=False, server_default=db.func.current_timestamp())
    
    member = db.relationship("Member")

    def to_json(self):
        message_dict = {
            'id': self.id,
            'member_id': self.member_id,
            'content': self.content,
            'like_count': str(self.like_count),
            'time': self.time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return message_dict

def reset_session(session):
    session["userid"] = None
    session["username"] = None
    session["signed_in"] = False
    return session

@app.route('/')
def homepage():
    if session.get('userid', None):
        return redirect('/member')
    return render_template('index.html')

@app.route("/signin", methods=["GET", "POST"]) 
def verify_user():
    if request.method == "POST":
        payload = request.get_json()
        username = payload.get("username")
        password = payload.get("password")

        # 驗證使用者名稱和密碼 
        if (not username) and (not password):
            msg = "請輸入使用者名稱與密碼"
            return jsonify({"message": msg})
        
        user:Member = Member.query.filter_by(username=username).first()
        if not user or user.password != password:
            msg = "使用者不存在或密碼錯誤"
            return jsonify({"message": msg})
        
        session["username"] = user.username
        session["name"] = user.name
        session["signed_in"] = True
        return jsonify({"message": "ok"})
    return redirect("/")

# 會員頁面
@app.route("/member")
def member_page():
    name = session.get("name", None)
    signed_in = session.get("signed_in", None)
    if signed_in:
        return render_template(
            "member.html",
            page_name=f"歡迎光臨 {name}，這是會員頁",
            username=name,
        )
    else:
        reset_session(session)
        return redirect("/")

# 登入失敗
@app.route("/error")
def error_page(): 
    error_msg = request.args.get("message", None)
    if error_msg:
        return render_template( 
            "error.html",
            error_msg=error_msg,
        )
    else:
        return redirect("/")

# 登出
@app.route("/signout") 
def signout():
    reset_session(session)
    return redirect("/")

# 註冊帳號
@app.route("/signup", methods=["POST"])
def signup():
    # 解析 request
    payload = request.get_json()
    username = payload.get("username")
    name = payload.get("name")
    password = payload.get("password")
    # 檢查資料庫中的 Member 是否在
    member = Member.query.filter_by(username=username).first()

    if member:
        # 有會員，導向到error，顯示帳號已經被註冊
        msg = f"{username} 已經被註冊"
        return jsonify({"message": msg})
    else:
        # 沒有會員，新增會員，導向至 member
        new_member = Member(username=username, name=name, password=password)
        # 將新的 Member 物件添加到資料庫中
        db.session.add(new_member)
        # 提交變更到資料庫
        db.session.commit()
        msg = 'ok'
        return jsonify({"message": msg})

# 新增留言
@app.route("/createMessage", methods=["POST"])
def createMessage():
    # 解析 request
    payload = request.get_json()
    message = payload.get("message")
    # 使用會員的session新增留言
    username = session.get('username', None)
    isSigned = session.get('signed_in', None)
    # 沒有會員，新增會員，導向至 member
    if isSigned:
        member = Member.query.filter_by(username=username).first()
        new_content = Message(member=member, content=message)
        # 將新的 Message 物件添加到資料庫中
        db.session.add(new_content)
        # 提交變更到資料庫
        db.session.commit()
        return {'message':'ok'}

# 刪除留言
@app.route("/deleteMessage", methods=["GET", "POST"])
def deleteMessage():
    if request.method == 'GET':
        return 'bad boy'
    # 解析 request
    payload = request.get_json()
    message_id = payload.get("message_id")
    message = Message.query.get(message_id)
    if session.get('signed_in', None):
        if message:
            db.session.delete(message)  # 刪除留言
            db.session.commit()  # 儲存修改到資料庫
            return {'message':'ok'}
        else:
            return {'message':'刪除留言失敗'}
    else:
        return 'bad boy'

# 讀取留言
@app.route("/readMessage")
def readMessage():
    isSigned = session.get('signed_in', None)
    # 沒有會員，新增會員，導向至 member
    if isSigned:
        messages = Message.query.all()[::-1]
        message_data = []
        for message in messages:
            name = message.member.name
            content = message.content
            message_id = message.id if message.member.username == session.get('username') else -1
            message_data.append({name: content, "message_id":message_id})
        return jsonify(message_data)
    else:
        return 'bad boy'

@app.route('/reset')
def db_reset():
    db.drop_all()
    db.create_all()
    return 'ok'

@app.route('/all')
def all():
    members:list[Message] = Member.query.all()
    msgs:list[Message] = Message.query.all()
    return jsonify({'member':[i.to_json() for i in members], 'msgs':[i.to_json() for i in msgs]})

if __name__ == "__main__": 
    db.create_all()
    app.run() 