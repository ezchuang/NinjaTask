from flask import Blueprint, g, redirect, request, render_template, make_response, url_for, session

blueprint = Blueprint('blueprint123', __name__, url_prefix = "/api", static_folder = "public", static_url_path = "/")

# @blueprint.route("/")
# def index():
#     return "Hello World, This is an example of blueprint"

# 搜尋使用者
# 此處不額外驗證是誰操作
# 能驗證的變數僅有 前端回傳 id，不可靠
# 所以此處選擇相信 session 不額外驗證使用者
@blueprint.route("/member", methods = ["GET"])
def search_name():
    username = request.args.get("username")
    try:
        if not session.get("signin"):
            raise Exception
        query_find = "SELECT id, name, username FROM member WHERE username = %s"
        name_data = use_cursor(g.db_pool, query_find, [username], False, True)
        print("try")

        return {"data" : name_data,}
    except:
        print("except")
        print(g.db_pool)
        print(use_cursor)

        return {"data" : None,}
    
# 修改姓名
# 此處不額外驗證是誰操作
# 能驗證的變數僅有 前端回傳 id，不可靠
# 所以此處選擇相信 session 不額外驗證使用者
@blueprint.route("/member", methods=["PATCH"])
def modify_name():
    new_name = request.json.get("name")
    try:
        if not session.get("signin") or not new_name:
            raise Exception
        query_update = "UPDATE member SET name = %s WHERE username = %s"
        use_cursor(g.db_pool, query_update, [new_name, session["user_username"]], True)
        session["user_name"] = new_name
        return {"ok": True,}
    except:
        return {"error": True,}