
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome() # Path to your chromedriver

    def login(self):
        """Function to login, and the 'send_message' function is called in the end"""
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        """try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass"""

        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4, 6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4, 6))

        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4, 6))

        self.send_message("direct/inbox", 'Teste' )  # The second text is the message you will send

    def send_message(self, link, message):
        try:
            driver = self.driver
            driver.find_element_by_xpath("//*[contains(text(), 'Not Now')]").click()
            time.sleep(5)
            driver.get("https://www.instagram.com/" + link + "/")
            time.sleep(5)

            new_message = driver.find_elements_by_xpath("//div[@style='height: 8px; width: 8px;']")

            print(len(new_message))
            while True:
                try:
                    for message_ in new_message:
                        message_.click()
                        time.sleep(5)
                        _message = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
                        _message.clear()
                        time.sleep(5)
                        _message.send_keys(message)
                        _message.send_keys(Keys.RETURN)
                        time.sleep(5)
                except Exception as e:
                    print(e)
                    time.sleep(5)
                return False
        except Exception as e:
            print(e)
            time.sleep(5)


samuelBot = InstagramBot(
    "username", "password"
)  # User and password here
samuelBot.login()
