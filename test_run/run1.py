import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner

#把测试用例作为附件发送到邮箱
def send_mail(report):
    yag=yagmail.SMTP(user="li1280208624@163.com",
                     password="li123456789",
                     host='smtp.163.com')
    subject="APP自动化测试报告"
    contents="正文，详情请查看附件"

    yag.send(['1229478118@qq.com','13016998360@163.com'],subject,contents,report)
    print('email has sent out')

if __name__=='__main__':
    test_dir= '../test_case'
#定义测试用例的目录为当前目录
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#获取当前日期和时间
    now_time=time.strftime("%Y-%m-%d %H_%M_%S")
    html_report='../report/'+ now_time +'report.html'
    print(html_report)
    fp=open(html_report,'wb')
#调用htmltsetrunner,运行测试用例
    runner=HTMLTestRunner(stream=fp,
                         title="APP测试报告",
                         description="运行环境：mac ,chrome")
    runner.run(suit)
    fp.close()
    send_mail(html_report)



