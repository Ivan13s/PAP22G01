import smtplib

from email.message import EmailMessage

mail_text="""
Body would go here
"""
msg=EmailMessage()
msg.set_content(mail_text)

print(msg)
msg['Subject']=f'The contents of Body wold go here'
msg['From']= "abcd@abcdefoisahd.com"
msg['To']='mitomitokoto13@gmail.com'

username_='exppython13s@gmail.com'
password_='experimentpython13'

print(msg)
s=smtplib.SMTP_SSL('smtp.gmail.com',465)
s.login(user=username_, password=password_)
s.send_message(msg)
s.quit()
