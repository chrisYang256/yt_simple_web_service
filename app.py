from flask  import Flask
from routes import *
from dotenv import load_dotenv
from flask_cors import CORS

import os


app = Flask(__name__)
CORS(app)
app.register_blueprint(common_api)
app.register_blueprint(company_api)
app.register_blueprint(company_view)
app.register_blueprint(user_api)
app.register_blueprint(user_view)

load_dotenv(
    dotenv_path=".env",
    verbose=True
)

if __name__=="__main__":
    app.run(
        host  = os.getenv("WEB_HOST"), 
        port  = os.getenv("WEB_PORT"), 
        debug = os.getenv("DEBUG")
    )