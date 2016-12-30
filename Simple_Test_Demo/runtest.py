from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import unittest, time, smtplib, os

#define sending email ------------------------------------------------------
def send_mail(file_new):
    f = open(file_new)
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'uft-8')
    msg['Subject'] = Header("自动化测试报告", 'utf-8')
    msg['From'] = "wyche_wang@outlook.com"
    msg['To'] = "yi-chen.wang@hpe.com"

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
    test_report = '.\\test_case'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

report_dir = './report'

if __name__ == '__main__':

    now = time.strftime('%Y-%m-%d %H_%M_%S')
    filename = report_dir + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='测试报告',
                            description='用例执行情况: ')

    runner.run(discover)
    fp.close()
