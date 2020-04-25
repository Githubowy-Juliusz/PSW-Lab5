import smtplib

class EmailSender:
	def __init__(self, email, server):
		self.email = email
		self.server = server
	
	def send_email(self, destination, name):
		with smtplib.SMTP(self.server) as smtp:
			message = f"""From: From Person <{self.email}>
To: To Person <{destination}>
Subject: Registration

Hello {name}, you successfully registered."""
			smtp.sendmail(self.email, destination, message)
