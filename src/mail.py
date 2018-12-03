import smtplib
 

def mail(frommail,fromSecret,tomail,data):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print('here')
    server.login(frommail, fromSecret)
    server.sendmail(frommail, tomail, data)
    server.quit()
