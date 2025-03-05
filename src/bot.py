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
        options.add_argument("--disable-blink-features=AutomationControlled")
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

        # If notification Label shows up, then click "NOT NOW"
        if self.driver.find_elements(By.CLASS_NAME, '_a9-v'):

            self.driver.find_element(By.CLASS_NAME, "_a9--._ap36._a9_1").click()

    def read_and_send_comments(self):

        retrieved_comments = self.driver.find_elements(
            By.CLASS_NAME,
            "x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xeuugli.x1iyjqo2")

        for comment in retrieved_comments:

            comment.click()

            time.sleep(5)

            reels = self.driver.find_elements(
                By.CLASS_NAME,
                "x1ey2m1c.x17qophe.xz9dl7a.xn6708d.xsag5q8.x1ye3gou.x10l6tqk.x1vjfegm"
            )

            comments = self.driver.find_elements(
                By.CLASS_NAME,
                "html-div.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1gslohp.x11i5rnm.x12nagc.x1mh8g0r.x1yc453h.x126k92a.x18lvrbx"
            )

            comment_to_post = comments[-1].text
            print(comment_to_post)

            reels[-1].click()

            time.sleep(2)
            
            self.driver.find_element(
                    By.XPATH,
            '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea'
            ).click()
            #.send_keys("test")

            input()
