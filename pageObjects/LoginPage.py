from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_xpath = "//input[@name='username']"
    textbox_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//button[@type='submit']"
    btn_User_xpath = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    lnk_Logout_xpath = "//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickUserIcon(self):
        self.driver.find_element(By.XPATH,self.btn_User_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.lnk_Logout_xpath).click()

    def isInvalidLoginMessage(self):
        try:
            return self.driver.find_element(By.XPATH, "//p[contains(text(),'Invalid credentials')]").is_displayed()
        except:
            return False

    def isDashboardVisible(self):
        try:
            return self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']").is_displayed()
        except:
            return False

