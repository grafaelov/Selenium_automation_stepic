import time
import math
#import pytest
from selenium import webdriver

#answer = math.log(int(time.time()))
#print(answer)

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get("https://stepik.org/lesson/236895/step/1")
    #time.sleep(1)
    text_field = browser.find_element_by_css_selector("#ember69")
    answer = math.log(int(time.time()))
    print(answer)
    text_field.send_keys(str(answer))
    submit_button = browser.find_element_by_css_selector(".submit-submission")
    submit_button.click()
    message = browser.find_element_by_id("ember78")
    assert "Correct!" in message.text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
