import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilies
import pytest


class Test_005_Login_ddt:
    baseURL = ReadConfig.getApplicationURL()
    path = ".\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("****** Test_Case_005_Login_ddt *****")
        self.logger.info("****** Verifying login DDT Test *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.driver.implicitly_wait(1)

        self.rows = XLUtilies.getRowCount(self.path,'Sheet1')
        print("Number of Rows in Excel File:",self.rows)

        lst_status = [] #Empty Variable List

        for r in range(2,self.rows+1):
            self.user = XLUtilies.readData(self.path,'Sheet1',r,1)
            self.password = XLUtilies.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtilies.readData(self.path,'Sheet1',r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()


            if self.lp.isDashboardVisible():
                if self.exp == "Pass":
                    lst_status.append("Pass")
                    self.lp.clickUserIcon()
                    self.lp.clickLogout()
                else:
                    lst_status.append("Fail")
            elif self.lp.isInvalidLoginMessage():
                if self.exp == "Fail":
                    lst_status.append("Pass")
                else:
                    lst_status.append("Fail")

        if all("Pass" in status for status in lst_status):
            self.logger.info("***** Login DDT Test Passed *****")
            self.logger.info(f"Final Results: {lst_status}")
            self.driver.quit()
            assert True
        else:
            self.logger.info("***** Login DDT Test Failed *****")
            self.logger.info(f"Final Results: {lst_status}")
            self.driver.quit()
            assert False

        self.logger.info("***** End of DDT Login Test *****")
        self.logger.info("***** Completed DDT Login Test 005 *****")



