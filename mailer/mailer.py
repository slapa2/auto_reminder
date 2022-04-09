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
        self.use_ssl = use_ssl
        self.kwargs = {}
        if self.use_ssl:
            self.smtp = smtplib.SMTP_SSL
            self.kwargs['context'] = ssl.create_default_context()
        else:
            self.smtp = smtplib.SMTP

    def send(self, mail_from: str, mail_to: str, message: str) -> None:
        """send email method"""

        with self.smtp(
            self.smtp_server,
            self.smtp_port,
            **self.kwargs
        ) as server:

            print(f'connection: {self.smtp}, server: {self.smtp_server}, port: {self.smtp_port}')
            server.login(self.username, self.password)
            print(f'loggin to: {self.username}, password: {self.password}')
            server.sendmail(mail_from, mail_to, message)
            print(f'sended mail from: {mail_from} to {mail_to}, message: {message}')
