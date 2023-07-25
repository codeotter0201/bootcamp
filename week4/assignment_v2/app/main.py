from flask import Flask, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__, 
            static_folder="static", 
            static_url_path="/static",
            template_folder="templates"
            )
app.secret_key = "your_secret_key"  # 用於加密 session 的密鑰

# 假設以下的使用者資料是存在資料庫中的
users = {"test": "test"}

def reset_session(session):
    session["username"] = None
    session["error_msg"] = None
    session["square_result"] = None
    return session

@app.route('/')
def login():
    if session.get('username', None): 
        return redirect('/member')
    return render_template('index.html') 

@app.route("/signin", methods=["POST"])
def verify_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 驗證使用者名稱和密碼
        if (not username) and (not password):
            msg = "請輸入使用者名稱與密碼"
            session['error_msg'] = msg
            return jsonify({"message": msg})
        
        if username not in users: 
            msg = "使用者不存在或密碼錯誤"
            session['error_msg'] = msg
            return jsonify({"message": msg})
        
        if password != users.get(username, None):
            msg = "使用者不存在或密碼錯誤"
            session['error_msg'] = msg
            return jsonify({"message": msg})
        
        if users.get(username, None) == password and username in users:
            session["username"] = username 
            msg = "ok"
            return jsonify({"message": msg})
        
# 會員頁面
@app.route("/member")
def member_page():
    name = session.get("username", None)
    if name:
        # return redirect('/member.html')
        ret = session.get("square_result", None)
        return render_template(
            "member.html",
            page_name=f"歡迎光臨 {name}，這是會員頁",
            username=name,
            square_result=ret
        )
    else:
        session["username"] = None
        session["error_msg"] = None
        return redirect("/error?message=Bad boy")

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
    # 刪除 session
    reset_session(session)
    return redirect("/")  

@app.route("/square/<number>") 
def cal_square(number): 
    n = int(number)
    session["square_result"] = n * n 
    return redirect("/")

@app.route("/clear") 
def clear_square_result():
    session["square_result"] = None
    return {'result':'ok'} 

if __name__ == "__main__": 
    app.run() 