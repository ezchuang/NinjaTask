from flask import Flask, session, request
from flask import render_template, redirect, jsonify
import json
import mysql.connector

app = Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = "I wanna be"

db_config = {
    "host" : "localhost",
    "username" : "root",
    "password" : "12345678",
    "database" : "website"
}
db_pool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "my_pool", pool_size = 10, **db_config)

# SQL 指令運行
def use_cursor(db_pool, command, values, update):
    db_connection = db_pool.get_connection()
    db_cursor = db_connection.cursor(dictionary = True)
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
    db_account_arr = use_cursor(db_pool, selector, [user_username], False)
    if len(db_account_arr) > 0:
        return redirect("/error?message=" + "帳號已被註冊")
    # 寫入 DB
    writer = "INSERT INTO member(name, username, password, follower_count) VALUES(%s, %s, %s, '0')"
    use_cursor(db_pool, writer, [user_name, user_username, user_password], True)
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
    # 建立搜尋結果
    selector = "SELECT id, name, username, password FROM member WHERE username = %s"
    db_account_arr = use_cursor(db_pool, selector, [user_username], False)
    if len(db_account_arr) < 1 or db_account_arr[0]["password"] != user_password:
        return redirect("/error?message=" + "帳號或密碼輸入錯誤")
    # 建立 session
    session["sign-in"] = True
    session["id"] = db_account_arr[0]["id"]
    session["user_name"] = db_account_arr[0]["name"]
    session["user_username"] = db_account_arr[0]["username"]
    return redirect("/member")

# 會員頁面
@app.route("/member", methods = ["GET"])
def member():
    if session.get("sign-in", None) != True:
        return redirect("/")
    # selector = "SELECT count(%s) as MAX FROM message"
    # counter = use_cursor(db_pool, selector, ["*"], False)
    selector = "SELECT id FROM message ORDER BY id DESC"
    msg_id_arr = use_cursor(db_pool, selector, [], False)
    return render_template("member.html", name = session["user_name"], mem_id = session["id"], \
                           msg_min = msg_id_arr[-1]["id"], msg_max = int(msg_id_arr[0]["id"]) + 1) 

# 搜尋使用者
@app.route("/api/member", methods = ["GET"])
def search_name():
    username = request.args.get("username")
    res = {
        "data" : None,
        }
    try:
        # 此處不額外驗證是誰操作
        # 能驗證的變數僅有 前端回傳 id，不可靠
        # 所以此處選擇相信 session 不額外驗證使用者
        if not session.get("sign-in", None):
            raise Exception
        selector = "SELECT id, name, username FROM member WHERE username = %s"
        name_arr = use_cursor(db_pool, selector, [username], False)
        res = {
            "data" : name_arr[0],
            }
        return res
    except:
        return res

# 修改姓名
@app.route("/api/member", methods=["PATCH"])
def modify_name():
    new_name = request.json.get("name")
    res = {
        "error": True,
        }
    try:
        if not session.get("sign-in", None):
            raise Exception
        if not new_name:
            raise Exception
        # 說明同 搜尋使用者 search_name()
        # 相信 session，此處不做 ID 驗證
        writer = "UPDATE member SET name = %s WHERE username = %s"
        use_cursor(db_pool, writer, [new_name, session["user_username"]], True)
        session["user_name"] = new_name
        res = {
            "ok": True,
            }
        return res
    except:
        return res

# 建立留言
@app.route("/createMessage", methods = ["POST"])
def createMessage():
    if session.get("sign-in", None) != True:
        return redirect("/")
    msg = request.form["msg"]
    writer = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
    use_cursor(db_pool, writer, [session["id"], msg], True)
    return redirect("/member")

# 取得留言
@app.route("/getMsg/<int:msg_pointer>", methods=["GET"])
def getMsg(msg_pointer):
    if session.get("sign-in", None) != True:
        return redirect("/")
    # 撈取留言 (100筆)
    # 按讚之後再做
    selector = "SELECT message.id, message.member_id, member.name, message.content, message.like_count, message.time \
    FROM message LEFT JOIN member ON member.id = message.member_id WHERE message.id < %s ORDER BY message.time DESC LIMIT %s"
    db_account_arr = use_cursor(db_pool, selector, [msg_pointer, 10], False)
    res = {
        "data" : db_account_arr
    }
    return res

# 刪除留言
@app.route("/deleteMessage", methods=["POST"])
def deleteMessage():
    # 防爆
    if session.get("sign-in", None) != True:
        return redirect("/")
    selector = "SELECTOR member_id FROM mseeage WHERE id = %s"
    msg_id = request.form["msg_id"]
    mem_id = use_cursor(db_pool, selector, [msg_id], False)
    if mem_id != session["id"]:
        return redirect("/member")
    msg_id = request.form["msg_id"]
    deleter = "DELETE FROM message WHERE id = %s"
    use_cursor(db_pool, deleter, [msg_id], True)
    return redirect("/member")

# 登出
@app.route("/signout", methods=["GET"])
def signout():
    # 沒登入，這邊應該是用不到
    if session.get("sign-in", None) != True:
        return redirect("/")
    # 去除登入紀錄
    session.clear()
    return redirect("/")

# 錯誤頁
@app.route("/error", methods = ["GET"])
def error():
    msg = request.args.get("message", "")
    return render_template("error.html", message = msg)

if __name__ == "__main__":
    app.run(port = 3000, debug = True, threaded = True)
    # app.run(port = 3000, debug = True)