from flask import Flask, render_template, request, redirect, session, url_for, jsonify

app = Flask(__name__, 
            static_folder="static", 
            static_url_path="/static",
            template_folder="templates"
            )
   
app.secret_key = "your_secret_key"  # 用於加密 session 的密鑰

# 使用者資料
users = {"test": "test"}

def reset_session(session):
    session["username"] = None
    session["signed_in"] = False
    return session

@app.route('/')
def signin():
    if session.get('username', None):
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
        
        if username not in users: 
            msg = "使用者不存在或密碼錯誤"
            return jsonify({"message": msg})
        
        if password != users.get(username, None):
            msg = "使用者不存在或密碼錯誤"
            return jsonify({"message": msg})
        
        if users.get(username, None) == password and username in users:
            session["username"] = username
            session["signed_in"] = True
            msg = "ok"
            return jsonify({"message": msg})
    return redirect("/")

# 會員頁面
@app.route("/member")
def member_page():
    name = session.get("username", None)
    signed_in = session.get("signed_in", None)
    if signed_in:
        return render_template(
            "member.html",
            page_name=f"歡迎光臨 {name}，這是會員頁",
            username=name,
        )
    else:
        session["username"] = None
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

@app.route("/square/<number>")
def cal_square(number):
    n = int(number)
    n *= n
    return render_template(  
        "square.html",
        square_result=n
    ) 

if __name__ == "__main__": 
    app.run() 