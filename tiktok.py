from time import sleep
import csv
import urllib.request
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_chromedriver(driver_location, show_browser=False, has_driver=False):
  from selenium.webdriver.chrome.options import Options
  chrome_options = Options()
  if not show_browser:
    chrome_options.add_argument("--headless")
  if has_driver:
    return webdriver.Chrome(options=chrome_options)
  else:
    return webdriver.Chrome(driver_location, options=chrome_options)

def main(driver_location="./chromedriver", driver=None, has_driver=False):
  parser = argparse.ArgumentParser()
  parser.add_argument("username", help="The TikTok username", type=str)
  parser.add_argument("--driver", help="Driver location", type=str)
  parser.add_argument("--driver-type", help="Type of driver (i.e. Chrome)", type=str)
  parser.add_argument("--show-browser", help="Shows browser while scraping. Useful for debugging", action="store_true")
  parser.add_argument("--delay", type=int, help="Number of seconds to delay between video downloading", default=0)
  parser.add_argument("--location", help="Location to store the files")

  args = parser.parse_args()

  if not args.driver:
    if not os.path.isfile(driver_location):
      try:
        webdriver.Chrome()
        has_driver = True
      except:
        import AutoChromedriver
        AutoChromedriver.download_chromedriver()
  else:
    driver_location = args.driver

  if not args.driver_type:
    driver = get_chromedriver(driver_location, show_browser=args.show_browser, has_driver=has_driver)
  else:
    if args.driver_type.lower() == 'chrome':
      driver = get_chromedriver(driver_location, show_browser=args.show_browser, has_driver=has_driver)
    if args.driver_type.lower() == 'firefox':
      driver = webdriver.Firefox()

  scraper.start(driver, args.username, folder=args.location, delay=args.delay)
        
username = input("Enter username : ") 
url = 'https://www.tiktok.com/@{}?langCountry=en'.format(username)
sleep(3) # let it load first


def create_folder_if_not_exist(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

def scrape_video(driver, folder="./"):
  url = driver.find_element_by_tag_name("video").get_attribute("src")
  name = "".join(url.split("/")[3:5])
  name = os.path.join(folder, name)
  downloader.download_mp4(name, url)
  ScrapeUtils.click_corner(driver)

def start(driver, username, folder=None, delay=1):
  if folder is None:
    folder = f"./{username}"
    create_folder_if_not_exist(folder)

  url = f"https://www.tiktok.com/@{username}"
  driver.get(url)
  if not Wait(driver).for_class_name("video-feed"):
    raise Exception(f"Can't load {url}")

  print("Getting all videos...")
  ScrapeUtils.scroll_bottom(driver)

  main_elem = driver.find_element_by_tag_name("main")
  print("Preparing to download")
  for link in tqdm(main_elem.find_elements_by_tag_name("a"), desc=f"Downloading videos to {folder}"):
    try:
      link.click()
    except ElementClickInterceptedException:
      print("clicked")
    except:
      print("failed")
    else:
      scrape_video(driver, folder=folder)
    time.sleep(delay)