from flask import render_template
from .     import user_view


@user_view.route("list_view")
def get_user_list():
    return render_template("select_user_list.html")

@user_view.route("detail_view/<user_id>")
def get_user_detail(user_id):
    return render_template("select_user_detail.html", user_id=user_id)

@user_view.route("add_view")
def add_user():
    return render_template("add_user.html")

@user_view.route("update_view/<user_id>")
def update_user(user_id):
    return render_template("update_user.html", user_id=user_id)