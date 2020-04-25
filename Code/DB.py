import mysql.connector as mysql
import datetime
from User import User
from EventSignup import EventSignup
from Event import Event

class DB:
	def __init__(self):
		self.host = "127.0.0.1"
		self.user = "root"
		self.password = "githubowyjuliusz"
		self.schema = "pswdb"
		self.users_table = "user"
		self.events_table = "event"
		self.signups_table = "event_signup"
		self.connection = mysql.connect(user = self.user, password = self.password, host = self.host)
		self.cursor = self.connection.cursor()

	def __del__(self):
		try:
			self.connection.close()
		except:
			print("Couldn't close connection.")
	
	def run_query(self, query):
		try:
			self.cursor.execute(query)
		except Exception as e:
			print(e)
		try:
			table = self.cursor.fetchall()
		except:
			table = self.cursor.fetchone()
		self.connection.commit()
		return table

	def get_users_table(self):
		query = f"SELECT * FROM {self.schema}.{self.users_table}"
		table = self.run_query(query)
		return table
	
	def get_events_table(self):
		query = f"SELECT * FROM {self.schema}.{self.events_table}"
		table = self.run_query(query)
		return table

	def get_pending_signups(self):
		query = f"SELECT * FROM {self.schema}.{self.signups_table} WHERE accepted=FALSE"
		table = self.run_query(query)
		return table

	def get_event_names(self):
		query = f"SELECT name FROM {self.schema}.{self.events_table}"
		table = self.run_query(query)
		return table
	
	def get_event_details(self, event_name):
		query = f"SELECT * FROM {self.schema}.{self.events_table} WHERE name=\'{event_name}\'"
		table = self.run_query(query)
		return table
	
	def insert_user(self, user):
		query = f"INSERT INTO {self.schema}.{self.users_table} VALUES (0, \'{user.name}\', \'{user.last_name}\', \'{user.login}\', \'{user.password}\', \'{user.email}\', \'{user.permission}\', \'{user.registration_date}\')"
		self.run_query(query)
	
	def insert_event(self, event):
		query = f"INSERT INTO {self.schema}.{self.events_table} VALUES (0, \'{event.name}\', \'{event.agenda}\', \'{event.date}\')"
		self.run_query(query)
	
	def insert_event_signup(self, event_signup):
		query = f"INSERT INTO {self.schema}.{self.signups_table} VALUES ({event_signup.id}, {event_signup.id_user}, {event_signup.id_event}, \'{event_signup.participation_type}\', \'{event_signup.catering}\', {event_signup.accepted})"
		self.run_query(query)
	
	def delete_user(self, id):
		query = f"DELETE FROM {self.schema}.{self.users_table} WHERE id={id}"
		self.run_query(query)

	def delete_event(self, id):
		query = f"DELETE FROM {self.schema}.{self.events_table} WHERE id={id}"
		self.run_query(query)
	
	def delete_signup(self, id):
		query = f"DELETE FROM {self.schema}.{self.signups_table} WHERE id={id}"
		self.run_query(query)
	
	def accept_signup(self, id):
		query = f"UPDATE {self.schema}.{self.signups_table} SET accepted=TRUE WHERE id={id}"
		self.run_query(query)
	
	def change_users_password(self, id, password):
		query = f"UPDATE {self.schema}.{self.users_table} SET password=\'{password}\' WHERE id={id}"
		self.run_query(query)
	
	def update_event(self, event):
		query = f"UPDATE {self.schema}.{self.events_table} SET name=\'{event.name}\', agenda=\'{event.agenda}\', date=\'{event.date}\' WHERE id={event.id}"
		self.run_query(query)
	
	def check_if_already_signed_up(self, event_signup):
		query = f"SELECT * FROM {self.schema}.{self.signups_table} WHERE id_user={event_signup.id_user} AND id_event={event_signup.id_event}"
		table = self.run_query(query)
		if table == []:
			return False
		return True
	
	def check_login_and_password(self, login, password):
		query = f"SELECT * FROM {self.schema}.{self.users_table} WHERE login=\'{login}\' and password=\'{password}\'"
		user_data = self.run_query(query)
		return user_data
	
	def is_login_taken(self, user):
		query = f"SELECT id FROM {self.schema}.{self.users_table} WHERE login=\'{user.login}\'"
		table = self.run_query(query)
		if table == []:
			return False
		return True