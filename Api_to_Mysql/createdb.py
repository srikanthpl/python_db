import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sri@1234"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE jeevafinance")
