from selenium.webdriver.common.by import By
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_xpath = "//input[@aria-label='Phone number, username or email address']"
        self.password_xpath = "//input[@aria-label='Password']"
        self.login_xpath = "//div[text()='Log in']"

    def username(self):
        self.driver.find_element(By.XPATH, self.username_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys("v_i_s_h_u_s_h_a_r_m_a")

    def password(self):
        self.driver.find_element(By.XPATH, self.password_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys("Aviz@1609")

    def signup(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()



