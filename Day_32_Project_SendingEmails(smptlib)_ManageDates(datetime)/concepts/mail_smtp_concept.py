import smtplib
"""SMTP: Simple Mail Transfer Protocol
TLS = Transfer Layer Security

1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com
Hotmail: smtp.live.com
Outlook: outlook.office365.com
Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider 
e.g. "Gmail SMTP address

Instructions for Configuring Gmail with smtplib in Python:

1. Go to https://myaccount.google.com/
   - Select "Security" on the left panel.
   - Scroll down to "How you sign in to Google".
   - Enable "2-Step Verification".

2. Generate an App Password:
   - Search for "App Passwords" in your Google account settings.(if not found use this www.account.google.com/apppasswords)
   - Create a new app password by giving it a name (e.g., "Python Mail") and click "Create".
   - COPY THE PASSWORD immediately. You will only see it once.
   - This password is 16 characters long with no spaces.
   - Use this App Password in your Python code instead of your regular Gmail password.

3. SMTP Port Information:
   - By default, smtplib.SMTP uses port 25, which is often blocked by email providers due to past abuse.
   - For Gmail and most other providers, use port 587 for sending mail via external apps.
   - Update your code to specify the port explicitly:
     smtplib.SMTP("smtp.gmail.com", port=587)

These steps ensure secure and reliable sending of emails using Python and Gmail.
"""

my_gmail = "demodemouser1002@gmail.com" #user1
password = "ypwbpoabvqtnxuue" #user1 16digit code

#my_gmail = "varuntesting@myyahoo.com" #user2
#password = "" #user2 16digit code

with smtplib.SMTP("smtp.gmail.com") as connection:   #this is to connect gmail server
#with smtplib.SMTP("smtp.mail.yahoo.com") as connection:   #this is to connect yahoo email server
    connection.starttls()
    connection.login(user=my_gmail,password=password)
    """So, At this stage a mail will be sent, 
    sender can see his mail in sent tab
     receiver can see the mail in spam box"""
    '''
    Now, Goal is to make the receiver to receive the mail in inbox instead in spam
    to achieve that we need to update the below line of code by adding "Subject:" and \n\n in msg parameter
    connection.sendmail(from_addr=my_gmail,to_addrs="varuntesting@myyahoo.com",msg="Hello")  to below code
    connection.sendmail(
        from_addr=my_gmail,
        to_addrs="varuntesting@myyahoo.com",
        msg="Subject:Hello \n\n This is the body of the mail")'''
    connection.sendmail(
        from_addr=my_gmail,
        to_addrs="varuntesting@myyahoo.com",
        msg="Subject:Hello \n\n This is the body of the mail")