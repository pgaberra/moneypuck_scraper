import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import locators
from constants import URL
import page


class Scraper(unittest.TestCase):
    def setUp(self) -> None:
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)

    def test_get_player_data(self) -> None:
        # wait = WebDriverWait(self.driver, 20)
        # season_select = wait.until(EC.element_to_be_clickable(locators.PlayerPageLocators.SEASON_SELECT))
        # select = Select(season_select)
        # select.select_by_value('2021')
        players_page = page.PlayersPage(self.driver)
        player_table_element = players_page.get_player_table_element()
        rows = player_table_element.find_elements(*locators.PlayerPageLocators.ROW)
        del rows[0]  # delete headers
        player_data = []
        for player_row in rows:
            player = {}
            for i, stat in enumerate(player_row.find_elements(*locators.PlayerPageLocators.STAT)):
                if i == 2:
                    player['name'] = stat.text
                elif i == 4:
                    player['GP'] = stat.text
                elif i == 6:
                    player['xG'] = stat.text
                elif i == 7:
                    player['G'] = stat.text
                elif i == 8:
                    player['A'] = stat.text
                elif i == 52:
                    player['Corsi'] = stat.text

            player_data.append(player)

        print(player_data)
