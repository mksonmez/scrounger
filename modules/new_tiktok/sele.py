
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType

PROXY = ""

capabilities = webdriver.DesiredCapabilities.CHROME
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('no-sandbox')
#chrome_options.add_argument(f'user-agent={user_agent}')

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.auto_detect = False
prox.http_proxy = PROXY
prox.ssl_proxy = PROXY
prox.add_to_capabilities(capabilities)

browser = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome('/usr/bin/chromedriver')


name = input(str('Enter a handler? \n'))
driver.get("https://www.tiktok.com/@{}?lang=en".format(name))

# tag = input(str('Enter a handler? \n'))
# driver.get("https://www.tiktok.com/tag/{}".format(tag))

driver.execute_script("!function(){var e=$$(\"a\"),n=[];for(index in e){var t=e[index].href;t.indexOf(\"video\")>-1&&(n.push(t),console.log(t))}var a=document.createElement(\"a\");a.href=\"data:attachment/text,\"+encodeURI(n.join(\"\n\")),a.target=\"_blank\",a.download=\"videolist.txt\",a.click()}();\n")

print(driver.title)

print(driver.current_url)

# driver.close()