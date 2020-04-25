class User:
	def __init__(self, id, name, last_name, login, password, email, permission, registration_date):
		self.id = id
		self.name = name
		self.last_name = last_name
		self.login = login
		self.password = password
		self.email = email
		self.permission = permission
		self.registration_date = registration_date
	
	def is_admin(self):
		if self.permission == "admin":
			return True
		return False

	def get_possible_permissions(self):
		return ["admin", "user"]