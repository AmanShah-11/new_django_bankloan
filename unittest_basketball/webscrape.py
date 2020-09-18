# All packages needed
# import unittest
# import time
# import selenium
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Options used to ignore SSL errors and Certificate errors that occur when webscraping
PATH = "C:\Program Files (x86)\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# DesiredCapabilities handlSSLErr = DesiredCapabilities.chrome ()
# handlSSLErr.setCapability (CapabilityType.ACCEPT_SSL_CERTS, true)
driver = webdriver.Chrome(PATH, options=options)

# Global variables used
WEBSITE = "https://fantasydata.com/nba/fantasy-basketball-leaders?scope=1&season=2020&seasontype=3&conference=1"
LOAD_TIME = 8  # Amount of time needed to load the website
WAIT_TIME = 5  # Amount of time I allocate to allow the website to wait
ROW_AMOUNT = 300  # The number of rows per webpage
NUM_CATEGORIES = 19  # This is excluding player name and ranking and team and positions and games


# Class used for Web scraping
class Webscrape:

    def __init__(self):
        self.driver = driver

    def navigation(self):
        self.driver.get(WEBSITE)
        self.driver.implicitly_wait(LOAD_TIME)
        try:
            element = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "300")))
            element.click()
        except:
            print("Couldn't find 300 button")
            self.driver.quit()
        self.driver.maximize_window()
        self.driver.implicitly_wait(WAIT_TIME)
        # self.driver.set_page_load_timeout(WAIT_TIME)

    @staticmethod
    def merge(list1, list2):
        merged_list = [(list1[i], list2[i]) for i in range(0, len(list1))]
        return merged_list

    def get_basketball_lists(self):
        count = 0
        basketball_name_list = []
        basketball_ranking_list = []
        # Used to locate the table where all the information is kept
        table = self.driver.find_element_by_class_name("k-grid-content-locked")
        # Used to find all row elements
        rows = table.find_elements_by_tag_name("tr")
        # Gets the names and rankings of all basketball player lists
        while count < ROW_AMOUNT:
            for element in rows:
                basketball_name = element.find_element_by_css_selector("a").text
                basketball_name_list.append(basketball_name)
                basketball_ranking = element.find_element_by_class_name("ng-binding").text
                basketball_ranking_list.append(basketball_ranking)
                count = count + 1
        return basketball_ranking_list, basketball_name_list

    def get_basketball_stats(self):
        count_row = 0
        count_column = 0
        basketball_row_stats = []
        basketball_column_stats = []
        # Used to locate the table where all the information is kept
        table = self.driver.find_element_by_css_selector("div.k-grid-content.k-auto-scrollable")
        # Used to find all rows elements
        rows = table.find_elements_by_css_selector("tr.ng-scope")

        '''
        I'm going to split this up into 3 components:
        Part 1 is for the team name (has an a tag)
        Part 2 is for the position and number of games (has span tags)
        Part 3 is for everything else to the right of it (has no extra tags)
        '''

        ''' Change 3 on next line to NUM_CATEGORIES after done testing for this function'''
        while count_row < 3:
            # Used to find all the column elements in each individual row
            for row in rows:
                columns = row.find_elements_by_tag_name("td")
                # Inspects each column element and gets the text from the column
                for column in columns:
                    # Part 1
                    if count_column < 1:
                        column_stat = column.find_element_by_tag_name("a").text
                        # print(column_stat)
                        # Uses temporary list to put all of one player's info in one list
                        basketball_column_stats.append(column_stat)
                        count_column = count_column + 1
                    # Part 2
                    elif 1 <= count_column < 3:
                        column_stat = column.find_element_by_class_name("ng-binding").text
                        # Uses temporary list to put all of one player's info in one list
                        # print(column_stat)
                        basketball_column_stats.append(column_stat)
                        count_column = count_column + 1
                    # Part 3
                    else:
                        # column_stat = column.find_element_by_xpath(".").text
                        # Uses temporary list to put all of one player's info in one list
                        basketball_column_stats.append(column.text)
                # Puts all the players info into a list of lists
                basketball_row_stats.append(basketball_column_stats)
                count_column = 0
                count_row = count_row + 1
        return basketball_row_stats
