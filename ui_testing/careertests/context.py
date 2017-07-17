from unittest import TestCase
from ui_testing.data import general
from ui_testing.core.driver.driver import Browser
from ui_testing.careertests.pagemodels import googlecareersmodel
import importlib
import logging
import os

class GoogleCareersContext(TestCase):

    def setUp(self):
        self.google_careers_data = importlib.import_module('ui_testing.data.' + general.test_environment + '.googlecareersdata')
        self.browser = Browser(self.google_careers_data.google_careers_home_url)
        self.google_careers_model = googlecareersmodel.GoogleCareersPageModel(self.browser, general.explicit_wait_time)

    def tearDown(self):
        self.browser.driver.quit()
        os.system('taskkill /f /im chromedriver.exe')

