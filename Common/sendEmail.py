# email：3381350680@qq.com password：***
"""
使用一个邮箱向另一个邮箱发送测试报告的html文件，这里需要对发送邮件的邮箱进行设置，获取邮箱授权码。
username=“发送邮件的邮箱”， password=“邮箱授权码”
这里要特别注意password不是邮箱密码而是邮箱授权码。

mail_server = "发送邮箱的服务器地址"
这里常用的有 qq邮箱——"stmp.qq.com", 163邮箱——"stmp.163.com"
其他邮箱服务器地址可自行百度

"""
import os.path
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time


# 自动发送邮件
class SendEmail():
    def send_email(self, new_report):
        # 读取测试报告中的内容作为邮件的内容
        # with open(new_report, 'r', encoding='utf8') as f:
        #     mail_body = f.read()
        #     print(mail_body)
     with open(new_report, 'r', encoding='utf8') as f:
        mail_body = f.read()
        print(mail_body)
        # 发件人地址
        send_addr = 'li1280208624@163.com'
        # 收件人地址
        reciver_addr = '1229478118@qq.com'
        # 发送邮箱的服务器地址 qq邮箱是'smtp.qq.com', 136邮箱是'smtp.136.com'
        mail_server = 'smtp.163.com'
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        # 邮件标题
        subject = 'APPTest自动化测试报告' + now
        # 发件人的邮箱及邮箱授权码
        username = 'li1280208624@163.com'
        password = 'li123456789'  # 注意这里是邮箱的授权码而不是邮箱密码
        # 邮箱的内容和标题
        message = MIMEText(mail_body, 'html', 'utf8')
        message['Subject'] = Header(subject, charset='utf8')
        message['From'] = 'li1280208624@163.com'
        message['To'] = '1229478118@qq.com'
        # 发送邮件，使用的使smtp协议
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username, password)
        smtp.sendmail(send_addr, reciver_addr.split(','), message.as_string())
        smtp.quit()

    # 获取最新的测试报告地址
    def new_report(test_report):
        # 测试报告文件夹中的所有文件加入到列表
        test_reports_list = os.listdir(test_report)
        # 按照升序排序生成新的列表
        new_test_reports_list = sorted(test_reports_list)
        # 获取最新的测试报告
        the_last_report = new_test_reports_list[-1]
        # 最新的测试报告地址
        the_last_report_address = os.path.join(test_report, the_last_report)
        return the_last_report_address

    # def new_report(test_report):
    #     lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    #     lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # 按时间排序 win
    #     file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    #     print(file_new)
    #     return file_new