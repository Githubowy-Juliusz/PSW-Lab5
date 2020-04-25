import re, datetime
from DB import DB
from User import User
from EmailSender import EmailSender

class Registration:
	def __init__(self, db):
		self.db = db
		#using localhost as SMTP server
		self.email_sender = EmailSender("registration@pswdb", "localhost")
	
	def _validate_input(self, login, password, password_validation, name, last_name, email):
		error_message = []
		if len(name) < 2 or len(last_name) < 2:
			error_message.append("name and last name have to be at least 2 characters long")
		if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
			error_message.append("incorrect e-mail address")
		if len(login) < 3:
			error_message.append("login has to be at least 3 characters long")
		if len(password) < 8:
			error_message.append("password has to be at least 8 characters long")
		if password != password_validation:
			error_message.append("passwords do not match")

		if len(error_message) != 0:
			error_message = ", ".join(error_message)
			error_message = f"Error: {error_message}."
			raise Exception(error_message)
	
	def register(self, login, password, password_validation, name, last_name, email):
		self._validate_input(login, password, password_validation, name, last_name, email)

		new_user = User(0, name, last_name, login, password, email, "user", str(datetime.date.today()))
		if self.db.is_login_taken(new_user):
			raise Exception("Error: login already in use.")
		
		self.db.insert_user(new_user)
		try:
			self.email_sender.send_email(email, f"{name} {last_name}")
		except:
			return ("Warning!", "Account created, but confirmation mail couldn't be sent.")
		return ("Success!", "You created an account.")