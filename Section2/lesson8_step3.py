import math
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
    z = int(x) + int(y)
    print(z)
    #select = Select(browser.find_element_by_tag_name("select"))
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(z))  # ищем элемент с текстом "Python"
    submit = browser.find_element_by_css_selector(".btn-default")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()