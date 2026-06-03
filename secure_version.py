import sqlite3
conn = sqlite3.connect('users.db')
username = input("Enter username: ")
password = input("Enter password: ")
query = "SELECT * FROM users WHERE username=? AND password=?"
conn.execute(query, (username, password))
print("secure query executed")