import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# local
import form

class RoundTrip(form.Form):
  def __init__(self, ita, options={}):
    super(RoundTrip, self).__init__(ita, options)

    self.from1 = options.get('from1', None)
    self.to1 = options.get('to1', None)
    self.out_date = options.get('out_date', None)
    self.out_span = options.get('out_span', form.Form.SPAN_THIS_DAY)
    self.return_date = options.get('return_date', None)
    self.return_span = options.get('return_span', form.Form.SPAN_THIS_DAY)

  def input_info(self):
    # Departing From
    advancedfrom1 = self.ita.driver.find_element(By.CSS_SELECTOR, '#advancedfrom1')
    advancedfrom1.send_keys(self.from1)
    time.sleep(1)
    ActionChains(self.ita.driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    ActionChains(self.ita.driver).key_down(Keys.RETURN).perform()
    time.sleep(1)

    # Destination
    advancedto1 = self.ita.driver.find_element(By.CSS_SELECTOR, "#advancedto1")
    advancedto1.send_keys(self.to1)
    time.sleep(1)
    ActionChains(self.ita.driver).key_down(Keys.ARROW_DOWN).perform()
    time.sleep(1)
    ActionChains(self.ita.driver).key_down(Keys.RETURN).perform()
    time.sleep(1)


    # Outbound Date
    out_date = self.ita.driver.find_element(By.CSS_SELECTOR, "#advanced_rtDeparture")
    out_date.send_keys(self.out_date)
    time.sleep(1)

    ret_date = self.ita.driver.find_element(By.CSS_SELECTOR, "#advanced_rtReturn")
    ret_date.send_keys(self.return_date)
    time.sleep(1)
