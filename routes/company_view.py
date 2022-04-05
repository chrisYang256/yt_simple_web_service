from flask import render_template
from .     import company_view

import datetime


@company_view.route("list_view")
def get_company_list():
    server_time = '{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 로딩 시 서버시간 출력(갱신 필요없음 - 교육 내용)
    return render_template("select_company_list.html", server_time=server_time)

@company_view.route("detail_view/<company_id>")
def get_company_detail(company_id):
    return render_template("select_company_detail.html", company_id=company_id)

@company_view.route("add_view")
def add_company():
    return render_template("add_company.html")

@company_view.route("update_view/<company_id>")
def update_company(company_id):
    return render_template("update_company.html", company_id=company_id)