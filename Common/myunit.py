import unittest
from Common.desired_caps import appium_desired
import logging
from time import sleep


class StartEnd(unittest.TestCase):

    @classmethod
    def setUp(self):
        logging.info('======setUp=========')
        self.driver = appium_desired()

    @classmethod
    def tearDown(self):
        logging.info('======tearDown=====')
        sleep(5)
        self.driver.close_app()
