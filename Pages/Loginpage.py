from selenium.webdriver.common.by import By


#Xpath 
login_xpath = "//a[@title='Login']"



class LoginPage:

    def __init__(self, driver):
        self.driver = driver


    def click_login(self):
        self.driver.find_element(By.XPATH, login_xpath).click()

