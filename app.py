from flask  import Flask
from routes import *
from dotenv import load_dotenv

import os

app = Flask(__name__)
app.register_blueprint(company)

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