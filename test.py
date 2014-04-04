import pickle


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


with open("pickled", "w") as fp:
  pickle.dump(proxy.har, fp)

output = proxy.har
output = output.replace("u'", "'")
print output

server.stop()
driver.quit()