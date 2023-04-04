from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import BasePage


class AdvancedSearchPage(BasePage):
    ADVANCE_LINK = (By.ID, "gh-as-a")
    ENTER_KEYWORDS_OR_ITEM_NUMBER = (By.ID, "_nkw")
    KEYWORD_OPTIONS = (By.ID, "s0-1-17-4[0]-7[1]-_in_kw")
    SEARCH_CATEGORIES = (By.ID,"s0-1-17-4[0]-7[3]-_sacat")
    SEARCH_BUTTON = (By.XPATH,"//button[@type='submit'][1]")
    EXPECTED_RESULTS = (By.XPATH,"//h1/span[1]")
    def click_advance_link(self):
        self.chrom.find_element(*self.ADVANCE_LINK).click()

    def enter_keywords_or_item_number(self, item):
        self.chrom.find_element(*self.ENTER_KEYWORDS_OR_ITEM_NUMBER).send_keys(item)

    def select_keyword_options(self, option):
        keyword_options = Select( self.chrom.find_element( *self.KEYWORD_OPTIONS ) )
        keyword_options.select_by_visible_text( option )

    def select_search_category(self, category):
        search_category = Select( self.chrom.find_element( *self.SEARCH_CATEGORIES ) )
        search_category.select_by_visible_text( category )

    def click_search_button(self):
        self.chrom.find_element( *self.SEARCH_BUTTON ).click()

    def expected_results(self, results_no):
        result = self.chrom.find_element(*self.EXPECTED_RESULTS).text
        result = result.replace(",", "")
        assert int(result)> int(results_no), f"Error: The result is {result} while the espected result is {results_no}"
