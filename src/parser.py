from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import PARSER
import logging

LOGGER = logging.getLogger(PARSER)

class WebDriverError(Exception):
    pass

class FriendsParser:
    def __enter__(self):
        try:
            self._driver = webdriver.Firefox()
            self._driver.implicitly_wait(20)  # Set implicit wait once
            return self
        except Exception as ex:
            LOGGER.fatal(f"Webdriver initialization failed: {ex}")
            raise WebDriverError from ex

    def go(self, url):
        self._driver.get(url)

    def sign_in(self, log, passwd):
        login = self._driver.find_element(By.NAME, "email")
        login.send_keys(log)
        password = self._driver.find_element(By.NAME, "pass")
        password.send_keys(passwd + Keys.ENTER)

    def find_friends_page(self):
        self._driver.find_element(By.TAG_NAME, "html").send_keys(Keys.LEFT_SHIFT + Keys.LEFT_ALT + '2')
        WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='fbTimelineHeadline']//a[@data-tab-key='friends']"))
        ).send_keys(Keys.ENTER)

    def calculate_friends(self):
        friends_a = self._driver.find_elements(By.CSS_SELECTOR, "div.uiProfileBlockContent div a:first-child")
        LOGGER.info(f"Friends count: {len(friends_a)}")
        for friend in friends_a:
            LOGGER.info(f"{friend.text}: {friend.get_attribute('href')}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._driver.quit()  # Ensure driver quits only here for cleanup

