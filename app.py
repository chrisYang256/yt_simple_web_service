from flask  import Flask, render_template, request
from dotenv import load_dotenv

import os
import pymysql

app = Flask(__name__)
load_dotenv(".env.dev")

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
def compamy_list():
    # offset = request.args.get('start', default=0, type=int)
    # limit  = request.args.get('limit', default=20, type=int)
    sql_values = "select * from company"
    cursor.execute(sql_values)

    results = cursor.fetchall() # all/one 구분하기

    return { "results": results, "status": 200 }

@app.route("/company/api/get", methods=["GET"]) # query param 방식
def compamy_get():
    company_name = request.args.get("company_name", default="", type=str)

    if company_name:
        sql_value = "select * from company where company_name=%s"
        cursor.execute(sql_value, (company_name))

        result = cursor.fetchone()

        return { "result": result, "status": 200 }
    
    else:
        return { "message": "회사 이름이 입력되지 않았습니다.", "status": 200 }

@app.route("/company/api/add", methods=["POST"])
def compant_add():
    db.connect()
    req = request.get_json()
    company_name = req["company_name"]
    description  = req["description"]

    sql_value = "insert into company(company_name, description) values(%s, %s)"

    cursor.execute(sql_value, (company_name, description))
    db.commit()
    db.close()

    return { "message": "success", "Status": 201 }


@app.route("/company/api/update/<company_id>", methods=["PUT"]) # path param 방식
def company_update(company_id: int):
    db.connect()
    req = request.get_json()

    company_name = req["company_name"]
    description  = req["description"]

    sql_value = "update company set company_name=%s, description=%s where id=%s"

    cursor.execute(sql_value, (company_name, description, company_id))
    db.commit()
    db.close()

    return { "message": "success", "Status": 201 }

@app.route("/company/api/remove/<company_id>", methods=["DELETE"])
def company_remove(company_id: int):
    db.connect()

    sql_value = "delete from company where id=%s"

    cursor.execute(sql_value, (company_id))
    db.commit()
    db.close()

    return { "message": "success", "Status": 201 }
    
if __name__=="__main__":
    app.run(debug=True)