class BaseView(object):
    '''封装公共类'''
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,*loc):
        '''查找元素'''
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        '''查找元素集'''
        return self.driver.find_elements(*loc)

    def get_window_size(self):
        '''获取窗口大小'''
        return self.driver.get_window_size()
    #滑动
    def swipe(self,start_x, start_y, end_x, end_y, duration):
        return self.driver.swipe(start_x, start_y, end_x, end_y, duration)
