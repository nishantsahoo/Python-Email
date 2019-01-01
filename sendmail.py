import smtplib

smtp_name = "smtp.gmail.com"
port_no = 587
server = smtplib.SMTP(smtp_name, port_no)

# Start the server
server.starttls()

# Log in to the server
email_id = "you@gmail.com"
password = ""
server.login(email_id, password)

msg = "Enter message here"
sender = "you@gmail.com"
receiver = "receiver@gmail.com"

# Send the mail
server.sendmail(sender, receiver, msg)