from unittest.mock import patch
from .mailer import Mailer
import dotenv


@patch('smtplib.SMTP_SSL')
def test_send_mail(mock_smtp):
    smtp_server = 'server'
    smtp_port = 123
    mail_from = 'from@test.com'
    password = 'password'
    mail_to = 'address@email.com'
    message = 'test message'

    mailer = Mailer(smtp_server, smtp_port, mail_from, password)
    mailer.send(mail_to, message)
    mock_smtp.assert_called()
    context = mock_smtp.return_value.__enter__.return_value
    context.sendmail.assert_called_with(
        mail_from, mail_to, message
    )
