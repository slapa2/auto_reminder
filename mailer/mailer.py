""" This module provides basic mailer service that allows you to send emails """

import smtplib
import ssl

class Mailer:
    """ class that allows you to send emails """

    def __init__(self, smtp_server: str, smtp_port: int, email: str, password: str) -> None:
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email = email
        self.password = password

    def send(self, mail_to: str, message: str) -> None:
        """send email method"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=context) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, mail_to, message)

