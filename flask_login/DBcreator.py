import sqlite3  
  
con = sqlite3.connect("usersdb.db")  
print("Database opened successfully")  
  
con.execute("create table UsersDB (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  