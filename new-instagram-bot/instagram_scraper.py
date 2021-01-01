import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
INSTAGRAM_URL = "https://www.instagram.com/"


class Scrape:

    def __init__(self):
        self.driver = wb.Chrome(PATH)
        self.driver.get(INSTAGRAM_URL)
        self.username, self.password = self.read_login_info()

    def read_login_info(self):
        with open("secrets.txt") as myfile:
            head = [next(myfile) for x in range(2)]
        return [head[0], head[1]]

    def login(self):
        try:
            username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.CLASS_NAME, "f0n8F "
            )))
            username.send_keys(self.username)
            time.sleep(10)
            self.driver.find_element_by_css_selector("label[class='f0n8F ']").send_keys(self.password)
            time.sleep(20)
            self.driver.find_element_by_css_selector("button[type='submit']").click()
        except:
            self.driver.quit()

    def not_now(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.ID, 'react-root'
        )))
        self.driver.find_element_by_css_selector("button[class='sqdOP yWX7d    y3zKF     ']").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
            By.ID, 'react-root'
        )))
        self.driver.find_element_by_css_selector('button[class="aOOlW   HoLwm "]').click()


if __name__ == '__main__':
    scrape_object = Scrape()
    scrape_object.login()
    scrape_object.not_now()
