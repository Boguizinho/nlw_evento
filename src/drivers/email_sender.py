import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_addrs, body):
    from_addr = "tvhlodx3yv2osr3b@ethereal.email"
    login = "tvhlodx3yv2osr3b@ethereal.email"
    password = "BNsD2zpUh8wk7yhYAP"

    msg = MIMEMultipart()
    msg["from"] = "viagem_confirmada@email.com"
    msg["to"] = ', '.join(to_addrs)

    msg["Subject"] = "Confirmação da Viagem!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)
    
    server.quit()