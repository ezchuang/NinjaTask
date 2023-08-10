from flask import Flask, session, request
from flask import render_template, redirect, jsonify
import mysql.connector

app = Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = "I wanna be"

# 首頁
@app.route("/", methods = ["GET"])
def index():
    return render_template("index.html")

# 註冊
@app.route("/signup", methods = ["POST"])
def signup():
    # 取得 input
    user_name = request.form["account_name"]
    user_username = request.form["account_username"]
    user_password = request.form["account_password"]
    # 建立搜尋結果
    selector = "SELECT username, password FROM member WHERE username = %s"
    db_cursor = db_website.cursor()
    db_cursor.execute(selector, [user_username])
    db_account_arr = db_cursor.fetchall()
    if len(db_account_arr) > 0:
        return redirect("/error?message=" + "帳號已被註冊")
    # 寫入 DB
    writer = "INSERT INTO member(name, username, password, follower_count) VALUES(%s, %s, %s, '0')"
    db_cursor = db_website.cursor()
    db_cursor.execute(writer, [user_name, user_username, user_password])
    db_website.commit()
    # 註冊結束直接登入
    # 建立 session
    # session["user_name"] = user_name
    # session["user_username"] = user_username
    # return redirect("/member")
    return redirect("/")

# 登入
@app.route("/signin", methods = ["POST"])
def signin():
    user_username = request.form["account_username"]
    user_password = request.form["account_password"]
    print("user_username : ", user_username)
    print("user_password : ", user_password)
    # 建立搜尋結果
    selector = "SELECT id, name, username, password FROM member WHERE username = %s"
    db_cursor = db_website.cursor()
    db_cursor.execute(selector, [user_username])
    db_account_arr = db_cursor.fetchall()
    print("db_account_arr : ", db_account_arr)
    if len(db_account_arr) < 1 or db_account_arr[0][3] != user_password:
        return redirect("/error?message=" + "帳號或密碼輸入錯誤")
    # 建立 session
    session["sign-in"] = True
    session["id"] = db_account_arr[0][0]
    session["user_name"] = db_account_arr[0][1]
    session["user_username"] = db_account_arr[0][2]
    return redirect("/member")

# 會員頁面
@app.route("/member", methods = ["GET"])
def member():
    if session.get("sign-in", None) != True:
        return redirect("/")
    return render_template("member.html", name = session["user_name"], mem_id = session["id"]) 

# 建立留言
@app.route("/createMessage", methods = ["POST"])
def createMessage():
    msg = request.form["msg"]
    writer = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
    db_cursor = db_website.cursor()
    db_cursor.execute(writer, [session["id"], msg])
    db_website.commit()
    return redirect("/member")

# 取得留言
@app.route("/getMsg", methods=["GET"])
def getMsg():
    # 撈取留言 (100筆)
    # 按讚之後再做
    selector = "SELECT message.id, member.id, member.name, message.content \
    FROM member RIGHT JOIN message ON member.id = message.member_id ORDER BY message.time DESC LIMIT %s"
    db_cursor = db_website.cursor()
    db_cursor.execute(selector, [100])
    return jsonify( db_cursor.fetchall() )

# 刪除留言
@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    # 防爆
    mem_id = int(request.form["id"])
    if mem_id != session["id"]:
        return redirect("/member")
    msg_id = request.form["msg_id"]
    deleter = "DELETE FROM message WHERE id = %s"
    db_cursor = db_website.cursor()
    db_cursor.execute(deleter, [msg_id])
    db_website.commit()
    return redirect("/member")

# 登出
@app.route("/signout", methods=["GET"])
def signout():
    print(session.get("sign-in", None))
    # 沒登入，這邊應該是用不到
    if session.get("sign-in", None) != True:
        return redirect("/")
    # 去除登入紀錄
    del session["sign-in"]
    del session["id"]
    del session["user_name"]
    del session["user_username"]
    return redirect("/")

# 錯誤頁
@app.route("/error", methods = ["GET"])
def error():
    msg = request.args.get("message", "")
    return render_template("error.html", message = msg)

if __name__ == "__main__":
    db_website = mysql.connector.connect(
        host = "localhost",
        username = "root",
        password = "12345678",
        database = "website"
    )
    app.run(port = 3000, debug = True)