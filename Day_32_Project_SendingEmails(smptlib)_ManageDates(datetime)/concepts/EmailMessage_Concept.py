
# EmailMessage Module Concept Guide

The `email.message.EmailMessage` class is part of Python's standard library for constructing and sending email messages.
It is the recommended modern way to send emails using Python, especially when dealing with Unicode content, HTML messages,
or attachments.

## Basic Usage

```python
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Your Subject Here"
msg["From"] = "your_email@example.com"
msg["To"] = "recipient@example.com"
msg.set_content("This is the body of the email.")
```

## Why Use EmailMessage?

- ✅ Automatically handles Unicode (no ASCII errors)
- ✅ Supports HTML and plain text formats
- ✅ Allows easy attachment of files
- ✅ Clean and readable message construction

## Sending with smtplib

```python
import smtplib

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("your_email@example.com", "your_password")
    server.send_message(msg)
```

## Adding HTML Content

```python
msg.set_content("This is the plain text version.")
msg.add_alternative("""<html>
  <body>
    <h1>This is an HTML Email</h1>
    <p><b>Enjoy your day!</b></p>
  </body>
</html>
""", subtype="html")
```

## Adding Attachments

```python
with open("document.pdf", "rb") as file:
    msg.add_attachment(file.read(), maintype="application", subtype="pdf", filename="document.pdf")
```

## Summary

Use `EmailMessage` for clean, Unicode-safe, and feature-rich emails in Python projects.
