import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class AdminTab_page:
    lnk_admin_xpath = "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]"
    txtbox_username_xpath = "(//input[@class='oxd-input oxd-input--active'])[2]"
    btn_search_xpath = "//button[@type='submit']"

    btn_userRollDown_xpath = "(//div[@class='oxd-select-text--after'])[1]"
    select_userRole_xapth = "//div[@role='option']"

    tableRows_xpath = "//div[@class='oxd-table-row oxd-table-row--with-border']"
    tableColumns_xpath = "//div[@class='oxd-table-cell oxd-padding-cell']"

    btn_add_xpath = "//i[@class='oxd-icon bi-plus oxd-button-icon']"


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
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def clickUserRole(self, role):
        #  Click the dropdown
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_userRollDown_xpath))
        )
        dropdown.click()

        #  Wait for options to be visible
        options = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, self.select_userRole_xapth))
        )

        # Click the option that matches the role
        for option in options:
            if option.text.strip().lower() == role.strip().lower():
                option.click()
                break

    def getNoofRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoofColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))

    def searchUserByrole(self,role):
        flag = False
        row = self.driver.find_elements(By.XPATH, self.tableRows_xpath)
        for r in range(1 ,len(row)+1):
            user_role = self.driver.find_element(By.XPATH,f"(//div[@class='oxd-table-row oxd-table-row--with-border']//div[3]//div)[{r}]").text
            print("user_role_value :",  user_role)
            if user_role.strip().lower() == role.strip().lower():
                flag = True
                break
        return flag


    def clickAdd(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()













