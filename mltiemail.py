import csv, smtplib, ssl

def mltiem():

    message = 'hi {name}, your grade is {grade}'

    """Subject: Your grade

    Hi {name}, your grade is {grade}"""
    from_address = "zaroahmad72@gmail.com"
    password = input("Type your password and press enter: ")

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(from_address, password)
        with open("contacts_file.csv") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for name, email, grade in reader:
                server.sendmail(
                    from_address,
                    email,
                    message.format(name=name,grade=grade),
                )
mltiem()
want_more = input('want to send more emails? n/y')
if(want_more == 'y'):
    mltiem()
else:
    print('thanks')
    
