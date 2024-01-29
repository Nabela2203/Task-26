from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class SearchPage:

    def __init__(self,driver):
        self.driver = driver


    search_button_xpath = "//button/span[text()='See results']"
    signin_popup_xpath = "//button[@aria-label='Close']"
    name_box_xpath = "//div[text()='Name']"
    enter_name_box_name = "name-text-input"
    birth_date_xpath = "//div[text()='Birth date']"
    from_date_name = "birth-date-start-input"
    to_date_name = "birth-date-end-input"
    birth_day_xpath = "//div[text()='Birthday']"
    enter_birth_day_name = "birthday-input"

    # close - sign-in pop-up
    def close_signin_popup(self):
        signin = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.signin_popup_xpath)))
        signin.click()

    # to perform a series of page down and to avoid auto scrolling after each entry
    def page_scroll(self):
        for _ in range(15):
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DOWN).perform()

    # Input Boxes
    def enter_name_input_box(self, enter_name):
        name_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.name_box_xpath)))
        name_box.click()
        enter_name_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.enter_name_box_name)))
        enter_name_box.send_keys(enter_name)

    def select_birth_date(self, enter_fromdate, enter_todate):
        # Select Boxes - Birth date
        birth_date = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.birth_date_xpath)))
        birth_date.click()
        enter_from_date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.from_date_name )))
        enter_from_date.send_keys(enter_fromdate)
        enter_to_date = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.to_date_name)))
        enter_to_date.send_keys(enter_todate)

    # Birthday
    def enter_birth_day(self, enter_birthday):
        birth_day = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.birth_day_xpath)))
        birth_day.click()
        day_text_box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, self.enter_birth_day_name)))
        day_text_box.send_keys(enter_birthday)

    def click_search_button(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,self.search_button_xpath)))
        search_button.click()



