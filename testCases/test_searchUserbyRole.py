import time

from pageObjects.AdminTab_page import AdminTab_page
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
import pytest


class Test_003_SearchUserbyRole:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    role = ReadConfig.setRole()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_searchUserbyRole(self,setup):
        self.logger.info("**** Test_003_Search_User_by_Role ****")
        self.logger.info("**** Verifying User by Role *****")
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("**** Verifying User by Role *****")
        self.admintab = AdminTab_page(self.driver)
        self.admintab.clickAdmin()
        self.admintab.clickUserRole(self.role)
        self.admintab.clickSearch()

        status = self.admintab.searchUserByrole(self.role)
        self.driver.quit()
        self.logger.info(f'role: {self.role}')

        assert True == status
        self.logger.info("**** Test_003_Search_User_by_Role Completed *****")







