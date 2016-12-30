import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

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

#send text mail ----------------------------------------------
"""
msg = MIMEText(content,'html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = receiver
"""
#send text mail ----------------------------------------------

#send attachment file ----------------------------------------
sendfile = open('./test_project/report/login.txt', 'rb').read()

att = MIMEText(sendfile, 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="login.txt"'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)
msgRoot['To'] = receiver
#send attachment file ----------------------------------------

smtp = smtplib.SMTP()
smtp.connect(smtpserver)
#smtp.login(user, password) 
#smtp.sendmail(sender, receiver, msg.as_string())
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
