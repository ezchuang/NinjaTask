from flask import ( Blueprint, request, session, current_app,
                   make_response, jsonify)

import app_modules

blueprint = Blueprint('blueprint123', __name__, url_prefix = "/api", static_folder = "public", static_url_path = "/")

# 搜尋使用者
# 此處不額外驗證是誰操作
# 能驗證的變數僅有 前端回傳 id，不可靠
# 所以此處選擇相信 session 不額外驗證使用者
@blueprint.route("/member", methods=["GET"])
def search_name():
    username = request.args.get("username")
    try:
        if not session.get("signin"):
            raise Exception
        # query_find = "SELECT id, name, username FROM member WHERE username = %s"
        command_paras = {
            "columns" : "id, name, username",
            "table" : "member",
            "where" : "username = %s",
            "target" : (username,)
        }
        name_data = app_modules.query_fetch_one(command_paras)
        return jsonify({"data" : name_data,})
    except Exception as err:
        print(err)
        return jsonify({"data" : None,})
    
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
        # query_update = "UPDATE member SET name = %s WHERE username = %s"
        command_paras = {
            "table" : "member",
            "set" : "name = %s",
            "where" : "username = %s",
            "target" : (new_name, session["user_username"],)
        }
        app_modules.query_update(command_paras)
        session["user_name"] = new_name
        return jsonify({"ok": True,})
    except Exception as err:
        print(err)
        return jsonify({"error": True,})
    
# 取得 member page 要用的全域變數
@blueprint.route("/getInfo", methods=["POST"])
def get_info():
    mem_id = request.json.get("mem_id")
    try:
        if not session.get("signin") or mem_id != str(session["id"]):
            raise Exception
        # 分別撈出資料
        # query_find = "SELECT id as mem_id, name as name_show FROM member WHERE id = %s"
        command_paras = {
            "columns" : "id as mem_id, name as name_show",
            "table" : "member",
            "where" : "id = %s",
            "target" : (mem_id,)
        }
        info_data = app_modules.query_fetch_one(command_paras)
        # query_find = "SELECT id as msg_min FROM message ORDER BY id ASC LIMIT 1"
        command_paras = {
            "columns" : "id as msg_min",
            "table" : "message",
            "order" : "id",
            "order_ordered" : "ASC",
            "limit" : "1",
        }
        msg_min = app_modules.query_fetch_one(command_paras)
        # query_find = "SELECT id as msg_pointer FROM message ORDER BY id DESC LIMIT 1"
        command_paras = {
            "columns" : "id as msg_pointer",
            "table" : "message",
            "order" : "id",
            "order_ordered" : "DESC",
            "limit" : "1",
        }
        msg_pointer = app_modules.query_fetch_one(command_paras)
        msg_pointer["msg_pointer"] = int(msg_pointer["msg_pointer"]) + 1
        # 合併資料
        info_data.update(msg_min)
        info_data.update(msg_pointer)
        return jsonify({"data" : info_data,})
    except Exception as err:
        print(err)
        return jsonify({"data" : None,})