from flask  import Flask, render_template, request
from dotenv import load_dotenv

import os
import pymysql
import datetime

app = Flask(__name__)

load_dotenv(
    dotenv_path=".env",
    verbose=True
)

db = pymysql.connect(
	user    = os.getenv("DB_USER"),
    passwd  = os.getenv("DB_PASSWORD"),
    host    = os.getenv("DB_HOST"),
    db      = os.getenv("DB_NAME"),
    port    = int(os.getenv("DB_PORT")),
    charset = "utf8"
)
cursor = db.cursor(pymysql.cursors.DictCursor)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/company/api/list", methods=["GET"])
def select_compamy_list():
    db.connect()

    offset = request.args.get('offset', default=1, type=int)
    limit  = request.args.get('limit', default=20, type=int)
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
        db.close()
        return { "message": "아직 입력된 기업이 존재하지 않습니다.", "status": 200 }

    db.close()
    return { "results": results, "status": 200 }

@app.route("/company/api/get", methods=["GET"]) # query param 방식
def select_compamy():
    db.connect()

    company_name = request.args.get("company_name", default="", type=str)

    if company_name:
        company = """
            select * 
            from company 
            where company_name=%s
        """
        cursor.execute(company, (company_name))

        result = cursor.fetchone()

        if result is None:
            db.close()
            return { "message": "존재하지 않는 기업입니다.", "status": 200 }

        db.close()
        return { "result": result, "status": 200 }

    db.close()
    return { "message": "기업 이름이 입력되지 않았습니다.", "status": 200 }

@app.route("/company/api/add", methods=["POST"])
def create_company():
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
    db.close()
    return { "message": "success", "Status": 201 }


@app.route("/company/api/update/<company_id>", methods=["PUT"]) # path param 방식
def update_company(company_id: int):
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
        db.close()
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
    db.close()
    return { "message": "success", "Status": 201 }

@app.route("/company/api/remove/<company_id>", methods=["DELETE"])
def delete_company(company_id: int):
    db.connect()

    find_company = """
        select * 
        from company
        where id=%s
    """
    cursor.execute(find_company, (company_id))
    find_company = cursor.fetchone()

    if find_company is None:
        db.close()
        return { "message:": "존재하지 않는 기업입니다.", "status": 200 }

    company_info = """
        delete from company 
        where id=%s
    """

    cursor.execute(company_info, (company_id))
    cursor.fetchall()

    db.commit()
    db.close()
    return { "message": "success", "Status": 201 }

if __name__=="__main__":
    app.run(
        host  = os.getenv("WEB_HOST"), 
        port  = os.getenv("WEB_PORT"), 
        debug = os.getenv("DEBUG")
    )