import mysql.connector as mysql
import pandas as pd

db = mysql.connect(
    host="localhost",  # Corrected host name
    user="root",
    password="Your localhost password",
    port=3306,
    database="company"
    )
if db.is_connected():
    print("Connected to MySQL Server")
else:
    print("Connection failed")

pd.read_sql("SELECT * FROM employee", con=db)    