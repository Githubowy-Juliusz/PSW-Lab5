from PyQt5 import QtCore, QtGui, QtWidgets
from DB import DB
from LoginRegistrationView import LoginRegistrationView
from AdminView import AdminView
from UserView import UserView
import sys

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		try:
			self.db = DB()
		except:
			print("Can't connect to database:")
			self.create_popup_window("Error!", "Can't connect to database!")
			exit()
		self.login_view = LoginRegistrationView()
		self.admin_view = AdminView()
		self.user_view = UserView()
		
		#center window
		qtRectangle = self.frameGeometry()
		centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())
		self.show_login_view()
	
	def create_popup_window(self, title, message):
		popup_window = QtWidgets.QMessageBox()
		popup_window.setWindowTitle(title)
		popup_window.setText(message)
		popup_window.exec_()
	
	def show_login_view(self):
		self.login_view.setupUi(self)
		self.show()
	
	def show_admin_view(self):
		self.admin_view.setupUi(self)
		self.show()
	
	def show_user_view(self, user):
		self.user_view.setupUi(self, user)
		self.show()

app = QtWidgets.QApplication(sys.argv)
ui = MainWindow()
sys.exit(app.exec_())
