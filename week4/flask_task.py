from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for

app = Flask(__name__, static_folder = "public", static_url_path = "/")
# session 密鑰
app.secret_key = "you can't see me"

# index page
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# 登入判斷，POST將使用者帳密隱藏
@app.route("/signin", methods=["POST"])
def signin():
    # session["user_account"] = request.form["account"]
    # session["user_password"] = request.form["password"]
    user_account = request.form["account"]
    user_password = request.form["password"]
    # 帳密驗證，至少其一為空
    if user_account == "" or user_password =="":
        error_msg = "Please enter username and password"
        return redirect("/error?message=" + error_msg)
    # 帳密驗證，錯誤
    if not (user_account == "test" and user_password == "test"):
        error_msg = "Username or password is not correct"
        # 建立 GET 方法的 url 列 (參數傳遞)
        return redirect("/error?message=" + error_msg)
    else:
        # 紀錄 驗證通過資訊
        session["SIGNED-IN"] = True
        return redirect("/member")

# 登出
@app.route("/signout", methods=["GET"])
def signout():
    # 去除 驗證通過資訊
    # session["SIGNED-IN"] = False
    del session["SIGNED-IN"]
    # del session["user_account"]
    # del session["user_password"]
    return redirect("/")


# 登入成功
@app.route("/member", methods=["GET"])
def member():
    # 驗證 是否有通過資訊
    if session["SIGNED-IN"] == False:
        return redirect("/")
    else:
        return render_template("member.html")

# 登入失敗
@app.route("/error", methods=["GET"])
def error():
    msg = request.args.get("message", "")
    # 承襲自 "/signin"，參數傳遞
    return render_template("error.html", message = msg)

# Soltion 2，用 form 傳遞資訊，並從後端轉跳網頁
# # 計算器轉跳
# @app.route("/square/", methods=["GET"])
# def square_jump():
#     target = int(request.args.get("calculate"))
#     # 轉跳到/square
#     return redirect(url_for("square_res", num = target))

# 計算器
@app.route("/square/<int:num>", methods=["GET"])
def square_res(num):
    # 參數傳遞
    return render_template("/square.html", num = num)



if __name__ == "__main__":
    app.run(port=3000, debug=True)