from flask import request

import sys
import datetime

from db_module import db
from .         import company_api
from routes    import company_query


@company_api.route("api/list", methods=["GET"])
def select_compamy_list():
    try: 
        db.connect()

        offset = request.args.get("offset", default=1, type=int)
        limit  = (
            request.args.get("limit", type=int) 
            if request.args.get("limit") 
            else sys.maxsize
        ) # default=5,
        skip   = int(limit * (offset - 1))
        print(offset, limit, skip)

        compaies = company_query.select_company_list(limit, skip)

        if compaies is None:
            return { "message": "아직 입력된 기업이 존재하지 않습니다.", "status": 200 }

        return { "results": compaies, "status": 200 }

    finally:
        db.close()

@company_api.route("api/get/<company_id>", methods=["GET"])
def select_compamy_detail(company_id: int):
    try:
        db.connect()

        if company_id:
            company = company_query.select_company_to_check_exist(company_id)

            if company is None:
                return { "message": "존재하지 않는 기업입니다.", "status": 200 }

            return { "result": company, "status": 200 }

        return { "message": "기업 id가 입력되지 않았습니다.", "status": 200 }

    finally:
        db.close()

@company_api.route("api/add", methods=["POST"])
def create_company():
    try:
        db.connect()
        
        company_name = request.form["company_name"]
        description  = request.form["description"]

        company_query.create_company(company_name, description)

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()

@company_api.route("api/update/<company_id>", methods=["PUT"]) # path param 방식
def update_company(company_id: int):
    try:
        db.connect()

        company_name = request.form["company_name"]
        description  = request.form["description"]
        now_date     = datetime.datetime.now()

        find_company = company_query.select_company_to_check_exist(company_id)

        if find_company is None:
            return { "message:": "존재하지 않는 기업입니다.", "status": 200 }

        company_query.update_company(company_name, description, now_date, company_id)

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()

@company_api.route("api/remove/<company_id>", methods=["DELETE"])
def delete_company(company_id: int):
    try:
        db.connect()

        company = company_query.select_company_to_check_exist(company_id)

        if company is None:
            return { "message:": "존재하지 않는 기업입니다.", "status": 200 }

        company_query.delete_company(company_id)

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()