import os
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    first_window = browser.window_handles[0]
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    value = calc(str(x))
    text_field = browser.find_element_by_id("answer")
    text_field.send_keys(value)
    submit = browser.find_element_by_css_selector(".btn-primary")
    submit.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()