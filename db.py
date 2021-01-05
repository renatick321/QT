import sqlite3
import datetime


conn = sqlite3.connect("db.db")
cursor = conn.cursor()

def convert_dt(text):
	return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def user_create(login, password, name, age, location, description, img_path):
	cursor.execute("""
					  INSERT INTO Users(login, password, name, age, location, description, img_path) 
					  SELECT '{}', '{}', '{}', {}, '{}', '{}', '{}' WHERE NOT EXISTS(SELECT 1 FROM Users WHERE login = '{}')
				   """.format(login, password, name, age, location, description, img_path, login))
	conn.commit()


def can_create(login):
	for i in cursor.execute("SELECT name FROM Users WHERE login = '{}'"):
		return False
	return True


def mark(login, partner_login, status):
	cursor.execute("INSERT INTO History(login, partner_login, status) VALUES ('{}', '{}', {})".format(login, partner_login, status))
	if status == 1:
		message_create("{} оценил {}".format(login, partner_login), login, partner_login)
	conn.commit()

def get_partner(login):
	lst = []
	for i in cursor.execute("SELECT login FROM Users WHERE login != '{}'".format(login)):
		lst.append(i[0])
	users = []
	st = set()
	for i in cursor.execute("SELECT partner_login FROM History WHERE login = '{}'".format(login, login)):
		st.add(i[0])
	users = list(filter(lambda x: x not in st, lst))
	if len(users) > 0:
		return get_user(users[0])
	return None

def get_user(login): # По логину
	for i in cursor.execute("SELECT login, password, name, age, location, description, img_path, id FROM Users WHERE login = '{}'".format(login)):
		d = {"login": i[0], "password": i[1], "name": i[2], "age": i[3], "location": i[4], "description": i[5], "img_path": i[6], "id": i[7]}
		return d
	return None


def login_(login, password):
	user = get_user(login)
	if user is None:
		return None
	if user['password'] == password:
		return user
	return None


def user_update(login, password, age, location, description, img_path):
	cursor.execute("UPDATE Users SET password = '{}' WHERE login = '{}'".format(password, login))
	cursor.execute("UPDATE Users SET location = '{}' WHERE login = '{}'".format(location, login))
	cursor.execute("UPDATE Users SET description = '{}' WHERE login = '{}'".format(description, login))
	cursor.execute("UPDATE Users SET img_path = '{}' WHERE login = '{}'".format(img_path, login))
	conn.commit()


def message_create(text, from_user_login, to_user_login):
	dt = datetime.datetime.now()
	cursor.execute("INSERT INTO Message(text, dt, from_user_login, to_user_login) VALUES ('{}', '{}', '{}', '{}')".format(text, dt, from_user_login, to_user_login))
	conn.commit()


def delete_id(login, s):
	lst = list(map(str, s.split(":")))
	if lst[0] == login:
		return lst[1]
	else:
		return lst[0]


def get_interlocutors(login):
	d = {}
	id = get_user(login)['id']
	for i in cursor.execute("SELECT from_user_login, to_user_login, dt FROM Message WHERE from_user_login = '{}' or to_user_login = '{}'".format(login, login)):
		if i[0] == login:
			s = str(i[0]) + ":" + str(i[1])
		else:
			s = str(i[1]) + ":" + str(i[0])
		datetime = convert_dt(i[2])
		try:
			if d[s] < datetime:
				d[s] = datetime
		except KeyError:
			d[s] = datetime
	lst = list(d.items())
	lst.sort(key=lambda x: x[1])
	lst = list(map(lambda x: delete_id(login, x[0]), lst))
	return lst


def get_some_messages(login, partner_login):
	lst = []
	for i in cursor.execute("SELECT text, from_user_login, to_user_login FROM Message WHERE (from_user_login = '{}' AND to_user_login = '{}') OR (from_user_login = '{}' AND to_user_login = '{}')".format(login, partner_login, partner_login, login)):
		from_ = i[1]
		to_ = i[2]
		text = i[0]
		if from_ == login:
			lst.append("{}: {}".format(login, text))
		else:
			lst.append("{}: {}".format(partner_login, text))
	return lst