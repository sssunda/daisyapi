import smtplib

from app.util.configs import get_config


def access_mail_server():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()

    master_email = get_config('EMAIL')
    master_password = get_config('EMAIL_PASSWORD')
    smtp.login(master_email, master_password)

    return smtp
