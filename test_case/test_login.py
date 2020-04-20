from Common.myunit import StartEnd
from businessView.loginView import LoginView
import unittest
import logging


class LoginTest(StartEnd):
    csv_file = '../data/account.csv'

    def test_loginError01(self):
        logging.info('=======test_login_error01=========')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,1)

        l.login_action(data[0],data[1])
       # self.assertTrue(l.check_loginStatus())

    def test_loginError02(self):
        logging.info('=======test_login_error02=========')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file,2)

        l.login_action(data[0],data[1])
        # self.assertTrue(l.check_loginStatus())

    def test_loginPass(self):
        logging.info('==========test_login_pass========')
        l=LoginView(self.driver)
        data = l.get_csv_data(self.csv_file, 3)

        l.login_action(data[0], data[1])
        # self.assertTrue(l.check_loginStatus(),msg='login fail!')

if __name__ == '__main__':
    unittest.main()
