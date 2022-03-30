from flask  import Flask
from routes import *

import os


app = Flask(__name__)
app.register_blueprint(company)

if __name__=="__main__":
    app.run(
        host  = os.getenv("WEB_HOST"), 
        port  = os.getenv("WEB_PORT"), 
        debug = os.getenv("DEBUG")
    )