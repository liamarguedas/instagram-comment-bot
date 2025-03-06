from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyautogui
import time

class Bot:
    """todo"""

    def __init__(self, headless=False) -> None:
        self.headless = headless
        self.driver = self.configure_driver()

    def configure_driver(self):
        """todo"""

        options = webdriver.ChromeOptions()
        if self.headless:
            options.add_argument('headless')
        options.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome(
            service = Service(ChromeDriverManager().install()),
            options = options
        )

        return driver

    def login(self, username: str, password: str):
        """todo"""

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


    def new_comment_recieved(self):
        """todo"""
        return self.driver.find_elements(
            By.CLASS_NAME,
            "x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xeuugli.x1iyjqo2")


    def read_and_send_comments(self):
        """todo"""

        comment = self.driver.find_element(
            By.CLASS_NAME,
            "x9f619.x1n2onr6.x1ja2u2z.x78zum5.xdt5ytf.x2lah0s.x193iq5w.xeuugli.x1iyjqo2")

        comment.click()

        time.sleep(3)

        reels = self.driver.find_elements(
                By.CLASS_NAME,
                "x1ey2m1c.x17qophe.xz9dl7a.xn6708d.xsag5q8.x1ye3gou.x10l6tqk.x1vjfegm"
            )

        comments = self.driver.find_elements(
                By.CLASS_NAME,
                "html-div.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1gslohp.x11i5rnm.x12nagc.x1mh8g0r.x1yc453h.x126k92a.x18lvrbx"
            )

        comment_to_post = comments[-1].text

        reels[-1].click()

        time.sleep(2)
            
        self.driver.find_element(
                    By.CSS_SELECTOR,
                "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x5ur3kl.x13fuv20.x178xt8z.x1roi4f4.x2lah0s.xvs91rp.xl56j7k.x17ydfre.x1n2onr6.x10b6aqq.x1yrsyyn.x1hrcb2b.x1pi30zi > div > form > div > textarea"
            ).click()
            
        pyautogui.write(comment_to_post)
        pyautogui.press('tab')
        pyautogui.press('enter')
        pyautogui.press('esc')

        time.sleep(2)

        self.driver.find_element(
                By.CLASS_NAME,
                "x78zum5.x4uap5.xurb0ha"
            ).click()

        time.sleep(2)


        for _ in range(5):
            pyautogui.press('tab')  

        pyautogui.press('enter')

        time.sleep(2)
        pyautogui.press('tab')
        pyautogui.press('enter')
