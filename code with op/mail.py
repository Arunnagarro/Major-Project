import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime as dt
import log


def send_mail(Server,User,From,Password,To,Message):

    user=User
    From="arunsinghratwaana@gmail.com";
    To="arunsinghratwaana@gmail.com";
    password="9990130859";
    server=Server
    message=Message

    msg = MIMEMultipart()
  
    # storing the senders email address  
    msg['From'] = From
  
    # storing the receivers email address 
    msg['To'] = To
  
    # storing the subject 
    msg['Subject'] = f'{user}'+" "+ str(dt.date.today())
  
    # string to store the body of the mail
    body = message
  
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
    # open the file to be sent 
    #filename = "log"+f'{dt.date.today()} '+".txt"
    
    log_file=log.read_file(User)

    p = MIMEBase('application', 'octet-stream')
  
    # To change the payload into encoded form
    p.set_payload((log_file).read())
  
    # encode into base64
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename=log_file.txt")
  
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
    msg=msg.as_string()
    try :
        server.sendmail(From,To,msg)
        print("message sent to " f'{To}'+ " succeffulyy ")
        value=1
    except Exception as e :
        print("\n\n")
        print(" Error occured while  sending mail \n  "+ str(e))
        value=0

    finally :
        server.quit()
        if value==1 and not server:
            print(f'{user}'+" logout successfully . ")
        return value

def login_mail(User,From,Password):

    
    From=From
    user=User
    password=Password

    
   
    login=False
    try :

        server=smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(From,password)
        print(f'{user}'+" logged in successfully . ")
        login=True
    except Exception as e :
        login=False
        print("\n\n")
        print(" Error occured while login or sending mail \n  "+ str(e))
        value=0

    finally :
        if login==True:
            return server
        else:
            return 0

