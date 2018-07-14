# -*- coding:utf-8 -*-
import requests
import json


class Crawler(object):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
    }

    proxies = {
        'http:': 'http://121.232.146.184',
        'https:': 'https://144.255.48.197'
    }

    def __init__(self, url):
        self.url = url

    def __getJson(self):
        try:
            datas = requests.get(self.url, headers=self.header, proxies=self.proxies).content
            return json.loads(datas)
        except:
            return None

    def getHot(self):
        try:
            jsonDatas = self.__getJson()
            hot_comments = jsonDatas['hot_comment']['commentlist']
            hot_data = [hot_comment['rootcommentcontent'] for hot_comment in hot_comments]
            return hot_data
        except:
            return None
