from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators

class BasePage(object):
    """Base page class from which all pages derive from"""

    def __init__(self, driver) -> None:
        self.driver = driver


class PlayersPage(BasePage):
    """
    First page displayed when starting the web app, only thing we do here is to click the login button.
    Order number when displayed: 1
    """

    @staticmethod
    def has_enough_rows(driver):
        wait = WebDriverWait(driver, 30)
        players_table = wait.until(EC.presence_of_element_located(locators.PlayerPageLocators.PLAYERS_TABLE))
        rows = players_table.find_elements(*locators.PlayerPageLocators.ROW)
        return len(rows) >= 600

    def get_player_table_element(self) -> WebElement:
        wait = WebDriverWait(self.driver, 20)
        wait.until(self.has_enough_rows)
        players_table = self.driver.find_element(*locators.PlayerPageLocators.PLAYERS_TABLE)
        return players_table
