from validators import email

email_user = input("What is your email address? ")

if email(email_user):
    print("Valid")
else:
    print("Invalid")