from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy
import time



proxy = Proxy();
proxy.setHttpProxy("http://localhost:9090/proxy");
driver = webdriver.Firefox(proxy=proxy)
actions = ActionChains(driver)

# go to the google home page
driver.get("http://matrix.itasoftware.com/")

# Departing From
advancedfrom1 = driver.find_element(By.CSS_SELECTOR, "#advancedfrom1")
advancedfrom1.send_keys("San Francisco International, CA (SFO)")
time.sleep(1)
ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
time.sleep(1)
ActionChains(driver).key_down(Keys.RETURN).perform()
time.sleep(1)

# Destination
advancedto1 = driver.find_element(By.CSS_SELECTOR, "#advancedto1")
advancedto1.send_keys("New York, NY - All airports")
time.sleep(1)
ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()
time.sleep(1)
ActionChains(driver).key_down(Keys.RETURN).perform()
time.sleep(1)


# Outbound Date
out_date = driver.find_element(By.CSS_SELECTOR, "#advanced_rtDeparture")
out_date.send_keys("6/8/2014")
time.sleep(1)

ret_date = driver.find_element(By.CSS_SELECTOR, "#advanced_rtReturn")
ret_date.send_keys("6/13/2014")
time.sleep(1)


submit = driver.find_element(By.CSS_SELECTOR, "#advanced_searchSubmitButton_label")
ActionChains(driver).click(submit).perform()
time.sleep(1)
