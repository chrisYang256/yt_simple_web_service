from flask import render_template
from .     import company_view

import datetime
import threading

# def server_time():
#     threading.Timer(1, server_time).start()
#     return print('{}'.format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

@company_view.route("list_view")
def get_company_list():
    # timer = server_time()
    return render_template("index.html")

@company_view.route("detail_view/<company_id>")
def get_company_detail(company_id):
    return render_template("company_detail.html", company_id=company_id)

@company_view.route("add_view")
def add_company():
    return render_template("add_company.html")

@company_view.route("update_view/<company_id>")
def update_company(company_id):
    return render_template("update_company.html", company_id=company_id)