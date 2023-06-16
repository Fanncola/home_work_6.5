import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_manager():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1360
    browser.config.window_height = 768
    yield
    browser.quit()

