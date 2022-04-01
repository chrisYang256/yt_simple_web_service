
from flask import render_template
from .     import company_view


@company_view.route("list_view")
def view_company_list():
    return render_template("index.html", time="00:00")

@company_view.route("add_view")
def add_company():
    return render_template("/add_company.html")