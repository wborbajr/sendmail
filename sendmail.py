import smtplib

class MailSender:
  
  def __init__(self, user="", pwd="", recipient, subject, body):
    self.__user = user
    self.__pwd = pwd
    self.__recipient = recipient
    self.__subject = subject
    self.__body = body        

  def __str__(self):
    return "User: " + str(self.__user) + " PWD: " + str(self.__pwd) + " Recipient: " + str(self.__recipient) + " Subject: " + str(self.__subject)

  def send_email(self):
    # expression_if_true if condition else expression_if_false
    __FROM = self.__user if self.__user else 'alguem.no.gmail@gmail.com'
    __PWD = self.__pwd if self.__pwd else '*******'
    __TO = self.__recipient if isinstance(self.__recipient, list) else [self.__recipient]
    __SUBJECT = self.__subject
    __TEXT = self.__body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (__FROM, ", ".join(__TO), __SUBJECT, __TEXT)
    
    # print """%s""" % (message)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(__FROM, __PWD)
        server.sendmail(__FROM, __TO, message)
        server.close()
        print 'successfully sent the mail'
    except Exception as e:
        print "failed to send mail"
        print(e)

#if __name__ == "__main__":
#    print('call send_email()')
#    send_email('xxxx@gmail.com','(xxxxx)','xxxx@gmail.com','PY_MAIL','Oi, blz?')

