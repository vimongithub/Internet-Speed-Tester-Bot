from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

UAERNAME = "username"
PASSWORD = "yourpassword"

promised_down = 75
promised_up = 50

chrome_driver_path = r"C:\Path\chromedriver.exe"
speed_test = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.ser = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(speed_test)
        time.sleep(10)

        test_start = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        test_start.click()
        time.sleep(40)

        self.down = (self.driver.find_element(by=By.CLASS_NAME, value="upload-speed")).text
        self.up = (self.driver.find_element(by=By.CLASS_NAME, value="download-speed")).text


        if float(self.down) < promised_down or float(self.up) < promised_up:
            self.tweet_at_provider()
        else:
            self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)

        sign_in = self.driver.find_element(by=By.NAME, value="text")
        sign_in.send_keys(UAERNAME)

        sign_in.send_keys(Keys.ENTER)
        time.sleep(5)

        pass_in = self.driver.find_element(by=By.NAME, value="password")
        pass_in.send_keys(PASSWORD)

        pass_in.send_keys(Keys.ENTER)
        time.sleep(5)

        compose_tweet = self.driver.find_element(by=By.XPATH, value='//*[text()="Tweet"]').click()
        time.sleep(2)

        paste_tweet = self.driver.find_element(by=By.CSS_SELECTOR, value=".public-DraftEditor-content")

        paste_tweet.send_keys(f"Hey ISP, This is my current {self.up} MBPS download and {self.down} MBPS upload speed"
                              f" but i pay for {promised_up}MBPS download and {promised_down} MBPS Uploadspeed,"
                              f"kindly, resolve it ASAP.")
        time.sleep(2)
        tweet_btn = self.driver.find_element(by=By.XPATH, value='//*[text()="Tweet"]').click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()