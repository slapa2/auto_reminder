"""
This module provides basic mailer service that allows you to send emails 
"""

import smtplib
import ssl


class Mailer:
    """ class that allows you to send emails """

    def __init__(self, smtp_server: str, smtp_port: int, username: str,
                 password: str, use_ssl: bool) -> None:

        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password
        self.kwargs = {}
        self.smtp = smtplib.SMTP

        if use_ssl:
            self.smtp = smtplib.SMTP_SSL
            self.kwargs['context'] = ssl.create_default_context()

    @staticmethod
    def _preper_message(subject, mail_to, mail_from, message):
        return  f"""\
Subject: {subject}
To: {mail_to}
From: {mail_from}

{message}"""
            

    def send(self, mail_from: str, mail_to: str, subject: str, message: str) -> None:
        """send email method"""

        message_to_send = self._preper_message(subject, mail_to, mail_from, message)        

        with self.smtp(
            self.smtp_server,
            self.smtp_port,
            **self.kwargs
        ) as server:

            server.login(self.username, self.password)
            server.sendmail(mail_from, mail_to, message_to_send)
