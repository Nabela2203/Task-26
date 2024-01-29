import pytest
from pages.SearchPage import SearchPage
from tests.conftest import setup_and_teardown

@pytest.mark.usefixtures("setup_and_teardown")
class TestImdb:
    def test_search_all(self):

        # close - sign-in pop-up
        search_page = SearchPage(self.driver)
        search_page.close_signin_popup()

        # to perform a series of page down and to avoid auto scrolling after each entry
        search_page.page_scroll()

        # Input Boxes
        search_page.enter_name_input_box("Aysha")

        # to perform a series of page down and to avoid auto scrolling after each entry
        search_page.page_scroll()

        # Select Boxes - Birth date
        search_page.select_birth_date("01-01-1960", "31-12-1970")

        # to perform a series of page down and to avoid auto scrolling after each entry
        search_page.page_scroll()

        # Birthday
        search_page.enter_birth_day("01-06")

        # Click the Search button
        search_page.click_search_button()

        exp_url = "https://www.imdb.com/search/name/?name=Aysha&birth_date=1960-01-01,1955-12-31&birth_monthday=01-06"

        # Wait for the search results page to load
        assert self.driver.current_url == exp_url


