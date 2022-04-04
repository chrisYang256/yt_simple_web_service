from flask import render_template
from .     import user_view


@user_view.route("list_view")
def get_user_list():
    return render_template("select_user_list.html")

@user_view.route("detail_view/<company_id>")
def get_company_detail(company_id):
    return render_template("select_company_detail.html", company_id=company_id)

@user_view.route("add_view")
def add_company():
    return render_template("add_company.html")

@user_view.route("update_view/<company_id>")
def update_company(company_id):
    return render_template("update_company.html", company_id=company_id)