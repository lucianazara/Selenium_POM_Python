from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from SampleProjects.POMProject.Pages.loginPage import LoginPage
from SampleProjects.POMProject.Pages.homePage import HomePage
import HtmlTestRunner

t = 2


class LoginTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(t)

        homepage = HomePage(driver)
        time.sleep(t)
        homepage.click_welcome()
        time.sleep(t)
        homepage.click_logout()

        time.sleep(t)


    @classmethod
    def tearDown(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completado")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="reports"))