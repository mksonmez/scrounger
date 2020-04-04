from bs4 import BeautifulSoup
import requests
import json
import os
import time

def create_folder_if_not_exist(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

def get_user_info(self, name):
    url = 'https://www.tiktok.com/@' + name
    jsoned = ''
    try:
        jsoned = self.get_jsoned(url)
        return jsoned['/@:uniqueId']['userData']
    except:
        return {}


def get_user_videos(self, name):
    url = 'https://www.tiktok.com/@' + name
    jsoned = self.get_jsoned(url)
    return jsoned['/@:uniqueId']['itemList']


def get_trending_hashtags(self):
    url = 'https://www.tiktok.com/trending'
    jsoned = self.get_jsoned(url)
    return jsoned['/trending']['challengeList']


def get_trending_posts(self):
    url = 'https://www.tiktok.com/trending'
    jsoned = self.get_jsoned(url)
    return jsoned['/trending']['itemList']


def get_video_info(self, url):
    jsoned = self.get_jsoned(url)
    try:
        temp = jsoned['/@:uniqueId/video/:id']['videoData']
        temp['url'] = url
        return temp
    except Exception as identifier:
        print(identifier)
        return {}


def get_hash_recommend_list(self, hashtag):
    url = 'https://www.tiktok.com/tag/' + hashtag
    jsoned = self.get_jsoned(url)
    return jsoned['/tag/:name']['recommendList']


def get_videos_from_music(self, music_id, name):
    url = 'https://www.tiktok.com/music/'+name.replace(' ', '-') + music_id
    jsoned = self.get_jsoned(url)
    return jsoned['/music/*-:id']['itemList']


def get_music_recommend_list(self, music_id, name):
    url = 'https://www.tiktok.com/music' + name.replace(' ', '-') + music_id
    jsoned = self.get_jsoned(url)
    return jsoned['/music/*-:id']['recommendList']


def download_video(self, url, post_name=None):
    r = requests.get(url, stream=True)
    if post_name:
        with open(post_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                else:
                    return None
    else:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                return chunk
            else:
                return None
