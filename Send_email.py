import smtplib
import ssl
from email.message import EmailMessage

subject = "An email from Python"
body = "Hi there this is Python"
sender = "ines.kchelfi@etudiant-enit.utm.tn"
receiver = "ines.kchelfi@etudiant-enit.utm.tn"
password = input("Enter your paswword")

message = EmailMessage()
message["From"] = sender
message ["To"] = receiver
message ["Subject"] = subject

html = f"""
<html>
   <body>
      <h1>{Subject}</h1>
      <p>{body}</p>
   </body>
</html>
"""
message.add_alternative(html,subtype = "html")  

context = ssl.create_default_context() #context for secure connection when using smtplib and connecting to gmail
print("sending mail")
with smtplib.SMTP_SSL("smtp.gmail.com", 465,  context = context ) as server : #smtp.gamil.com server to connect to  465 : port
   server.login(sender,password)
   server.sendmail(sender,receiver, message.as_string())
print("succes")