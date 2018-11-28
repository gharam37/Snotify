import smtplib
 

def mail(mail,data):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print('here')
    server.login("mary.maher.252@gmail.com", "0113501338")
    server.sendmail("mary.maher.252@gmail.com", mail, data)
    server.quit()
#mail("mar.mar.1234@hotmail.com","mar.mar.1234@hotmail.com")