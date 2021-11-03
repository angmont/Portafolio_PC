import smtplib
import ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = input("Ingrese el asunto del correo: ")
bod = input("Ingrese el cuerpo del correo: ")
receiver_email = input("Ingrese el correo receptor: ")
sender_email = input("Ingrese su correo: ")
password = getpass.getpass()
archivo = input("Ingrese el archivo que se enviará: ")
nombre = input("Inserte nombre(s) completo(s):")
body = (bod + " " + nombre)

def sendMail(sender_email, password, receiver_email, subject, body):
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    filename = archivo  
    with open(filename, "rb") as attachment:
    
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
 
    encoders.encode_base64(part)


    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )


    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    try:
        smtpServer = smtplib.SMTP('outlook.office365.com', 587)
        print("[+] Connecting To Mail Server.")
        smtpServer.ehlo()
        print("[+] Starting Encrypted Session.")
        smtpServer.starttls(context=context)
        smtpServer.ehlo()
        print("[+] Logging Into Mail Server.")
        smtpServer.login(sender_email, password)
        print("[+] Sending Mail.")
        smtpServer.sendmail(sender_email, receiver_email, text)
        smtpServer.close()
        print("[+] Mail Sent Successfully.")
    except:
        print("[-] Sending Mail Failed.")


sendMail(sender_email, password, receiver_email,
         subject, body)