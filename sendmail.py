import smtplib
sender_mail="ajithdinesh242@gmail.com"
receiver_mail="ajithdinesh243@gmail.com"
passw="zrrxwymmfndkfnmz"
msg="WHATSUPP"
m=smtplib.SMTP('smtp.gmail.com')
m.starttls()
m.login(sender_mail,passw)
m.sendmail(sender_mail,receiver_mail,msg)
m.quit()

