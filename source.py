import smtplib

#note must be using a gmail account or similar SMTP switching server: 

to = 'somebody@.gmail.com'
userAddress = 'your-email-address@.gmail.com'
userPass = 'your-pswd-here'

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(userAddress, userPass)

header = 'To:' + to + '\n' + 'From: ' + userAddress + '\n' + 'Subject:testing \n'

print (header)

msg = header + '/TCWwqJYvWlI?t=211'
smtpserver.sendmail("your-email-here-again", to, msg)

print ('done!')

smtpserver.close()
