from baseView.baseView import BaseView
from Common.desired_caps import appium_desired
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import os
import time
import csv


class Common(BaseView):
    skipBtn = (By.ID,'com.sidechef.sidechef:id/skipText')
    skipConfirmBtn=(By.ID,'android:id/button1')
    noGoogleBtn=(By.ID,'android:id/button1')



    def check_skipBtn(self):
        logging.info('=========check skipBtn=============')

        try:
            skipBtn = self.driver.find_element(*self.skipBtn)
        except NoSuchElementException:
            logging.info('no skipBtn')
        else:
            skipBtn.click()

    def check_skipConfirmBtn(self):
        logging.info('=========check skipConfirmBtn=============')

        try:
            skipConfirmBtn = self.driver.find_element(*self.skipConfirmBtn)
        except NoSuchElementException:
            logging.info('no skipConfirmBtn')
        else:
            skipConfirmBtn.click()
    def check_noGoogle(self):
        try:
            noGoogleBtn = self.driver.find_element(*self.noGoogleBtn)
        except NoSuchElementException:
            logging.info('no noGoogleBtn')
        else:
            noGoogleBtn.click()


    def get_screenSize(self):
        '''
        获取屏幕尺寸
        :return: 
        '''
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return (x, y)

    def getTime(self):
        self.now = time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self, module):
        time = self.getTime()
        image_file = os.path.dirname(os.path.dirname(__file__)) + '/screenshots/%s_%s.png' % (module, time)

        logging.info('get %s screenshot' % module)
        self.driver.get_screenshot_as_file(image_file)

    def check_market_ad(self):
        '''检测登录或者注册之后的界面浮窗广告'''
        logging.info('=======check_market_ad=============')
        try:
            element = self.driver.find_element(*self.wemedia_cacel)
        except NoSuchElementException:
            pass
        else:
            logging.info('close market ad')
            element.click()

    def get_csv_data(self, csv_file, line):
        logging.info('========get_csv_data========')
        with open(csv_file, 'r', encoding='utf-8-sig') as file:
          reader = csv.reader(file)
          for index, row in enumerate(reader, 1):
              if index == line:
                  return row


if __name__ == '__main__':
    driver = appium_desired()
    com=Common(driver)
    #com.check_cancelBtn()
    com.check_skipBtn()
    com.getScreenShot('startApp')
    # list = ["这", "是", "一个", "测试", "数据"]
    # for i in range(len(list)):
    #     print(i, list[i])
    # list1 = ["这", "是", "一个", "测试", "数据"]
    # for index, item, in enumerate(list1):
    #     print(index, item)

    # def get_csv_data(csv_file, line):
    #     with open(csv_file, 'r', encoding='utf-8-sig') as file:
    #         reader = csv.reader(file)
    #         for index, row in enumerate(reader, 1):
    #             if index == line:
    #                 return row
    #
    #
    # csv_file = '../data/account.csv'
    # data = get_csv_data(csv_file, 1)
    # print(data[0])
    # print(data[1])
