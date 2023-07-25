from flask import Flask, render_template, request, redirect, session, url_for

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
    
    # if session.get("error_msg", None): 
    #     em = session.pop("error_msg", None)  
    #     redirect_url = url_for('error_page', message=em)
    #     # print(redirect_url)
    #     return redirect(f"/error?message={em}")
    #     return redirect(redirect_url)
    
    return render_template('index.html') 

@app.route('/test')
def test_page():
    return redirect('https://www.google.com')

@app.route("/signin", methods=["POST"])
def verify_user():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 驗證使用者名稱和密碼
        if (not username) and (not password):
            session['error_msg'] = "請輸入使用者名稱與密碼"
            # return {"result":"請輸入使用者名稱與密碼"}
            em = session['error_msg']
            em = "請輸入使用者名稱與密碼"
            return redirect(f"/error?message={em}")
        
        if username not in users: 
            session['error_msg'] = "使用者不存在或密碼錯誤"
            # return {"result":"使用者不存在或密碼錯誤"}
            em = session['error_msg']
            em = "使用者不存在或密碼錯誤"
            return redirect(f"/error?message={em}")
        
        if password != users.get(username, None):
            session['error_msg'] = "使用者不存在或密碼錯誤"
            # return {"result":"使用者不存在或密碼錯誤"}
            em = session['error_msg']
            em = "使用者不存在或密碼錯誤"
            return redirect(f"/error?message={em}")
        
        if users.get(username, None) == password & username in users:
            session["username"] = username 
            # return {"result":"ok"}
            return redirect('/')

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
            page_name=f"無法訪問",
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