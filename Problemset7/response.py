import validators
def main():
    print(mail_address(input("What's your email address? ")))
def mail_address(mail):
    result = validators.email(mail)
    if result == True:
        return "Valid"
    else:
        return "Invalid"

main()
