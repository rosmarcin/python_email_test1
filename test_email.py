# MR 2023
# Simple mail client 


import smtplib
con=smtplib.SMTP('smtp.gmail.com',587)
type(con)
con.ehlo()
#(250, b'smtp.gmail.com at your service, [37.30.61.161]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
con.starttls()
# (220, b'2.0.0 Ready to start TLS')
con.login('my@email.com','password')
#(235, b'2.7.0 Accepted')
con.sendmail('marcin.roszczyk@gmail.com','mr@marcinros.net','Subject: TEST')
{}
