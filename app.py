from flask  import Flask, render_template
from routes import *
from dotenv import load_dotenv
from flask_cors import CORS

import os


app = Flask(__name__)
CORS(app)
app.register_blueprint(company_api)
app.register_blueprint(company_view)

load_dotenv(
    dotenv_path=".env",
    verbose=True
)

@app.route("/company/list_view")
def view_company_list():
    return render_template("index.html")

@app.route("/company/add_view")
def add_company():
    return render_template("/add_company.html")

if __name__=="__main__":
    app.run(
        host  = os.getenv("WEB_HOST"), 
        port  = os.getenv("WEB_PORT"), 
        debug = os.getenv("DEBUG")
    )