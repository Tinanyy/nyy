import unittest
#from BSTestRunner import BSTestRunner
import HTMLTestRunner
import time
import logging
import sys
from Common.sendEmail import SendEmail
path = r'C:Users\yuanyuan.ni\PycharmProjects\AppTest'
sys.path.append(path)
sys.path.append('./Common')
sys.path.append('./test_case')
sys.path.append('./report')

#指定测试用例和测试报告的路径
test_dir = '../test_case'
report_dir = '../report'

if __name__=='__main__':

   #加载测试用例
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
   # 定义报告的文件格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report = report_dir
    filename = report_dir + '/' + now + ' test_report.html'
    print(filename)
    #运行用例并生成测试报告
#with open(report_name, 'wb') as f:
    fp=open(filename,'wb')
   # runner = BSTestRunner(stream=fp, title="SideChef Test Report", description="SideChef Andriod app Test Report")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'SideChef Test Report', description=u'SideChef Andriod app Test Report')
    logging.info("start run testcase...")
    runner.run(discover)
    fp.close()
    # 向指定邮箱发送测试报告的html文件
    time.sleep(6)
    # 查找最新生成的测试报告地址
    new_report = SendEmail.new_report(test_report)
    # 自动发送邮件
    SendEmail().send_email(new_report)
