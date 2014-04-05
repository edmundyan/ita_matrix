import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# local
import roundtrip
import itasolution


class ITASearch(object):
  """
  Search form object
  """
  def __init__(self, ita, options = None):
    self.solution = None
    self.ita = ita

    form_type = options.get("type", None)

    if form_type == 'roundtrip':
      self.form = roundtrip.RoundTrip(self.ita, options)
    else:
      # errrr
      sys.exit(1)

  def parse_har(self, har):
    # Find the POST request
    for i, entry in enumerate(har['log']['entries']):
      if (str(entry['request']['method']) == 'POST' and
          str(entry['request']['url']) ==
              "http://matrix.itasoftware.com/xhr/shop/search"):
        results = entry
        break

    if not results:
      return None

    # hackyiness to remove "{}&&" from the response string
    results = results['response']['content']['text'][4:]
    solution = json.loads(results)
    self.solution = itasolution.ITASolution(solution['result']['solutionList'])


  def execute(self):
    # enter in form information
    self.form.input_info()

    # start recording HTTP traffic
    self.ita.proxy.new_har("itamatrix",
        {"captureHeaders": True, "captureContent": True})

    # click submit button
    submit = self.ita.driver.find_element(By.CSS_SELECTOR,
                                     "#advanced_searchSubmitButton_label")
    ActionChains(self.ita.driver).click(submit).perform()

    # wait for the results
    wait = WebDriverWait(self.ita.driver, 20)
    loading_msg = wait.until(EC.invisibility_of_element_located(
        (By.CSS_SELECTOR, ".itaLoadingMessage")))
    har = self.ita.proxy.har

    self.parse_har(har)

  def results(self):
    return self.solution.minPrice()



