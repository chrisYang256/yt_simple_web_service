from flask import request

import os
import pymysql
import datetime

from . import company_api
from db_module import db


cursor = db.cursor(pymysql.cursors.DictCursor)

@company_api.route("api/server_time", methods=["GET"]) 
def get_servertime():
    return '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@company_api.route("api/list", methods=["GET"])
def select_compamy_list():
    try: 
        db.connect()

        offset = request.args.get('offset', default=1, type=int)
        limit  = request.args.get('limit', default=5, type=int)
        skip   = int(limit * (offset - 1))

        compaies = """
            select * 
            from company 
            order by cdate DESC 
            limit %s offset %s
        """

        cursor.execute(compaies, (limit, skip))

        results = cursor.fetchall() # all/one 구분하기

        if results is None:
            return { "message": "아직 입력된 기업이 존재하지 않습니다.", "status": 200 }

        return { "results": results, "status": 200 }

    finally:
        db.close()

@company_api.route("api/get/<company_id>", methods=["GET"]) # query param 방식
def select_compamy(company_id):
    try:
        db.connect()

        company_id = request.args.get("company_id", default="", type=int)

        if company_id:
            company = """
                select * 
                from company 
                where id=%s
            """
            cursor.execute(company, (company_id))

            result = cursor.fetchone()

            if result is None:
                return { "message": "존재하지 않는 기업입니다.", "status": 200 }

            return { "result": result, "status": 200 }

        return { "message": "기업 이름이 입력되지 않았습니다.", "status": 200 }

    finally:
        db.close()

@company_api.route("api/add", methods=["POST"])
def create_company():
    try:
        db.connect()

        req = request.get_json()
        company_name = req["company_name"]
        description  = req["description"]

        company_info = """
            insert into company(company_name, description) 
            values(%s, %s)
        """
        cursor.execute(company_info, (company_name, description))

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()

@company_api.route("api/update/<company_id>", methods=["PUT"]) # path param 방식
def update_company(company_id: int):
    try:
        db.connect()
        req = request.get_json()

        company_name = req["company_name"]
        description  = req["description"]
        now_date     = datetime.datetime.now()

        find_company = """
            select * 
            from company
            where id=%s
        """
        cursor.execute(find_company, (company_id))
        find_company = cursor.fetchone()

        if find_company is None:
            return { "message:": "존재하지 않는 기업입니다.", "status": 200 }

        company_info = """
            update company 
            set company_name=%s, description=%s, udate=%s
            where id=%s
        """

        cursor.execute(company_info, 
            (company_name, description, now_date, company_id)
        )
        cursor.fetchall()

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()

@company_api.route("api/remove/<company_id>", methods=["DELETE"])
def delete_company(company_id: int):
    try:
        db.connect()

        find_company = """
            select * 
            from company
            where id=%s
        """
        cursor.execute(find_company, (company_id))
        find_company = cursor.fetchone()

        if find_company is None:
            return { "message:": "존재하지 않는 기업입니다.", "status": 200 }

        company_info = """
            delete from company 
            where id=%s
        """

        cursor.execute(company_info, (company_id))
        cursor.fetchall()

        db.commit()
        return { "message": "success", "Status": 201 }
    
    finally:
        db.close()