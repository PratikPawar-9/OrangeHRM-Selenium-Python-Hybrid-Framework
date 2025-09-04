import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddUser_page:
    drpdown_newUserRole_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
    select_newUserRole_xpath = "//div[@role='option']"

    drpdown_newUserStatus_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
    select_newUserStatus_xpath = "//div[@role='option']"

    txtbox_newUserPassword_xpath = "(//input[@type='password'])[1]"
    txtbox_employeeName_xpath = "//input[@placeholder='Type for hints...']"
    drplist_employeeNamelist_xpath = "(//div[@role='listbox']//div)[1]"
    txtbox_newUserName_xpath = "(//label[text()='Username']//following::input[@class='oxd-input oxd-input--active'])[1]"
    txtbox_newUserConfirmPwd_xpath = "//label[text()='Confirm Password']//following::input[@type='password']"
    btn_save_xpath = "//button[@type='submit']"
    btn_deleteUser_xpath = "(//button[@class='oxd-icon-button oxd-table-cell-action-space'])[1]"
    btn_deleteConfirm_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']"

    def __init__(self, driver):
        self.driver = driver

    def setUserRole(self,new_role):
        dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.drpdown_newUserRole_xpath)))
        dropdown.click()

        #  Wait for options to be visible
        options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.select_newUserRole_xpath)))

        # Click the option that matches the role
        for option in options:
            if option.text.strip().lower() == new_role.strip().lower():
                option.click()
                break

    def setUserStatus(self,newUserStatus):
        dropdown = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.drpdown_newUserStatus_xpath)))
        dropdown.click()

        #  Wait for options to be visible
        options = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, self.select_newUserStatus_xpath)))

        # Click the option that matches the role
        for option in options:
            if option.text.strip().lower() == newUserStatus.strip().lower():
                option.click()
                break

    def addNewUserPassword(self,newUserPassword):
        self.driver.find_element(By.XPATH, self.txtbox_newUserPassword_xpath).send_keys(newUserPassword)

    def setNewEmployeeName(self,newEmployeeName):
        input_box = self.driver.find_element(By.XPATH, self.txtbox_employeeName_xpath)
        input_box.send_keys("a")  # type partial text
        time.sleep(3)

        # Wait for dropdown and select the first option
        wait = WebDriverWait(self.driver, 10)
        first_option = wait.until(EC.element_to_be_clickable((By.XPATH, self.drplist_employeeNamelist_xpath)))
        first_option.click()

    def setNewUserName(self,newUserName):
        self.driver.find_element(By.XPATH, self.txtbox_newUserName_xpath).send_keys(newUserName)

    def setNewUserConfirmPassword(self,newUserConfirmPwd):
        self.driver.find_element(By.XPATH, self.txtbox_newUserConfirmPwd_xpath).send_keys(newUserConfirmPwd)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def deleteUser(self):
        self.driver.find_element(By.XPATH, self.btn_deleteUser_xpath).click()
        self.driver.find_element(By.XPATH, self.btn_deleteConfirm_xpath).click()
        time.sleep(2)





