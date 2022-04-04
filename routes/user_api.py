from flask import request

from db_module import db
from .         import user_api
from routes    import user_query


@user_api.route("api/list", methods=["GET"])
def select_user_list():
    try: 
        db.connect()

        offset = request.args.get('offset', default=1, type=int)
        limit  = request.args.get('limit', default=5, type=int)
        skip   = int(limit * (offset - 1))

        users = user_query.select_user_list(limit, skip)

        if users is None:
            return { "message": "아직 입력된 사용자가 존재하지 않습니다.", "status": 200 }

        return { "results": users, "status": 200 }

    finally:
        db.close()

@user_api.route("api/get/<user_id>", methods=["GET"])
def select_user_detail(user_id: int):
    try:
        db.connect()

        if user_id:
            user = user_query.select_user_to_check_exist(user_id)

            if user is None:
                return { "message": "존재하지 않는 사용자입니다.", "status": 200 }



            return { "result": user, "status": 200 }

        return { "message": "사용자 id가 입력되지 않았습니다.", "status": 200 }

    finally:
        db.close()

@user_api.route("api/add", methods=["POST"])
def create_user():
    try:
        db.connect()
        
        company_id = request.form["company_id"]
        user_name = request.form["user_name"]
        login_id  = request.form["login_id"]

        user_query.create_user(company_id, user_name, login_id)

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()

# @user_api.route("api/update/<company_id>", methods=["PUT"]) # path param 방식
# def update_company(company_id: int):
#     try:
#         db.connect()

#         company_name = request.form["company_name"]
#         description  = request.form["description"]
#         now_date     = datetime.datetime.now()

#         find_company = company_query.select_company_to_check_exist(company_id)

#         if find_company is None:
#             return { "message:": "존재하지 않는 기업입니다.", "status": 200 }

#         company_query.update_company(company_name, description, now_date, company_id)

#         db.commit()
#         return { "message": "success", "Status": 201 }
    
#     finally:
#         db.close()

@user_api.route("api/remove/<user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    try:
        db.connect()

        user = user_query.select_user_to_check_exist(user_id)

        if user is None:
            return { "message:": "존재하지 않는 사용자입니다.", "status": 200 }

        user_query.delete_user(user_id)

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()