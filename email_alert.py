import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from dotenv import load_dotenv


response = requests.get('https://api.kanye.rest')

print(response.text)

mail_content = response.text
#The mail addresses and password
sender_address = 'ruizeduardo21@gmail.com'
sender_pass = APP_PASSWORD
receiver_email_addresses=['hwek21@gmail.com','amandaalvarezpr@gmail.com ']

#Setup the MIME
message = MIMEMultipart()

receiver_address = 'hwek21@gmail.com'

message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Automated Email :: '   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
# session.sendmail(sender_address, receiver_address, text)



for email in receiver_email_addresses:
  message['To'] = email
  session.sendmail(sender_address, email, text)
  print('Mail Sent')

session.quit()

