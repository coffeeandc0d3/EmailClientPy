import smtplib

to = 'justin.s9615@gmail.com'
gmail_user = 'justin.s9615@gmail.com'
gmail_pwd = 'Sinnersaved9615!!!'

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)

header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'

print (header)

msg = header + '/TCWwqJYvWlI?t=211'
smtpserver.sendmail("justin.s9615@gmail.com", to, msg)

print ('done!')

smtpserver.close()
