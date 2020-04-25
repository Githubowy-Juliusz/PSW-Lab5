from PyQt5 import QtCore, QtGui, QtWidgets


class ResetUsersPasswordDialog(object):
	def __init__(self):
		self.dialog = QtWidgets.QDialog()
		self.user_password_input = QtWidgets.QLineEdit(self.dialog)
		self.user_password_input.setGeometry(QtCore.QRect(120, 40, 201, 34))
		self.user_password_input.setEchoMode(QtWidgets.QLineEdit.Password)
		self.user_password_input.setObjectName("user_password_input")
		self.update_button = QtWidgets.QPushButton(self.dialog)
		self.update_button.setGeometry(QtCore.QRect(30, 140, 171, 36))
		self.update_button.setObjectName("update_button")
		self.cancel_button = QtWidgets.QPushButton(self.dialog)
		self.cancel_button.setGeometry(QtCore.QRect(220, 140, 181, 36))
		self.cancel_button.setObjectName("cancel_button")
		_translate = QtCore.QCoreApplication.translate
		self.user_password_input.setPlaceholderText(_translate("MainWindow", "New password"))
		self.update_button.setText(_translate("MainWindow", "Update"))
		self.cancel_button.setText(_translate("MainWindow", "Cancel"))
		#
		self.cancel_button.clicked.connect(self.dialog.close)
		#