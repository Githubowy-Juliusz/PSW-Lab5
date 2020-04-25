from PyQt5 import QtCore, QtGui, QtWidgets
from AddUserDialog import AddUserDialog
from ResetUsersPasswordDialog import ResetUsersPasswordDialog
from AddEventDialog import AddEventDialog
from User import User
from Event import Event
from EventSignup import EventSignup
import re, datetime

class AdminView(object):
	def setupUi(self, Admin_View):
		Admin_View.setObjectName("Admin_View")
		Admin_View.resize(683, 600)
		self.central_widget = QtWidgets.QWidget(Admin_View)
		self.central_widget.setObjectName("central_widget")
		self.signups_frame = QtWidgets.QFrame(self.central_widget)
		self.signups_frame.setGeometry(QtCore.QRect(0, 50, 671, 351))
		self.signups_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.signups_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.signups_frame.setObjectName("signups_frame")
		self.signups_accept_button = QtWidgets.QPushButton(self.signups_frame)
		self.signups_accept_button.setGeometry(QtCore.QRect(20, 240, 131, 36))
		self.signups_accept_button.setObjectName("signups_accept_button")
		self.signups_table = QtWidgets.QTreeWidget(self.signups_frame)
		self.signups_table.setGeometry(QtCore.QRect(0, 0, 661, 221))
		self.signups_table.setColumnCount(5)
		self.signups_table.setObjectName("signups_table")
		self.signups_decline_button = QtWidgets.QPushButton(self.signups_frame)
		self.signups_decline_button.setGeometry(QtCore.QRect(480, 240, 151, 36))
		self.signups_decline_button.setObjectName("signups_decline_button")
		self.user_frame = QtWidgets.QFrame(self.central_widget)
		self.user_frame.setGeometry(QtCore.QRect(0, 50, 671, 351))
		self.user_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.user_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.user_frame.setObjectName("user_frame")
		self.user_add_button = QtWidgets.QPushButton(self.user_frame)
		self.user_add_button.setGeometry(QtCore.QRect(20, 240, 131, 36))
		self.user_add_button.setObjectName("user_add_button")
		self.user_delete_button = QtWidgets.QPushButton(self.user_frame)
		self.user_delete_button.setGeometry(QtCore.QRect(250, 240, 131, 36))
		self.user_delete_button.setObjectName("user_delete_button")
		self.user_table = QtWidgets.QTreeWidget(self.user_frame)
		self.user_table.setGeometry(QtCore.QRect(0, 0, 661, 221))
		self.user_table.setColumnCount(8)
		self.user_table.setObjectName("user_table")
		self.user_reset_password_button = QtWidgets.QPushButton(self.user_frame)
		self.user_reset_password_button.setGeometry(QtCore.QRect(480, 240, 151, 36))
		self.user_reset_password_button.setObjectName("user_reset_password_button")
		self.events_view_button = QtWidgets.QPushButton(self.central_widget)
		self.events_view_button.setGeometry(QtCore.QRect(260, 0, 94, 36))
		self.events_view_button.setObjectName("events_view_button")
		self.users_view_button = QtWidgets.QPushButton(self.central_widget)
		self.users_view_button.setGeometry(QtCore.QRect(0, 0, 94, 36))
		self.users_view_button.setObjectName("users_view_button")
		self.log_out_button = QtWidgets.QPushButton(self.central_widget)
		self.log_out_button.setGeometry(QtCore.QRect(10, 380, 621, 36))
		self.log_out_button.setObjectName("log_out_button")
		self.sign_ups_view_button = QtWidgets.QPushButton(self.central_widget)
		self.sign_ups_view_button.setGeometry(QtCore.QRect(570, 0, 94, 36))
		self.sign_ups_view_button.setObjectName("sign_ups_view_button")
		self.events_frame = QtWidgets.QFrame(self.central_widget)
		self.events_frame.setGeometry(QtCore.QRect(0, 50, 671, 351))
		self.events_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
		self.events_frame.setFrameShadow(QtWidgets.QFrame.Raised)
		self.events_frame.setObjectName("events_frame")
		self.event_delete_button = QtWidgets.QPushButton(self.events_frame)
		self.event_delete_button.setGeometry(QtCore.QRect(250, 240, 131, 36))
		self.event_delete_button.setObjectName("event_delete_button")
		self.event_add_button = QtWidgets.QPushButton(self.events_frame)
		self.event_add_button.setGeometry(QtCore.QRect(20, 240, 131, 36))
		self.event_add_button.setObjectName("event_add_button")
		self.event_modify_button = QtWidgets.QPushButton(self.events_frame)
		self.event_modify_button.setGeometry(QtCore.QRect(480, 240, 151, 36))
		self.event_modify_button.setObjectName("event_modify_button")
		self.events_table = QtWidgets.QTreeWidget(self.events_frame)
		self.events_table.setGeometry(QtCore.QRect(0, 0, 661, 221))
		self.events_table.setColumnCount(4)
		self.events_table.setObjectName("events_table")
		Admin_View.setCentralWidget(self.central_widget)
		self.statusbar = QtWidgets.QStatusBar(Admin_View)
		self.statusbar.setObjectName("statusbar")
		Admin_View.setStatusBar(self.statusbar)
		self.retranslateUi(Admin_View)
		self.parent = Admin_View
		#
		self.db = self.parent.db

		self.log_out_button.clicked.connect(self.parent.show_login_view)
		self.users_view_button.clicked.connect(self.show_users_table)
		self.events_view_button.clicked.connect(self.show_events_table)
		self.sign_ups_view_button.clicked.connect(self.show_signups_table)
		self.user_add_button.clicked.connect(self.add_user)
		self.user_delete_button.clicked.connect(self.delete_user)
		self.user_reset_password_button.clicked.connect(self.reset_users_password)
		self.event_add_button.clicked.connect(self.add_event)
		self.event_delete_button.clicked.connect(self.delete_event)
		self.event_modify_button.clicked.connect(self.modify_event)
		self.signups_accept_button.clicked.connect(self.accept_signup)
		self.signups_decline_button.clicked.connect(self.decline_signup)


		
		self.show_users_table()

		#
		QtCore.QMetaObject.connectSlotsByName(self.parent)

	def retranslateUi(self, Admin_View):
		_translate = QtCore.QCoreApplication.translate
		Admin_View.setWindowTitle(_translate("Admin_View", "MainWindow"))
		self.signups_accept_button.setText(_translate("Admin_View", "Accept"))
		self.signups_table.headerItem().setText(0, _translate("Admin_View", "id"))
		self.signups_table.headerItem().setText(1, _translate("Admin_View", "id_user"))
		self.signups_table.headerItem().setText(2, _translate("Admin_View", "id_event"))
		self.signups_table.headerItem().setText(3, _translate("Admin_View", "type"))
		self.signups_table.headerItem().setText(4, _translate("Admin_View", "catering"))
		self.signups_decline_button.setText(_translate("Admin_View", "Decline"))
		self.user_add_button.setText(_translate("Admin_View", "Add"))
		self.user_delete_button.setText(_translate("Admin_View", "Delete"))
		self.user_table.headerItem().setText(0, _translate("Admin_View", "id"))
		self.user_table.headerItem().setText(1, _translate("Admin_View", "name"))
		self.user_table.headerItem().setText(2, _translate("Admin_View", "last_name"))
		self.user_table.headerItem().setText(3, _translate("Admin_View", "login"))
		self.user_table.headerItem().setText(4, _translate("Admin_View", "password"))
		self.user_table.headerItem().setText(5, _translate("Admin_View", "email"))
		self.user_table.headerItem().setText(6, _translate("Admin_View", "permission"))
		self.user_table.headerItem().setText(7, _translate("Admin_View", "registration_date"))
		self.user_reset_password_button.setText(_translate("Admin_View", "Reset password"))
		self.events_view_button.setText(_translate("Admin_View", "Events"))
		self.users_view_button.setText(_translate("Admin_View", "Users"))
		self.log_out_button.setText(_translate("Admin_View", "Log out"))
		self.sign_ups_view_button.setText(_translate("Admin_View", "Sign ups"))
		self.event_delete_button.setText(_translate("Admin_View", "Delete"))
		self.event_add_button.setText(_translate("Admin_View", "Add"))
		self.event_modify_button.setText(_translate("Admin_View", "Modify"))
		self.events_table.headerItem().setText(0, _translate("Admin_View", "id"))
		self.events_table.headerItem().setText(1, _translate("Admin_View", "name"))
		self.events_table.headerItem().setText(2, _translate("Admin_View", "agenda"))
		self.events_table.headerItem().setText(3, _translate("Admin_View", "date"))

	def show_users_table(self):
		self.events_frame.hide()
		self.signups_frame.hide()
		self.user_frame.show()
		self.fill_users_table()

	def show_events_table(self):
		self.signups_frame.hide()
		self.user_frame.hide()
		self.events_frame.show()
		self.fill_events_table()

	def show_signups_table(self):
		self.user_frame.hide()
		self.events_frame.hide()
		self.signups_frame.show()
		self.fill_signups_table()
	
	def fill_users_table(self):
		self.user_table.clear()
		table = self.db.get_users_table()
		for item in range(len(table)):
			QtWidgets.QTreeWidgetItem(self.user_table)
			for value in range(len(table[item])):
				self.user_table.topLevelItem(item).setText(value, str(table[item][value]))
	
	def fill_events_table(self):
		self.events_table.clear()
		table = self.db.get_events_table()
		for item in range(len(table)):
			QtWidgets.QTreeWidgetItem(self.events_table)
			for value in range(len(table[item])):
				self.events_table.topLevelItem(item).setText(value, str(table[item][value]))
	
	def fill_signups_table(self):
		self.signups_table.clear()
		table = self.db.get_pending_signups()
		for item in range(len(table)):
			QtWidgets.QTreeWidgetItem(self.signups_table)
			for value in range(len(table[item])):
				self.signups_table.topLevelItem(item).setText(value, str(table[item][value]))
	
	def add_user(self):
		add_user_dialog = AddUserDialog()
		def validate_input():
			name = add_user_dialog.user_name_input.text()
			last_name = add_user_dialog.user_last_name_input.text()
			login = add_user_dialog.user_login_input.text()
			password = add_user_dialog.user_password_input.text()
			email = add_user_dialog.user_email_input.text()
			permission = add_user_dialog.user_permission_input.text()
			new_user = User(0, name, last_name, login, password, email, permission, str(datetime.date.today()))

			error_message = []
			if len(name) < 2 or len(last_name) < 2:
				error_message.append("name and last name have to be at least 2 characters long")
			if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
				error_message.append("incorrect e-mail address")
			if len(login) < 3:
				error_message.append("login has to be at least 3 characters long")
			if self.db.is_login_taken(new_user):
				error_message.append("login already in use")
			if len(password) < 8:
				error_message.append("password has to be at least 8 characters long")
			available_permissions = new_user.get_possible_permissions()
			if permission not in available_permissions:
				error_message.append(f"incorrect permission, available permissions are: {available_permissions}")
			
			if len(error_message) != 0:
				error_message = ", ".join(error_message)
				error_message = f"Error: {error_message}."
				self.parent.create_popup_window("Error", error_message)
				return
			self.db.insert_user(new_user)
			add_user_dialog.dialog.close()
			self.fill_users_table()
			self.parent.create_popup_window("Success", "Account created.")
		
		add_user_dialog.add_button.clicked.connect(validate_input)
		#add_user_dialog.cancel_button.clicked.connect(add_user_dialog.dialog.close)
		add_user_dialog.dialog.exec_()

	def delete_user(self):
		selected_user = self.user_table.currentItem()
		if selected_user is None:
			self.parent.create_popup_window("Error", "Nothing selected.")
			return
		id = selected_user.text(0)
		self.db.delete_user(id)
		self.fill_users_table()
		self.parent.create_popup_window("Success", "User deleted")
	
	def reset_users_password(self):
		selected_user = self.user_table.currentItem()
		if selected_user is None:
			self.parent.create_popup_window("Error", "Nothing selected.")
			return
		id = selected_user.text(0)
		reset_dialog = ResetUsersPasswordDialog()
		def validate_password():
			password = reset_dialog.user_password_input.text()
			if len(password) < 8:
				self.parent.create_popup_window("Error", "Password has to be at least 8 characters long.")
				return
			self.db.change_users_password(id, password)
			self.fill_users_table()
			reset_dialog.dialog.close()
			self.parent.create_popup_window("Success", "Password changed")
		reset_dialog.update_button.clicked.connect(validate_password)
		reset_dialog.dialog.exec_()
	
	def add_event(self):
		add_event_dialog = AddEventDialog()
		def validate_input():
			name = add_event_dialog.name_input.text()
			agenda = add_event_dialog.agenda_input.text()
			date = add_event_dialog.date_input.text()
			if name == "" or agenda == "" or date == "":
				self.parent.create_popup_window("Error", "Fill every position.")
				return
			try:
				datetime.datetime.strptime(date, '%Y-%m-%d')
			except:
				self.parent.create_popup_window("Error", "Wrong date format")
				return
			event = Event(0, name, agenda, date)
			self.db.insert_event(event)
			add_event_dialog.dialog.close()
			self.fill_events_table()
			self.parent.create_popup_window("Success", "Event created.")
		add_event_dialog.add_button.clicked.connect(validate_input)
		add_event_dialog.dialog.exec_()
	
	def delete_event(self):
		selected_event = self.events_table.currentItem()
		if selected_event is None:
			self.parent.create_popup_window("Error", "Nothing selected.")
			return
		id = selected_event.text(0)
		self.db.delete_event(id)
		self.fill_events_table()
		self.parent.create_popup_window("Success", "Event deleted")
	
	def modify_event(self):
		selected_event = self.events_table.currentItem()
		if selected_event is None:
			self.parent.create_popup_window("Error", "Nothing selected.")
			return
		add_event_dialog = AddEventDialog()
		def validate_input():
			id = selected_event.text(0)
			name = add_event_dialog.name_input.text()
			agenda = add_event_dialog.agenda_input.text()
			date = add_event_dialog.date_input.text()
			if name == "" or agenda == "" or date == "":
				self.parent.create_popup_window("Error", "Fill every position.")
				return
			try:
				datetime.datetime.strptime(date, '%Y-%m-%d')
			except:
				self.parent.create_popup_window("Error", "Wrong date format")
				return
			event = Event(id, name, agenda, date)
			self.db.update_event(event)
			add_event_dialog.dialog.close()
			self.fill_events_table()
			self.parent.create_popup_window("Success", "Event updated.")
		add_event_dialog.add_button.clicked.connect(validate_input)
		add_event_dialog.add_button.setText("Update")
		add_event_dialog.dialog.exec_()
	
	def accept_signup(self):
		selected_signup = self.signups_table.currentItem()
		if selected_signup is None:
			self.parent.create_popup_window("Error", "Nothing selected.")
			return
		id = selected_signup.text(0)
		self.db.accept_signup(id)
		self.fill_signups_table()
		self.parent.create_popup_window("Success", "Sign up marked as accepted.")
	
	def decline_signup(self):
		selected_signup = self.signups_table.currentItem()
		if selected_signup is None:
			self.parent.create_popup_window("Error", "Nothing selected.")
			return
		id = selected_signup.text(0)
		self.db.delete_signup(id)
		self.fill_signups_table()
		self.parent.create_popup_window("Success", "Sign up declined.")
