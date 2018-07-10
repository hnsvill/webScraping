import smtplib
from creds import credentials

gmailID = "hnsvill@gmail.com"
gmailPwd = credentials(gmailID)
recEmail = "3609044450@vtext.com"
emailBody = "6pm.com/p/the-jetset-diaries-opal-mini-dress-lavender/product/9044544/color/427"

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.ehlo()
    server.login(gmailID, gmailPwd)
    server.sendmail(gmailID, recEmail, emailBody)
except:
    print ("Something went wrong...")
finally:
    print("Email sent")