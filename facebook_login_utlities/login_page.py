from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from facebook_testdata import credentials
from facebook_locators.facebook_login_page import LoginPageLocators

class LoginPageActions:

    def __init__(self):
        self.loginlocators = LoginPageLocators()
        self.driver = webdriver.Chrome()
        self.driver.get(credentials.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def set_username(self):
        """
        find the webelement for username ,clear the text field and set the username passed

        :return:
        """
        username_webelement = self.driver.find_element(By.ID, self.loginlocators.username_locator_id_tag)
        username_webelement.clear()
        username_webelement.send_keys(credentials.username)

    def set_password(self):
        """
        find the webelement for password ,clear the text field and set the username passed
        :return:
        """
        password_webelement = self.driver.find_element(By.ID, self.loginlocators.password_locator_id_tag)
        password_webelement.clear()
        password_webelement.send_keys(credentials.password)

    def click_login(self):
        login_button_webelement = self.driver.find_element(By.ID, self.loginlocators.login_path_locator_id)
        login_button_webelement.click()

    def login_to_facebook(self):
        self.set_username()
        self.set_password()
        sleep(2)
        self.click_login()
        sleep(2)
    def title_of_page(self):
        return self.driver.title

if __name__ == '__main__':
    LoginPageActions().login_to_facebook()
