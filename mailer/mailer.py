"""
This module provides basic mailer service that allows you to send emails 
"""

import email
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
        self.use_ssl = use_ssl
        self.server = None

    def __enter__(self):
        if self.use_ssl:
            smtp = smtplib.SMTP_SSL
            smtp_kwargs = {'context': ssl.create_default_context()}
        else:
            smtp = smtplib.SMTP
            smtp_kwargs = {}

        self.server = smtp(
            self.smtp_server,
            self.smtp_port,
            **smtp_kwargs
        )
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.server.close()

    def send(self, mail_from: str, mail_to: str, subject: str, message: str) -> None:
        """send email method"""
        message_to_send = self._preper_message(mail_from, mail_to, subject, message)
        self.server.login(self.username, self.password)
        self.server.sendmail(mail_from, mail_to, message_to_send)

    @staticmethod
    def _preper_message(mail_from: str, mail_to: str,subject: str, message: str) -> str:
        prepeared_message = email.message_from_string(message)
        prepeared_message.set_charset('utf-8')
        prepeared_message['Subject'] = subject
        prepeared_message['From'] = mail_from
        prepeared_message['To'] = mail_to
        return prepeared_message.as_string()

