from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session



# 建立 Application 物件
app = Flask(__name__,
          static_folder="static") 

# 建立 Session 金鑰
app.secret_key = "wehelp_roro"

# 建立網站首頁的回應方式
@app.route("/")
def index():
    return render_template("index.html")

# 驗證頁面 /signin (POST)
@app.route("/signin", methods=["POST"])
def signin():
    # 取得資料放入變數
    userid = request.form["userid"]
    password = request.form["password"]
    # 驗證欄位是否為test
    if userid == "test" and password == "test":
        session["SIGN_IN"] = True
        return redirect(url_for('member'))
    # 驗證欄位是否有輸入
    elif userid == "" or password == "":
        return redirect(url_for('error', message='請輸入帳號及密碼'))
    else:
        return redirect(url_for('error', message='帳號、或密碼輸入錯誤'))

# 成功頁面 /member
@app.route("/member")
def member():
    if session["SIGN_IN"] == True:
        return render_template("success.html")
    else:
        return redirect('index')

# 錯誤頁面 /error (GET)
@app.route("/error")
def error():
    message = request.args.get('message', '')
    return render_template('error.html', message=message)
    
# 狀態管理 /signout
@app.route("/signout")
def signout():
    session["SIGN_IN"] = False
    return redirect(url_for('index'))

# 啟動網站伺服器
app.run(port=3000)
