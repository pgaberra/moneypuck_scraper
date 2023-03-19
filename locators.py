from selenium.webdriver.common.by import By


class PlayerPageLocators(object):
    PLAYERS_TABLE = (By.CSS_SELECTOR, '#includedContent > table > tbody')
    ROW = (By.XPATH, '//tr[@role="row"]')
    STAT = (By.XPATH, './/td[not(parent::th)]')
    SEASON_SELECT = (By.ID, "season_type")
