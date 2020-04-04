import mechanicalsoup
import random

from useragents import *

url = 'https://www.tiktok.com/@willsmith?lang=en'

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True
)
browser.session.headers.update({'User-Agent':random.choice(user_agents)})

browser.open(url)


videos = browser.get_current_page().selector('a')
print(videos)


browser.close()
