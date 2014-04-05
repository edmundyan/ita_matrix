from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from browsermobproxy import Server

import json
import time
import pickle
import sys
import pprint

server = Server("/home/eyan/tree/ita_matrix/browsermob-proxy-2.0-beta-9/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


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
out_date.send_keys("6/16/2014")
time.sleep(1)

ret_date = driver.find_element(By.CSS_SELECTOR, "#advanced_rtReturn")
ret_date.send_keys("6/21/2014")
time.sleep(1)


proxy.new_har("google", {"captureHeaders": True, "captureContent": True})
submit = driver.find_element(By.CSS_SELECTOR, "#advanced_searchSubmitButton_label")
ActionChains(driver).click(submit).perform()



print "waiting to invis"
wait = WebDriverWait(driver, 20)
loading_msg = wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".itaLoadingMessage")))
print 'done'
har = proxy.har

with open("pickled", "w") as fp:
  pickle.dump(har, fp)

with open("f_output", "w") as out:
  def my_safe_repr(object, context, maxlevels, level):
      typ = pprint._type(object)
      if typ is unicode:
          object = str(object)
      return pprint._safe_repr(object, context, maxlevels, level)
  printer = pprint.PrettyPrinter(stream=out)
  printer.format = my_safe_repr

  printer.pprint(har)


results = None
# find the POST response
for i, entry in enumerate(har['log']['entries']):
  if (str(entry['request']['method']) == 'POST' and
      str(entry['request']['url']) ==
          "http://matrix.itasoftware.com/xhr/shop/search"):
    results = entry
    break


if not results:
  print "Nothing found!!"
  sys.exit(1)

results = results['response']['content']['text'][4:]
solution = json.loads(results)
minPrice = solution['result']['solutionList']['minPrice']

print minPrice

