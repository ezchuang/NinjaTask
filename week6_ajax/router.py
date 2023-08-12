from flask import Flask, session, request
from flask import render_template, redirect, jsonify
import mysql.connector

app = Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = "I wanna be"

db_config = {
    "host" : "localhost",
    "username" : "root",
    "password" : "12345678",
    "database" : "website"
}
db_website_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "my_pool", pool_size = 10, **db_config)

# SQL 指令運行
def use_cursor(db_pool, command, values, update):
    db_connection = db_pool.get_connection()
    db_cursor = db_connection.cursor()
    db_cursor.execute(command, values)
    try:
        if not update:
            return db_cursor.fetchall()
        db_connection.commit()
    finally:
        db_cursor.close()
        db_connection.close()

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
    db_account_arr = use_cursor(db_website_pool, selector, [user_username], False)
    if len(db_account_arr) > 0:
        return redirect("/error?message=" + "帳號已被註冊")
    # 寫入 DB
    writer = "INSERT INTO member(name, username, password, follower_count) VALUES(%s, %s, %s, '0')"
    use_cursor(db_website_pool, writer, [user_name, user_username, user_password], True)
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
    db_account_arr = use_cursor(db_website_pool, selector, [user_username], False)
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
    use_cursor(db_website_pool, writer, [session["id"], msg], True)
    return redirect("/member")

# 取得留言
@app.route("/getMsg", methods=["GET"])
def getMsg():
    if session.get("sign-in", None) != True:
        return redirect("/")
    # 撈取留言 (100筆)
    # 按讚之後再做
    selector = "SELECT message.id, member.id, member.name, message.content \
    FROM member LEFT JOIN message ON member.id = message.member_id ORDER BY message.time DESC LIMIT %s"
    db_account_arr = use_cursor(db_website_pool, selector, [100], False)
    return jsonify( db_account_arr )

# 刪除留言
@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    # 防爆
    selector = "SELECTOR member_id FROM mseeage WHERE id = %s"
    msg_id = request.form["msg_id"]
    mem_id = use_cursor(db_website_pool, selector, [msg_id], False)
    if mem_id != session["id"]:
        return redirect("/member")
    msg_id = request.form["msg_id"]
    deleter = "DELETE FROM message WHERE id = %s"
    use_cursor(db_website_pool, deleter, [msg_id], True)
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
    app.run(port = 3000, debug = True, threaded = True)
    # app.run(port = 3000, debug = True)