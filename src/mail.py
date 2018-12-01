import smtplib
 

def mail(frommail,fromSecret,tomail,data):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print('here')
    server.login(frommail, fromSecret)
    #msg=" /n" + data
    server.sendmail(frommail, tomail, data)
    server.quit()
#mail("mar.mar.1234@hotmail.com","mar.mar.1234@hotmail.com")