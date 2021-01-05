import sqlite3

conn = sqlite3.connect("db.db")
cursor = conn.cursor()
try:
	cursor.execute("""CREATE TABLE Users
			        (
			    	 id INTEGER PRIMARY KEY AUTOINCREMENT,
			    	 login varchar(31) NOT NULL,
			    	 password varchar(31) NOT NULL,
			    	 name varchar(31) NOT NULL,
			    	 age int NOT NULL,
			    	 location varchar(31) NOT NULL,
			    	 description varchar(1000) NOT NULL,
			    	 img_path varchar(100)
			        )
			        """)
except:
	print("Таблица Users уже существует")

try:
	cursor.execute("""CREATE TABLE History
			        (
			    	 id INTEGER PRIMARY KEY AUTOINCREMENT,
			    	 login varchar(100) NOT NULL,
			    	 partner_login varchar(100) NOT NULL,
			    	 status int
			        )
			        """)
except:
	print("Таблица History уже существует")

try:
	cursor.execute("""CREATE TABLE Message
			        (
			    	 id INTEGER PRIMARY KEY AUTOINCREMENT,
			    	 text text,
			    	 dt date,
			    	 from_user_login varchar(100),
			    	 to_user_login varchar(100)
			        )
			        """)
except:
	print("Таблица History уже существует")


conn.commit()



