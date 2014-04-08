import browsermobproxy
from selenium import webdriver

class ITAServer():
  """
  Abstraction of both browsermob and selenium server instances
  """
  def __init__(self):
    self.driver = None
    self.proxy = None
    self.server = None

    self._load()

  def __del__(self):
    # close Firefox
    self.driver.quit()

    # close browsermob
    self.server.stop()

  def _load(self):
    self.server = browsermobproxy.Server(
      "/home/eyan/tree/ita_matrix/browsermob-proxy-2.0-beta-9/bin/browsermob-proxy")
    self.server.start()
    self.proxy = self.server.create_proxy()

    profile  = webdriver.FirefoxProfile()
    profile.set_proxy(self.proxy.selenium_proxy())

    self.driver = webdriver.Firefox(firefox_profile=profile)

    # load page
    self.driver.get("http://matrix.itasoftware.com/")
