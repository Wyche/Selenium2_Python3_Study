import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver = 'smtp3.hpe.com'

user = ''
password = ''

sender = 'wyche_wang@hpe.com'

receiver = 'yi-chen.wang@hpe.com'

subject = 'Python send email test'

content = '''
<html>
<h1>Hello,</h1>
<p>This is only an automation email, please don't replay.</p>
<h2>Thanks</h2>
</html>
'''

msg = MIMEText(content,'html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = receiver

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
#smtp.login(user, password) 
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
