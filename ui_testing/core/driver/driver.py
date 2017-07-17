from selenium import webdriver
from ui_testing.data import general

class Browser(object):

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(general.implicit_wait_time)
        self.driver.maximize_window()
        self.driver.get(url)

