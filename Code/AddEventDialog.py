from PyQt5 import QtCore, QtGui, QtWidgets

class AddEventDialog(object):
	def __init__(self):
		self.dialog = QtWidgets.QDialog()
		self.name_input = QtWidgets.QLineEdit(self.dialog)
		self.name_input.setGeometry(QtCore.QRect(30, 30, 171, 34))
		self.name_input.setObjectName("name_input")
		self.date_input = QtWidgets.QLineEdit(self.dialog)
		self.date_input.setGeometry(QtCore.QRect(232, 30, 181, 34))
		self.date_input.setText("")
		self.date_input.setObjectName("date_input")
		self.agenda_input = QtWidgets.QLineEdit(self.dialog)
		self.agenda_input.setGeometry(QtCore.QRect(30, 80, 381, 81))
		self.agenda_input.setText("")
		self.agenda_input.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
		self.agenda_input.setObjectName("agenda_input")
		self.add_button = QtWidgets.QPushButton(self.dialog)
		self.add_button.setGeometry(QtCore.QRect(30, 180, 171, 36))
		self.add_button.setObjectName("add_button")
		self.cancel_button = QtWidgets.QPushButton(self.dialog)
		self.cancel_button.setGeometry(QtCore.QRect(230, 180, 181, 36))
		self.cancel_button.setObjectName("cancel_button")
		_translate = QtCore.QCoreApplication.translate
		self.name_input.setPlaceholderText(_translate("MainWindow", "Name"))
		self.date_input.setPlaceholderText(_translate("MainWindow", "Date"))
		self.agenda_input.setPlaceholderText(_translate("MainWindow", "Agenda"))
		self.add_button.setText(_translate("MainWindow", "Add"))
		self.cancel_button.setText(_translate("MainWindow", "Cancel"))
		#
		self.cancel_button.clicked.connect(self.dialog.close)
		#