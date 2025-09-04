import pytest
from selenium.webdriver.common.by import By
from pageObjects.AdminTab_page import AdminTab_page
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


class Test_002_searchUserbyName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    user = ReadConfig.setUser()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchUserbyName(self,setup):
        self.logger.info("***** Test_002_search_User_by_Name *****")
        self.logger.info("***** Verifying User by Username *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Search User by Username")
        self.admintab = AdminTab_page(self.driver)
        self.admintab.clickAdmin()
        self.admintab.setUser(self.user)
        self.admintab.clickSearch()

        self.msg = self.driver.find_element(By.XPATH,"(//div[@data-v-6c07a142])[1]").text
        print("Expected_user : ", self.msg)
        self.expt_user = self.user
        if self.msg == self.expt_user:
            assert True == True
            self.logger.info("***** Search User by Username Successful *****")

        else:
            self.logger.info("***** Search User by Username Failed *****")
            assert True == False







