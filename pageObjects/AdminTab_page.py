from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminTab_page:
    lnk_admin_xpath = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]"
    txtbox_username_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    btn_seach_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def clickAdmin(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.element = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnk_admin_xpath)))
        self.element.click()

    def setUser(self,user):
       # self.driver.find_element(By.XPATH, self.txtbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_username_xpath).send_keys(user)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_seach_xpath).click()




