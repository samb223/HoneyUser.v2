import smtplib
from email.mime.text import MIMEText

class Emailer:
    def __init__(self, config):
        self.config = config['alerts']['email']

    def send_alert(self, event):
        msg = MIMEText(str(event))
        msg['Subject'] = 'HoneyUser Alert'
        msg['From'] = self.config['username']
        msg['To'] = self.config['to']

        with smtplib.SMTP(self.config['smtp_server'], self.config['port']) as server:
            server.starttls()
            server.login(self.config['username'], self.config['password'])
            server.send_message(msg)
