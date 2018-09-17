def emailFromHnsvill(emailBodyTextbg):
    import smtplib
    from credentials import creds

    gmailID = "hnsvill@gmail.com"
    gmailPwd = creds(gmailID)
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


emailFromHnsvill("Learned Linked Lists Today!!!")
# emailFromHnsvill("Credentials now removed from GitHub")
# print("all done!")