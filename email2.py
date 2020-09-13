# Import smtplib for the actual sending function
import smtplib

mailobj = smtplib.SMTP('smtp.gmail.com',587)
mailobj.ehlo()
(250, 'smtp.gmail.com at your service, [103.255.4.246]\nSIZE35882577\n8BITMIME\nSTARTTLS\
nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
mailobj.starttls()
(220, '2.0.0 Ready to start TLS')
mailobj.login('zaroahmad72@gmail.com','Netlinks@123')
(235, '2.7.0 Accepted')
mailobj.sendmail('zaroahmad72@gmail.com','hakeemzaryab@gmail.com','Subject:Hello world!  Hello world! this is my first hello world email in Python')
{}
mailobj.quit()
(221, '2.0.0 closing connection b6sm4519863lfi.72 - gsmtp')