from appium import webdriver
import yaml
import logging
import logging.config
import os
from os import path

CON_LOG='./config/log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

#log_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
#logging.config.fileConfig(log_file_path)
#logger = logging.getLogger()

def appium_desired():
    with open('./config/qsd_caps.yaml', 'r',encoding='utf-8') as file:
        data=yaml.load(file)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

   # base_dir = os.path.dirname(os.path.dirname(__file__))
  #  app_path = os.path.join(base_dir, 'app', data['appname'])
  #  desired_caps['app']=app_path

    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    # desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('start app...')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)
   # drive=webdriver.Remote('http://127.0.0.1:4723/wd/hub')
    driver.implicitly_wait(2)
    return driver

if __name__ == '__main__':
    appium_desired()

    # with open('../config/kyb_caps.yaml', 'r', encoding='utf-8') as file:
    #     data = yaml.load(file)
    #
    # base_dir=os.path.dirname(os.path.dirname(__file__))
    # print(os.path.dirname(__file__))
    # print(base_dir)
    #
    # app_path=os.path.join(base_dir,'app',data['appname'])
    # print(app_path)
