import mysql.connector

dataBase = mysql.connector.connect(
        host = 'localhost',
        user = 'moe',
        passwd = 'password'
        )
# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("create database CRM_Database")

print("All done!")
