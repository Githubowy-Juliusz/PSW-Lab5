from PyQt5 import QtCore, QtGui, QtWidgets
from EventSignup import EventSignup

class UserView(object):
	def setupUi(self, MainWindow, user):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(600, 600)
		self.central_widget = QtWidgets.QWidget(MainWindow)
		self.central_widget.setObjectName("central_widget")
		self.event_name_combobox = QtWidgets.QComboBox(self.central_widget)
		self.event_name_combobox.setGeometry(QtCore.QRect(40, 40, 231, 41))
		self.event_name_combobox.setObjectName("event_name_combobox")
		self.event_name_combobox.addItem("")
		self.event_agenda_label = QtWidgets.QLabel(self.central_widget)
		self.event_agenda_label.setGeometry(QtCore.QRect(310, 40, 221, 61))
		self.event_agenda_label.setText("")
		self.event_agenda_label.setObjectName("event_agenda_label")
		self.participation_type_combobox = QtWidgets.QComboBox(self.central_widget)
		self.participation_type_combobox.setGeometry(QtCore.QRect(40, 130, 231, 41))
		self.participation_type_combobox.setObjectName("participation_type_combobox")
		self.participation_type_combobox.addItem("")
		self.catering_combobox = QtWidgets.QComboBox(self.central_widget)
		self.catering_combobox.setGeometry(QtCore.QRect(310, 130, 231, 41))
		self.catering_combobox.setObjectName("catering_combobox")
		self.catering_combobox.addItem("")
		self.signup_button = QtWidgets.QPushButton(self.central_widget)
		self.signup_button.setGeometry(QtCore.QRect(170, 210, 251, 36))
		self.signup_button.setObjectName("signup_button")
		self.log_out_button = QtWidgets.QPushButton(self.central_widget)
		self.log_out_button.setGeometry(QtCore.QRect(170, 260, 251, 36))
		self.log_out_button.setObjectName("log_out_button")
		MainWindow.setCentralWidget(self.central_widget)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)
		self.retranslateUi(MainWindow)
		self.parent = MainWindow
		#
		self.user = user
		self.db = self.parent.db
		self.log_out_button.clicked.connect(self.log_out)
		self.signup_button.clicked.connect(self.sign_up)
		#self.event_name_combobox.activated.connect(self.fill_event_names_combobox)
		self.event_name_combobox.currentIndexChanged.connect(self.show_details)

		catering_list = ["No preference", "Vegeterian", "Gluten-free"]
		participation_type_list = ["Listener", "Author", "Backer", "Organizer"]
		self.catering_combobox.addItems(catering_list)
		self.participation_type_combobox.addItems(participation_type_list)
		
		self.fill_event_names_combobox()
		self.hide_details()
		
		#
		QtCore.QMetaObject.connectSlotsByName(self.parent)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.event_name_combobox.setItemText(0, _translate("MainWindow", "Events"))
		self.participation_type_combobox.setItemText(0, _translate("MainWindow", "Participation type"))
		self.catering_combobox.setCurrentText(_translate("MainWindow", "Catering"))
		self.catering_combobox.setItemText(0, _translate("MainWindow", "Catering"))
		self.signup_button.setText(_translate("MainWindow", "Sign up"))
		self.log_out_button.setText(_translate("MainWindow", "Log out"))

	def log_out(self):
		self.parent.show_login_view()

	def sign_up(self):
		error_message = []
		if self.participation_type_combobox.currentIndex() <= 0:
			error_message.append("you didn't pick participation type")
		if self.catering_combobox.currentIndex() <= 0:
			error_message.append("you didn't pick catering")
		if len(error_message) > 0 :
			error_message = ", ".join(error_message)
			error_message = f"Error: {error_message}."
			self.parent.create_popup_window("Error", error_message)
			return
		id_user = self.user.id
		try:
			id_event = self.db.get_event_details(self.event_name_combobox.currentText())[0][0]
		except:
			self.parent.create_popup_window("Error", "Error ocurred.")
			return
		participation_type = self.participation_type_combobox.currentText()
		catering = self.catering_combobox.currentText()
		accepted = False
		signup = EventSignup(0, id_user, id_event, participation_type, catering, accepted)
		if self.db.check_if_already_signed_up(signup):
			self.parent.create_popup_window("Error.", "You already signed up for this event.")
			return
		self.db.insert_event_signup(signup)
		self.parent.create_popup_window("Success", "You sigend up for an event.")
		self.hide_details()
		self.fill_event_names_combobox()

	
	def hide_details(self):
		self.catering_combobox.hide()
		self.participation_type_combobox.hide()
		self.event_agenda_label.hide()
		self.signup_button.setDisabled(True)
		self.catering_combobox.setCurrentIndex(0)
		self.participation_type_combobox.setCurrentIndex(0)
	
	def show_details(self):
		index = self.event_name_combobox.currentIndex()
		if index > 0:
			self.catering_combobox.show()
			self.participation_type_combobox.show()
			self.event_agenda_label.show()
			self.signup_button.setDisabled(False)
			event_name = self.event_name_combobox.currentText()
			event_details = self.db.get_event_details(event_name)
			try:
				agenda = event_details[0][2]
				date = event_details[0][3]
				self.event_agenda_label.setText(f"Date: {date}\n{agenda}")
			except:
				self.parent.create_popup_window("Error", "Error ocurred.")
				self.hide_details()
				self.fill_event_names_combobox()
		else:
			self.hide_details()

	def fill_event_names_combobox(self):
		tuples_with_names = self.db.get_event_names()
		event_names = []
		for tuple_ in tuples_with_names:
			event_names.append(tuple_[0])
		self.event_name_combobox.clear()
		self.event_name_combobox.addItem("Events")
		self.event_name_combobox.addItems(event_names)
