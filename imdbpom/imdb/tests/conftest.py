import chromedriver_autoinstaller
import pytest
from selenium import webdriver
from Utilities import ReadConfigurations

@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    driver = None
    chromedriver_autoinstaller.install()
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    driver.maximize_window()  # Local variable 'driver' might be referenced before assignment, so used driver = None
    driver.implicitly_wait(10)
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()