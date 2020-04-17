import time
import math
import pytest
from selenium import webdriver

answer = math.log(int(time.time()))
expected = "Correct!"
final = []

#print(answer)


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
#@pytest.mark.parametrize('number', ["236895"])
def test_insert_correct_answer(browser, number):
    #link = f"http://selenium1py.pythonanywhere.com/{language}/"
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)
    text_field = browser.find_element_by_css_selector("#ember69")
    answer = math.log(int(time.time()))
    print(answer)
    text_field.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    #message = browser.find_element_by_id("ember78")
    message = browser.find_element_by_css_selector(".smart-hints__hint")
    #print(message.text)
    actual = message.text
    print(actual)
    #assert "Correct!" in message.text
    if actual != expected:
        final.append(actual)
    print(*final)
    assert expected == actual, f"expected {expected}, got {actual}"


print(final)