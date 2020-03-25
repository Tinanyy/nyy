import logging
from Common.common_fun import Common
from Common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class LoginView(Common):
    loginLanding = (By.ID, 'com.sidechef.sidechef:id/tv_landing_havaaccount')
    # 用户名
    username_type = (By.ID, 'com.sidechef.sidechef:id/et_login_username')
    password_type = (By.ID, 'com.sidechef.sidechef:id/et_login_password')
    loginBtn = (By.ID, 'com.sidechef.sidechef:id/btn_login_signin')

    # 退出操作相关元素
    button_myself = (By.ID, 'com.yiqi.hj:id/rb_tab_four')
    SeettingButton = (By.ID, 'com.yiqi.hj:id/setting')
    logoutBtn = (By.ID, 'com.yiqi.hj:id/cCenterTextId')

    def login_action(self, username, password):
        self.check_skipBtn()
        self.check_skipConfirmBtn()
        time.sleep(4)
        self.check_noGoogle()
        self.driver.find_element(*self.loginLanding).click()
        time.sleep(2)
        self.check_noGoogle()

        logging.info('============login_action==============')
        logging.info('username is:%s' % username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s' % password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    def logout_action(self):
        logging.info('=========logout_action==========')

        self.driver.find_element(*self.button_myself).click()
        self.driver.find_element(*self.SeettingButton).click()
        self.driver.find_element(*self.logoutBtn).click()


if __name__ == '__main__':
    driver= appium_desired()
    l = LoginView(driver)
    l.login_action('abcd@abcd.com','123456ABC')
   # l.logout_action()