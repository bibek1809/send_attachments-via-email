from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
#from email.mime.base import MIMEBase
import setting as env
import csv


class SendMail:
    def __init__(self):
        pass

    def send_mail(self,sender_mail):
        FILE_NAME = 'out.csv'
        email_user ='dhakandai1@gmail.com'
        subject = 'csv file'
        
        msg = MIMEMultipart()
        msg['From'] =  email_user
        msg['To'] = sender_mail
        msg['Subject'] = subject
        
        body = 'This is csv file'
        msg.attach(MIMEText(body,'plain'))

        with open(env.FILE_PATH,'rb') as file:
            # Attach the file with filename to the email
            msg.attach(MIMEApplication(file.read(), Name = FILE_NAME))

        '''filename = 'out.csv'
        
        part = MIMEBase('application','octet_stream')
        part.set_payload(attachments.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachments; filename ="+filename)

        msg.attach(part)'''
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login(email_user,'qahrfkdbmomedqag')
        
        server.sendmail(email_user,sender_mail,text)
        server.quit()
        
