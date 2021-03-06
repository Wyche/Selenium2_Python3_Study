from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import unittest, time, smtplib, os

#define sending email ------------------------------------------------------
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'uft-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = ""
    msg['To'] = ""

    smtp = smtplib.SMTP()
    smtp.connect("smtp3.hpe.com")
    #smtp.login("", "")
    smtp.sendmail("wyche_wang@outlook.com", "yi-chen.wang@hpe.com", msg.as_string())
    smtp.quit()
    print("email has send out !")

#search test report folder --------------------------------------------------   
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':

    test_dir = '.\\test_case'
    test_report = '.\\report'
    
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况: ')
    runner.run(discover)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)
