from browsermobproxy import Server
server = Server("/home/eyan/tree/ita_matrix/browsermob-proxy-2.0-beta-9/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()

from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)


proxy.new_har("google")
driver.get("http://www.google.co.uk")
print str(proxy.har) # returns a HAR JSON blob

server.stop()
driver.quit()