from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect

app = Flask(__name__, static_folder = "public", static_url_path = "/")
app.secret_key = "you can't see me"

# index page
@app.route("/", methods=["GET"])
def index():
    session["SIGNED-IN"] = False
    return render_template("index.html")

# 登入判斷
@app.route("/signin", methods=["POST"])
def signin():
    user_account = request.form["account"]
    user_password = request.form["password"]
    if user_account == "test" and user_password == "test":
        session["SIGNED-IN"] = True
        return redirect("/member")
    else:
        error_msg = "帳號、或密碼輸入錯誤"
        return redirect("/error?message=" + error_msg)

# 登出
@app.route("/signout", methods=["GET"])
def signout():
    # 換到首頁做，確保每次登入都是初始狀態
    # session["SIGNED-IN"] = False
    return redirect("/")


# 登入成功
@app.route("/member", methods=["GET"])
def member():
    if session["SIGNED-IN"] == False:
        return redirect("/")
    else:
        return render_template("member.html")

# 登入失敗
@app.route("/error", methods=["GET"])
def error():
    msg = request.args.get("message", "帳號、或密碼輸入錯誤")
    return render_template("error.html", message = msg)

# 計算器
@app.route("/square")
def square():
    target = int(request.args.get("calculate", "0"))
    return render_template("/square.html", result = target * target)


if __name__ == "__main__":
    app.run(port=3000)