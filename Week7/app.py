from flask import *
import mysql.connector

# 建立資料庫連線
con = mysql.connector.connect(
    user="root",
    password="mynewpassword",
    host="localhost",
    database="website"
)

# 建立 Application 物件
app = Flask(__name__,
          static_folder="static") 

# 建立 Session 金鑰
app.secret_key = "wehelp_roro"

# 建立網站首頁的回應方式
@app.route("/")
def index():
    return render_template("index.html")

# 註冊頁面 /signup (POST)
@app.route("/signup", methods=["POST"])
def signup():
    # 從前端取得資料放入變數
    name = request.form["name"]
    account = request.form["account"]
    password = request.form["password"]

    # 建立 Cursor 物件執行 SQL 指令
    cursor = con.cursor()
    # 確認帳號是否存在於 member 中
    cursor.execute("SELECT COUNT(*) FROM member WHERE username = %s", (account,))
    account_count = cursor.fetchone()[0]
    
    # 若帳號已經存在, 返回錯誤訊息
    if account_count > 0:
        return redirect("/error?message=帳號已經被註冊")
    # 若帳號不存在, 新增資料
    else:
        cursor.execute("INSERT INTO member(name, username, password)VALUES (%s, %s, %s)", (name, account, password))
        con.commit()

    cursor.close()
    return redirect("/")

# 會員頁面 /member
@app.route("/member")
def member():
    if "name" in session:
        name = session.get("name")

        cursor = con.cursor()
        cursor.execute("SELECT member.id, member.name, message.content FROM member JOIN message ON member.id = message.member_id ORDER BY message.time;")
        messageContent = cursor.fetchall()
        messages = [{"memberName": row[1], "content": row[2]}for row in messageContent]
        cursor.close()
        return render_template("success.html", name=name, messages=messages)
    else:
        return redirect("/")

# 錯誤頁面 /error (GET)
@app.route("/error")
def error():
    message = request.args.get("message", "")
    return render_template("error.html", message=message)

# 登入狀況 /signin (POST)
@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    
    cursor=con.cursor()
    cursor.execute("SELECT * FROM member WHERE username = %s AND password = %s" , (account,password))
    user_data = cursor.fetchone()
    
    if user_data == None:
        return redirect("/error?message=帳號或密碼輸入錯誤")
    else:
        session["name"] = user_data[1]
        session["id"] = user_data[0]
        return redirect("/member")
    
    cursor.close()

# 登出狀況 /signout
@app.route("/signout")
def signout():
    if "name" in session or "id" in session:
        del session["name"]
        del session["id"]
        return redirect("/")
    return redirect("/")

# 留言功能 (POST)
@app.route("/createMessage", methods=["POST"])
def createMessage():
    content = request.form["usercontent"]
    userId = session["id"]

    cursor = con.cursor()
    cursor.execute("INSERT INTO message(member_id, content) VALUES (%s, %s)", (userId, content))
    con.commit()
    return redirect("/member")

# 查詢會員資料功能 /api/member (GET)
@app.route("/api/member", methods=["GET"])
def check_data():
    username = request.args.get("username")

    cursor = con.cursor()
    cursor.execute("SELECT id, name, username FROM member WHERE username=%s", (username,))
    data = cursor.fetchall()
    cursor.close()
  
    # 若查詢成功 , 回傳 JSON(id,name,username)
    if "name" in session or "id" in session:
        response = {"data": data[0]}
    else:
        response = {"data": None}
    return jsonify(response)
    

# 修改會員姓名功能 /api/member (PATCH)
@app.route("/api/member", methods=["PATCH"])
def update_name():
    data = request.get_json()
    newName = data.get("name")
    if "name" in session and "id" in session:
        cursor = con.cursor()    
        cursor.execute("UPDATE member SET name=%s WHERE id=%s", (newName, session["id"]))
        con.commit()
        cursor.close()
        session["name"] = newName
       
        return jsonify({"ok":True})
    else:
        return jsonify({"error":True})

    

    

# 啟動網站伺服器
app.run(port=3000)