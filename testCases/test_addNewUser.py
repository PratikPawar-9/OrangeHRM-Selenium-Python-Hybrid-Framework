from pageObjects.AddUser_page import AddUser_page
from pageObjects.AdminTab_page import AdminTab_page
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
import time


class Test_004_addNewUser:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    new_role = ReadConfig.setAddNewRole()
    newUserStatus = ReadConfig.setNewUserStatus()
    newUserPassword = ReadConfig.getNewUserPassword()
    newEmployeeName = ReadConfig.getNewEmployeeName()
    newUserName = ReadConfig.getNewUserName()
    newUserConfirmPwd = ReadConfig.getNewUserConfirmPwd()
    logger = LogGen.loggen()


    def test_addNewUser(self,setup):
        self.logger.info("***** Test_004_addNewUser *****")
        self.logger.info("****** Adding New User ******")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.admintab = AdminTab_page(self.driver)
        self.admintab.clickAdmin()
        self.admintab.clickAdd()

        self.logger.info("***** Adding New User *****")
        self.addusertab = AddUser_page(self.driver)
        self.addusertab.setUserRole(self.new_role)
        self.addusertab.setUserStatus(self.newUserStatus)
        self.addusertab.addNewUserPassword(self.newUserPassword)
        self.addusertab.setNewEmployeeName(self.newEmployeeName)
        self.addusertab.setNewUserName(self.newUserName)
        self.addusertab.setNewUserConfirmPassword(self.newUserConfirmPwd)
        time.sleep(3)
        self.addusertab.clickSave()
        self.logger.info("****** New User Saved Successfully *****")
        time.sleep(5)
        self.admintab.setUser(self.newUserName)
        self.admintab.clickSearch()
        time.sleep(2)

        self.msg = self.driver.find_element(By.XPATH, "(//div[@data-v-6c07a142])[1]").text
        print("Expected_user : ", self.msg)
        self.expt_user = self.newUserName
        if self.msg == self.expt_user:
            assert True == True
            self.logger.info("***** Search User by Username Successful *****")

        else:
            self.logger.info("***** Search User by Username Failed *****")
            assert True == False
        self.addusertab.deleteUser()
        self.driver.quit()




