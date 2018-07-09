import smtplib

gmailID = "hnsvill@gmail.com"
gmailPwd = input("please enter app password: ")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.ehlo()
server.login(gmailID, gmailPwd)
print ("Something went wrong...")

server.sendmail(gmailID, "3609044450@vtext.com", "Test message")