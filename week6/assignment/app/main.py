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

users = {'test':'test'}

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    userid = db.Column(db.String(80), index=True)
    password = db.Column(db.String(80))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(300), db.ForeignKey('member.userid'))
    content = db.Column(db.String(300))
    member = db.relationship('Member', backref=db.backref('messages', lazy=True))

def reset_session(session):
    session["userid"] = None
    session["username"] = None
    session["id"] = None
    session["signed_in"] = False
    return session

@app.route('/')
def signin():
    db.create_all()
    if session.get('userid', None):
        return redirect('/member')
    return render_template('index.html')

@app.route("/signin", methods=["GET", "POST"]) 
def verify_user():
    if request.method == "POST":
        payload = request.get_json()
        userid = payload.get("userid")
        password = payload.get("password")

        # 驗證使用者名稱和密碼 
        if (not userid) and (not password):
            msg = "請輸入使用者名稱與密碼"
            return jsonify({"message": msg})
        
        if not Member.query.filter_by(userid=userid).first():
            msg = "使用者不存在或密碼錯誤"
            return jsonify({"message": msg})
        
        if not Member.query.filter_by(password=password).first():
            msg = "使用者不存在或密碼錯誤"
            return jsonify({"message": msg})
        
        if Member.query.filter_by(userid=userid).first() and Member.query.filter_by(password=password).first():
            user:Member = Member.query.filter_by(userid=userid).first()
            session["userid"] = user.userid
            session["username"] = user.username
            session["id"] = user.id
            session["signed_in"] = True
            return jsonify({"message": "ok"})
    return redirect("/")

# 會員頁面
@app.route("/member")
def member_page():
    username = session.get("username", None)
    signed_in = session.get("signed_in", None)
    if signed_in:
        return render_template(
            "member.html",
            page_name=f"歡迎光臨 {username}，這是會員頁",
            username=username,
        )
    else:
        reset_session()
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
    userid = payload.get("userid")
    password = payload.get("password")
    # 檢查資料庫中的 Member 是否在
    member = Member.query.filter_by(userid=userid).first()

    if member:
        # 有會員，導向到error，顯示帳號已經被註冊
        msg = f"{userid} 已經被註冊"
        return jsonify({"message": msg})
    else:
        # 沒有會員，新增會員，導向至 member
        new_member = Member(username=username, userid=userid, password=password)
        # 將新的 Member 物件添加到資料庫中
        db.session.add(new_member)
        # 提交變更到資料庫
        db.session.commit()
        msg = 'ok'
        return jsonify({"message": msg})


@app.route('/all')
def all():
    mems:list[Member] = Member.query.all()
    return {i.userid:i.id for i in mems}

# 新增留言
@app.route("/createMessage", methods=["POST"])
def createMessage():
    # 解析 request
    payload = request.get_json()
    message = payload.get("message")
    # 使用會員的session新增留言
    userid = session.get('userid', None)
    isSigned = session.get('signed_in', None)
    # 沒有會員，新增會員，導向至 member
    if isSigned:
        member = Member.query.filter_by(userid=userid).first()
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
            username = message.member.username
            content = message.content
            message_id = message.id if message.member.userid == session.get('userid') else -1
            message_data.append({username: content, "message_id":message_id})
        
        return jsonify(message_data)
    else:
        return 'bad boy'

# @app.route('/reset')
# def db_reset():
#     db.drop_all()
#     db.create_all()
#     return 'ok'

if __name__ == "__main__": 
    app.run() 