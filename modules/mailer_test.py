"""mailer mdule tests"""
import email
from unittest.mock import patch
from modules.mailer import Mailer


@patch('smtplib.SMTP_SSL')
@patch('ssl.create_default_context')
def test_send_mail(mock_ssl, mock_smtp):
    """test sending emails with ssl"""

    # GIVEN
    smtp_server = 'server'
    smtp_port = 123
    mail_from = 'from@test.com'
    password = 'password'
    mail_to = 'address@email.com'
    subject = 'test subject'
    use_ssl = True
    message = 'test ,essage'

    message_to_send = email.message_from_string(message)
    message_to_send.set_charset('utf-8')
    message_to_send['Subject'] = subject
    message_to_send['From'] = mail_from
    message_to_send['To'] = mail_to
    message_to_send = message_to_send.as_string()

    # WHEN
    with Mailer(smtp_server, smtp_port, mail_from, password, use_ssl) as mailer:
        mailer.send(mail_from, mail_to, subject, message)

    # THEN
    ssl_context = mock_ssl.return_value
    server = mock_smtp.return_value
    mock_smtp.assert_called_with(smtp_server, smtp_port, context=ssl_context)
    server.sendmail.assert_called_with(mail_from, mail_to, message_to_send)


@patch('smtplib.SMTP')
def test_send_mail_no_ssl(mock_smtp):
    """test sending emails without ssl"""

    # GIVEN
    smtp_server = 'server'
    smtp_port = 123
    mail_from = 'from@test.com'
    password = 'password'
    mail_to = 'address@email.com'
    subject = 'test subject'
    use_ssl = False
    message = 'test ,essage'

    message_to_send = email.message_from_string(message)
    message_to_send.set_charset('utf-8')
    message_to_send['Subject'] = subject
    message_to_send['From'] = mail_from
    message_to_send['To'] = mail_to
    message_to_send = message_to_send.as_string()

    # WHEN
    with Mailer(smtp_server, smtp_port, mail_from, password, use_ssl) as mailer:
        mailer.send(mail_from, mail_to, subject, message)

    # THEN
    server = mock_smtp.return_value
    mock_smtp.assert_called_with(smtp_server, smtp_port)
    server.sendmail.assert_called_with(mail_from, mail_to, message_to_send)
