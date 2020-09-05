import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

link = driver.find_element_by_link_text("Python Programming")
# This allows us to find the link that says "Python Programming and bring us to that"
link.click()

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials")) #EC = expected conditions
    )
    element.click()

    new_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))  # EC = expected conditions
    )
    new_element.click()

    time.sleep(4)
    driver.back()
    driver.back()
    driver.back()
    driver.forward()
    driver.forward()
except:
    driver.quit()
