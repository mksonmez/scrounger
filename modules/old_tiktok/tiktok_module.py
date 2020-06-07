#! /usr/bin/env python3
import random
import requests
import sys
import argparse
import json
import os
import urllib3

from bs4 import BeautifulSoup
from useragents import *

class TiktokScraper:

	def __init__(self, username):
		if username.startswith('@'):
			self.username = username
		else:
			self.username = f'@{username}'
		
		self.create_dir()
		self.data = self.scrape_profile()
		self.save_data()
		self.print_data()

	def scrape_profile(self):

		r = requests.get(f'http://tiktok.com/{self.username}', headers={'User-Agent':random.choice(user_agents)})
		soup = BeautifulSoup(r.text, "html.parser")
		content = soup.find_all("script", attrs={"type":"application/json", "crossorigin":"anonymous"})
		content = json.loads(content[0].contents[0])
		profile_data = {"UserID":content["props"]["pageProps"]["userData"]["userId"],
			"username":content["props"]["pageProps"]["userData"]["uniqueId"],
			"nickName":content["props"]["pageProps"]["userData"]["nickName"],
			"bio":content["props"]["pageProps"]["userData"]["signature"],
			"profileImage":content["props"]["pageProps"]["userData"]["coversMedium"][0],
			"following":content["props"]["pageProps"]["userData"]["following"],
			"fans":content["props"]["pageProps"]["userData"]["fans"],
			"hearts":content["props"]["pageProps"]["userData"]["heart"],
			"videos":content["props"]["pageProps"]["userData"]["video"],
			"verified":content["props"]["pageProps"]["userData"]["verified"]}

		return profile_data

	def download_picture(self):

		r = requests.get(self.data['profileImage'])
		with open(f"{self.username}.jpg","wb") as f:
			f.write(r.content)

	def save_data(self):

		with open(f'{self.username}_profile_data.json','w') as f:
			f.write(json.dumps(self.data))
		print(f"Profile data saved to {os.getcwd()}")


	def create_dir(self):
		while True:
			os.mkdir(self.username)
			os.chdir(self.username)
			break


	def print_data(self):

		for key, value in self.data.items():
			print(f"{key.upper()}: {value}")

#
# Argument selection
#

def arg_parse():
	parser = argparse.ArgumentParser(description="TikTok Scraper")
	parser.add_argument("--username", help="Profile Username", required=True, nargs=1)
	parser.add_argument("--download", help="Downloads the user data", required=False, action='store_true')
	return parser.parse_args()

def main():
	args = arg_parse()
	if args.download == True:
		tiktok = TiktokScraper(args.username[0])
		tiktok.download_picture()
	else:
		tiktok = TiktokScraper(args.username[0])


if __name__ == "__main__":
	main()
