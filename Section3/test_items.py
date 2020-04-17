import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def is_element_present(browser, how, what):
    try:
        browser.find_element(how, what)
    except (NoSuchElementException):
        return False
    return True

def test_add_button_to_the_basket_present(browser):
    browser.get(link)
    assert is_element_present(browser, By.CSS_SELECTOR, ".btn-add-to-basket"), "A button for adding an item to the basket should be present"