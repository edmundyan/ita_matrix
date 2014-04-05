import browsermobproxy
from selenium import webdriver

class ITAServer():
  """
  Abstraction of both browsermob and selenium server instances
  """
  def __init__(self):
    self.proxy = None
    self.driver = None

    self.load()

  def load(self):
    server = browsermobproxy.Server(
      "/home/eyan/tree/ita_matrix/browsermob-proxy-2.0-beta-9/bin/browsermob-proxy")
    server.start()
    self.proxy = server.create_proxy()

    profile  = webdriver.FirefoxProfile()
    profile.set_proxy(self.proxy.selenium_proxy())

    self.driver = webdriver.Firefox(firefox_profile=profile)

    # load page
    self.driver.get("http://matrix.itasoftware.com/")