# create db with sqlite
# import sqlite3
# conn = sqlite3.connect("users.db")
# c = conn.cursor()
# c.execute("SELECT id FROM users WHERE users.email = ?")
# rows = c.fetchall()
# print(rows)
# # SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, user date_added AS users_date_added FROM users WHERE users.email = ?


# create db with mysql
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password123")
my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE our_users")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
  print(db)
