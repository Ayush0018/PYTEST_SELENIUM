import pytest

from utils.config import Configuration as conf


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in Browser name Ex. Chrome or Firefox")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser.upper() == 'CHROME':
        options = webdriver.ChromeOptions()
        if conf.headless:
            options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(
            executable_path=r'C:\Users\lenovo\PycharmProjects\SELENIUM\Driver\ChromeDriver\chromedriver.exe',
            options=options)
    conf.driver = driver
    driver.implicitly_wait(conf.implicit_wait)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
    print("Test Completed")