def emailFromHnsvill(emailBodyTextbg):
    import smtplib
    from creds import credentials

    gmailID = "hnsvill@gmail.com"
    gmailPwd = credentials(gmailID)
    recEmail = "3609044450@vtext.com"
    emailBody = emailBodyTextbg

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.ehlo()
        server.login(gmailID, gmailPwd)
        server.sendmail(gmailID, recEmail, emailBody)
        print("Email sent")
    except:
        print ("Something went wrong...")



emailFromHnsvill("ACT-W is going well!")
print("all done!")