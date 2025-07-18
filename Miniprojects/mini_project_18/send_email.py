import smtplib

sender = input("From: ")
receiver = input("To: ")
msg = "Subject: Test\n\nThis is a test email."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# server.login(sender, "yourpassword")  # Use app password for Gmail
# server.sendmail(sender, receiver, msg)
# server.quit()
print("Email sent (mock)")
