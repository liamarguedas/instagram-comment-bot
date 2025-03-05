from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
class Bot:

    def __init__(self) -> None:
        self.driver = self.configure_driver()



    def configure_driver(self):
        """todo"""

        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            service = Service(ChromeDriverManager().install()),
            options = options
        )

        return driver

    def login(self, username: str, password: str):

        self.driver.get("https://www.instagram.com/")
        self.driver.find_element(
            By.XPATH,
            '//*[@id="loginForm"]/div[1]/div[1]/div/label/input'
        ).send_keys(username)
        self.driver.find_element(
            By.XPATH,
            '//*[@id="loginForm"]/div[1]/div[2]/div/label/input'
        ).send_keys(password)

        self.driver.find_element(
            By.XPATH,
            '//*[@id="loginForm"]/div[1]/div[3]/button'
        ).click()

        time.sleep(5)

        self.driver.get("https://www.instagram.com/direct/inbox/")

        input()

        


    
