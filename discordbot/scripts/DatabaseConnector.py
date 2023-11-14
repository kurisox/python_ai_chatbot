import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def connector():
    print(os.getenv("DBUSER"))
    return mysql.connector.connect(host=os.getenv("HOST"),
                                   user=os.getenv("DBUSER"),
                                   password=os.getenv("PASSWORD"),
                                   database=os.getenv("DATABASE"),
                                   port=os.getenv("PORT"))