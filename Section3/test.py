from selenium import webdriver

#FirefoxProfile profile = new FirefoxProfile()
#profile.setPreference("network.proxy.type", 4)
#WebDriver driver = new FirefoxDriver(profile)
#driver.get("https://stepik.org/lesson/25969/step/8")

#fp = webdriver.FirefoxProfile('/Users/rafaelo/AppData/Roaming/Mozilla/Firefox/Profiles/uk79h21c.Selenium')

driver = webdriver.Firefox(firefox_profile="C:\Users\rafaelov\AppData\Roaming\Mozilla\Firefox\Profiles\uk79h21c.Selenium")
#driver = webdriver.Firefox(Selenium)

driver.get("https://stepik.org/lesson/25969/step/8")
