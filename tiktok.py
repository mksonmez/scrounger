from time import sleep
import csv
import urllib.request

def _set_driver(self, driver_choice):
    if driver_choice == Driver.CHROME:
        self._driver = webdriver.Chrome()
    elif driver_choice == Driver.FIREFOX:
        self._driver = webdriver.Firefox()
    else:
        self._driver = webdriver.PhantomJS()
    return True
        
username = input("Enter username : ") 
url = 'https://www.tiktok.com/@{}?langCountry=en'.format(username)
sleep(3) # let it load first

# set selenium to crawl url

