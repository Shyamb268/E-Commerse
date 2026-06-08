import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('shyambandi532@gmail.com','fhxo qtdz odmp txpo')
    msg=EmailMessage()
    msg['FROM']='shyambandi532@gmail.com'
    msg['SUBJECT']=subject
    msg['TO']=to
    msg.set_content(body)
    server.send_message(msg)
    server.close()