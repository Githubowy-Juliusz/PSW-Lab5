from DB import DB
from User import User

class LogIn:
	def __init__(self, db):
		self.db = db
		self.failed_log_ins = 0
	
	def log_in(self, login, password):
		if self.failed_log_ins >= 3:
			raise Exception("You failed to log in 3 times in a row. You can't log in now.")
		
		user_data = self.db.check_login_and_password(login, password)
		if user_data == []:
			self.failed_log_ins += 1
			raise Exception("Wrong login and/or password")

		self.failed_log_ins = 0
		user = User(user_data[0][0], user_data[0][1], user_data[0][2], user_data[0][3], user_data[0][4], user_data[0][5], user_data[0][6], user_data[0][7])
		return user