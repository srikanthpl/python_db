import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Sri@1234",
  database="finance"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
