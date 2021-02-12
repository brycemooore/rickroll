import sys
# Sending emails without attachments using Python.
# importing the required library. 
import smtplib 

#url to send
url = 'https://www.tomorrowtides.com/saturdays-are-for-the-boys.html'

reciever = sys.argv[1]
sender_email = 'email'
sender_password ='email password'
  
# creates SMTP session 
email = smtplib.SMTP('smtp.gmail.com', 587) 
  
# TLS for security 
email.starttls() 
  
# authentication
# compiler gives an error for wrong credential. 
email.login(sender_email, sender_password) 
  
# message to be sent 
message = "Dude you have to check this out\n" + url
  
# sending the mail 
try:
    email.sendmail(sender_email, reciever, message)     
    print("Successfully sent email")
except SMTPException:
    print ("Error: unable to send email")
  
# terminating the session 
email.quit()

