from flask import Flask, session, request, render_template, redirect, jsonify
import app_modules

app = app_modules.create_app()

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

    command_paras = {
        "columns" : "username, password",
        "table" : "member",
        "where" : "username = %s",
        "target" : (user_username,)
    }
    db_account_data = app_modules.query_fetch_one(command_paras)
    if db_account_data:
        return redirect("/error?message=" + "帳號已被註冊")
    # query_update = "INSERT INTO member(name, username, password, follower_count) VALUES(%s, %s, %s, '0')"
    command_paras = {
        "table" : "member",
        "columns" : "name, username, password, follower_count",
        "values" : "%s, %s, %s, '0'",
        "target" : (user_name, user_username, user_password,)
    }
    app_modules.query_create(command_paras)
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

    # query_find = "SELECT id, name, username, password FROM member WHERE username = %s"
    command_paras = {
        "columns" : "id, name, username, password",
        "table" : "member",
        "where" : "username = %s",
        "target" : (user_username,)
    }
    db_account_data = app_modules.query_fetch_one(command_paras)
    if not db_account_data or db_account_data["password"] != user_password:
        return redirect("/error?message=" + "帳號或密碼輸入錯誤")
    
    session["signin"] = True
    session["id"] = db_account_data["id"]
    session["user_name"] = db_account_data["name"]
    session["user_username"] = db_account_data["username"]
    return redirect("/member")

# 會員頁面
@app.route("/member", methods=["GET"])
def member():
    if not session.get("signin"):
        return redirect("/")
    return render_template("member.html", mem_id = session["id"]) 

# 建立留言
@app.route("/createMessage", methods=["POST"])
def create_message():
    if not session.get("signin"):
        return redirect("/")
    msg = request.form["msg"]
    # query_update = "INSERT INTO message(member_id, content) VALUES(%s, %s)"
    command_paras = {
        "table" : "message",
        "columns" : "member_id, content",
        "values" : "%s, %s",
        "target" : (session["id"], msg,)
    }
    app_modules.query_create(command_paras)
    return redirect("/member")

# 取得留言
@app.route("/getMsg/<int:msg_pointer>", methods=["GET"])
def get_msg(msg_pointer):
    if not session.get("signin"):
        return redirect("/")
    # 按讚之後再做
    # query_find = "SELECT message.id, message.member_id, member.name, message.content, message.like_count, message.time \
    #             FROM message LEFT JOIN member ON member.id = message.member_id WHERE message.id < %s ORDER BY \
    #             message.time DESC LIMIT %s"
    command_paras = {
        "columns" : "message.id, message.member_id, member.name, message.content, message.like_count, message.time",
        "table" : "message LEFT JOIN member ON member.id = message.member_id",
        "where" : "message.id < %s",
        "order" : "message.time",
        "order_ordered" : "DESC",
        "limit" : "%s",
        "target" : (msg_pointer, 10,)
    }
    db_account_arr = app_modules.query_fetch_all(command_paras)
    return {"data" : db_account_arr}

# 刪除留言
@app.route("/deleteMessage", methods=["POST"])
def delete_message():
    if not session.get("signin"):
        return redirect("/")
    
    msg_id = request.form["msg_id"]
    # query_find = "SELECT member_id FROM message WHERE id = %s"
    command_paras = {
        "columns" : "member_id",
        "table" : "message",
        "where" : "id = %s",
        "target" : (msg_id,)
    }
    mem_id_dict = app_modules.query_fetch_one(command_paras)
    if mem_id_dict["member_id"] != session["id"]:
        return redirect("/member")
    
    # query_update = "DELETE FROM message WHERE id = %s"
    command_paras = {
        "table" : "message",
        "where" : "id = %s",
        "target" : (msg_id,)
    }
    app_modules.query_del(command_paras)
    return redirect("/member")

# 登出
@app.route("/signout", methods=["GET"])
def signout():
    session.clear()
    return redirect("/")

# 錯誤頁
@app.route("/error", methods=["GET"])
def error():
    msg = request.args.get("message", "")
    return render_template("error.html", message = msg)

if __name__ == "__main__":
    app.config['connection_pool'] = app_modules.create_connection_pool()
    app.run(port = 3000)