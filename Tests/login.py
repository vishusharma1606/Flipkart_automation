import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import sys

sys.path.append('/Users/vishveksharma/Desktop/Flipkart_automation')
from Pages.Loginpage import LoginPage


class SeleniumTest(unittest.TestCase):

# url and credential login 
    @classmethod
    def setUp(self):
        # self.driver = webdriver.Chrome()
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        driver = self.driver
        driver.get("https://www.flipkart.com")  
        time.sleep(5)

    def test01_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        login.click_login()
        time.sleep(15)
        print("Login_succesfull")
        time.sleep(10)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/vishveksharma/Desktop/Instagram_automation/Reports'))