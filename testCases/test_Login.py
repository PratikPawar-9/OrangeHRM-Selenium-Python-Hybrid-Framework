import time

import pytest
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("******** Test_001_Login.test_homePageTitle *******")
        self.logger.info("******** Verifying Home Page Title ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("******* Home Page Title Passed *******")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******* Home Page Title Failed *******")
            assert False

    def test_login(self,setup):
        self.logger.info("******** Test_001_Login.test_login *******")
        self.logger.info("******** Verifying Login Test *******")
        self.driver = setup
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("******* Login Test Passed *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("******* Login Test Failed *******")
            assert False



