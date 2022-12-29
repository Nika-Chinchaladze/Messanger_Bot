from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class MessangerBot:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)

    def login_messanger(self, my_log, my_pass):
        self.driver.get("https://www.messenger.com/login/")
        sleep(5)
        email = self.driver.find_element(By.ID, "email")
        email.click()
        email.send_keys(f"{my_log}")
        sleep(2)
        password = self.driver.find_element(By.ID, "pass")
        password.click()
        password.send_keys(f"{my_pass}")
        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(10)

    def send_messages(self, my_msg):
        my_accounts = self.driver.find_elements(By.CLASS_NAME, "xsyo7zv")[2:7]
        sleep(2)
        for account in my_accounts:
            account.click()
            sleep(2)
            msg_area = self.driver.find_element(By.CSS_SELECTOR, ".notranslate p")
            msg_area.click()
            sleep(2)
            msg_area.send_keys(f"{my_msg}")
            sleep(2)
            msg_area.send_keys(Keys.ENTER)
            sleep(4)
