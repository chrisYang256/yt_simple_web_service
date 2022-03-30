import os
import pymysql

from dotenv import load_dotenv


load_dotenv(
    dotenv_path=".env",
    verbose=True
)

db = pymysql.connect(
	user    = os.getenv("DB_USER"),
    passwd  = os.getenv("DB_PASSWORD"),
    host    = os.getenv("DB_HOST"),
    db      = os.getenv("DB_NAME"),
    port    = int(os.getenv("DB_PORT")),
    charset = "utf8"
)