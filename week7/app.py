from flask import Flask, session, request
from flask import render_template, redirect
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
def use_cursor(db_pool, command, values, update, fetch_mode = ""):
    db_connection = db_pool.get_connection()
    db_cursor = db_connection.cursor(dictionary = True)
    try:
        db_cursor.execute(command, values)
        if update:
            db_connection.commit()
            return
        if fetch_mode == "one":
            return db_cursor.fetchone()
        return db_cursor.fetchall()
    except Exception as err:
        print(err)
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
    user_name = request.form["account_name"]
    user_username = request.form["account_username"]
    user_password = request.form["account_password"]

    query_find = "SELECT username, password FROM member WHERE username = %s"
    db_account_data = use_cursor(db_pool, query_find, [user_username], False, "one")
    if db_account_data:
        return redirect("/error?message=" + "帳號已被註冊")
    query_update = "INSERT INTO member(name, username, password, follower_count) VALUES(%s, %s, %s, '0')"
    use_cursor(db_pool, query_update, [user_name, user_username, user_password], True)
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

    query_find = "SELECT id, name, username, password FROM member WHERE username = %s"
    db_account_data = use_cursor(db_pool, query_find, [user_username], False, "one")
    if not db_account_data or db_account_data["password"] != user_password:
        return redirect("/error?message=" + "帳號或密碼輸入錯誤")
    
    session["signin"] = True
    session["id"] = db_account_data["id"]
    session["user_name"] = db_account_data["name"]
    session["user_username"] = db_account_data["username"]
    return redirect("/member")

# 取得 member page 要用的全域變數
@app.route("/api/getInfo", methods = ["POST"])
def get_info():
    mem_id = request.json.get("mem_id")
    try:
        if not session.get("signin") or mem_id != str(session["id"]):
            raise Exception
        
        query_find = "SELECT id as mem_id, name as name_show FROM member WHERE id = %s"
        info_data = use_cursor(db_pool, query_find, [mem_id], False, "one")
        query_find = "SELECT id as msg_min FROM message ORDER BY id ASC LIMIT 1"
        msg_min = use_cursor(db_pool, query_find, [], False, "one")
        query_find = "SELECT id as msg_pointer FROM message ORDER BY id DESC LIMIT 1"
        msg_pointer = use_cursor(db_pool, query_find, [], False, "one")
        msg_pointer["msg_pointer"] = int(msg_pointer["msg_pointer"]) + 1

        info_data.update(msg_min)
        info_data.update(msg_pointer)
        res = {
            "data" : info_data,
        }
    except:
        res = {
            "data" : None,
        }
    finally:
        return res

# 會員頁面
@app.route("/member", methods = ["GET"])
def member():
    if not session.get("signin"):
        return redirect("/")
    return render_template("member.html", mem_id = session["id"]) 

# 搜尋使用者
@app.route("/api/member", methods = ["GET"])
def search_name():
    username = request.args.get("username")
    try:
        # 此處不額外驗證是誰操作
        # 能驗證的變數僅有 前端回傳 id，不可靠
        # 所以此處選擇相信 session 不額外驗證使用者
        if not session.get("signin"):
            raise Exception
        query_find = "SELECT id, name, username FROM member WHERE username = %s"
        name_data = use_cursor(db_pool, query_find, [username], False, "one")
        res = {
            "data" : name_data,
            }
    except:
        res = {
            "data" : None,
            }
    finally:
        return res

# 修改姓名
@app.route("/api/member", methods=["PATCH"])
def modify_name():
    new_name = request.json.get("name")
    try:
        if not session.get("signin"):
            raise Exception
        if not new_name:
            raise Exception
        # 說明同 搜尋使用者 search_name()
        # 相信 session，此處不做 ID 驗證
        query_update = "UPDATE member SET name = %s WHERE username = %s"
        use_cursor(db_pool, query_update, [new_name, session["user_username"]], True)
        session["user_name"] = new_name
        res = {
            "ok": True,
            }
    except:
        res = {
            "error": True,
            }
    finally:
        return res

# 建立留言
@app.route("/createMessage", methods = ["POST"])
def create_message():
    if not session.get("signin"):
        return redirect("/")
    msg = request.form["msg"]
    query_update = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
    use_cursor(db_pool, query_update, [session["id"], msg], True)
    return redirect("/member")

# 取得留言
@app.route("/getMsg/<int:msg_pointer>", methods=["GET"])
def get_msg(msg_pointer):
    if not session.get("signin"):
        return redirect("/")
    # 按讚之後再做
    query_find = "SELECT message.id, message.member_id, member.name, message.content, message.like_count, message.time \
                FROM message LEFT JOIN member ON member.id = message.member_id WHERE message.id < %s ORDER BY \
                message.time DESC LIMIT %s"
    db_account_arr = use_cursor(db_pool, query_find, [msg_pointer, 10], False)
    res = {
        "data" : db_account_arr
    }
    return res

# 刪除留言
@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    if not session.get("signin"):
        return redirect("/")
    
    query_find = "SELECT member_id FROM message WHERE id = %s"
    msg_id = request.form["msg_id"]
    mem_id_dict = use_cursor(db_pool, query_find, [msg_id], False, "one")
    if mem_id_dict["member_id"] != session["id"]:
        return redirect("/member")
    
    query_update = "DELETE FROM message WHERE id = %s"
    use_cursor(db_pool, query_update, [msg_id], True)
    return redirect("/member")

# 登出
@app.route("/signout", methods=["GET"])
def signout():
    session.clear()
    return redirect("/")

# 錯誤頁
@app.route("/error", methods = ["GET"])
def error():
    msg = request.args.get("message", "")
    return render_template("error.html", message = msg)

if __name__ == "__main__":
    app.run(port = 3000, debug = True, threaded = True)