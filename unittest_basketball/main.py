# All packages needed
# import unittest
# import time
# import selenium
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# Global variables used
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
WEBSITE = "https://fantasydata.com/nba/fantasy-basketball-leaders?scope=1&season=2020&seasontype=3&conference=1"
LOAD_TIME = 10  # Amount of time needed to load the website
ROW_AMOUNT = 300  # The number of rows per webpage
NUM_CATEGORIES = 16  # This is excluding player name and ranking and team and positions and games

# Class used for webscraping
class Webscrape:

    def __init__(self, driver):
        self.driver = driver

    def navigation(self, driver):
        driver.get(WEBSITE)
        driver.implicitly_wait(LOAD_TIME)
        self.driver.find_element_by_link_text("300").click()
        driver.implicitly_wait(LOAD_TIME)

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
        return (basketball_ranking_list, basketball_name_list)

    def get_basketball_stats(self):
        count = 0
        basketball_stats_list = []
        basketball_player_stats_list = []
        # Used to locate the table where all the information is kept
        table = self.driver.find_element_by_css_selector("div.k-grid-content.k-auto-scrollable")
        # Used to find all rows elements
        rows = table.find_elements_by_class_name("ng-scope")
        '''
        I'm going to split this up into 3 components:
        1 is for the team name
        2 is for the position and number of games
        3 is for everything else to the right of it '''
        # Part 1

        while count < 1:
            # Used to find all the column elements in each individual row
            for row in rows:
                columns = row.find_elements_by_tag_name("td")
                # Inspects each column element and gets the text from it
                for column in columns:
                    column_stat = column.find_element_by_tag_name("a").text
                    # Uses temporary list to put all of one player's info in one list
                    basketball_player_stats_list.append(column_stat)
                # Puts all the players info into a list of lists
                basketball_stats_list.append(basketball_player_stats_list)
                count = count + 1
        return (basketball_stats_list)




Test_1 = Webscrape(driver)
Test_1.navigation(driver)
# rankings, names = Test_1.get_basketball_lists()
# print(Test_1.merge(rankings, names))
Test_1.get_basketball_stats()

# element = self.browser.find_element_by_css_selector("li.active a")
# print element.text



# players = [driver.find_elements_by_css_selector('tr.k-alt ng-scope')]
# print(players)
# try:
#     for player in players:
#
#         element = WebDriverWait(driver, 20).until(
#             EC.presence_of_element_located((By.LINK_TEXT, "Giannis Antetokounmpo"))) #EC = expected conditions
#         print(element.link_text)
# except:
#     driver.quit()

# print("About to quit")
#
# driver.implicitly_wait(5)
# driver.quit()

# if __name__ == "__main__":
#     main.py()