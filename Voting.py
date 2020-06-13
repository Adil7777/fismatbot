import random
import smtplib
from config import EMAIL, PASSWORD


def create_cod():
    code = ''
    for i in range(0, 4):
        symbol = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        while symbol in code:
            symbol = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
        code += symbol

    return code


def check_mail(mail):
    if '@fizmat.kz' in mail:
        return True
    else:
        return False


def send_mail(send_to_email, code):
    try:
        message = str(code)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, send_to_email, message)
        server.quit()
        return True
    except Exception as e:
        return e
