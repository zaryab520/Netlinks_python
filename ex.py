import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com', 587)
s.set_debuglevel(1)
msg = MIMEText('this is test email for multiple recepeints')
sender = 'zaroahmad72@gmail.com'
recipients = ['zaryabmerzakhil01.asio@gmail.com', 'hakeemzaryab@gmail.com']
msg['Subject'] = "multiple receiver"
msg['From'] = sender
msg['To'] = ", ".join(recipients)
s.sendmail(sender, recipients, msg.as_string())