#!/usr/bin/python3

import sys
import smtplib
import getpass

sender_email_address = ''
reciever_email_address = ''
message = ''

for i in range(1, len(sys.argv)):
    item = sys.argv[i]
    if item == "-m":
        message = sys.argv[i+1]
    elif item == "--from":
        sender_email_address = sys.argv[i+1]
    elif item == "--to":
        reciever_email_address = sys.argv[i+1]


if not sender_email_address:
    sender_email_address = input("Sender's email address > ") 

    if not sender_email_address:
        print(sys.argv[0], "error: requires sender's email address")

if not reciever_email_address:
    reciever_email_address = input("Reciever's email address > ")

    if not reciever_email_address:
        print(sys.argv[0], "error: requires sender's email address")


if not message:
    message = input("Message > ")

# Starting mail service
mail = smtplib.SMTP('smtp.gmail.com', 587) 
mail.ehlo() 
mail.starttls()

pw = getpass.getpass()

mail.login(sender_email_address, pw) 
mail.sendmail(sender_email_address, reciever_email_address, message) 
mail.close()

