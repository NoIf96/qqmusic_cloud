# -*- coding:utf-8 -*-
import requests
import json
import time
from multiprocessing import	 Pool
import word_cloud
import config
from crawler import Crawler

#加载预置参数
header = config.header
proxies = config.proxies

load_bg = config.load_bg    #加载背景图
to_file_base = config.to_file_base  #加载导出词云路径
song_num = config.song_num  #加载歌曲数

def getSongUrl(song_id):
    song_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?biztype=1&topid={song_id}' \
               '&cmd=8&pagesize=25&callback='.format(song_id=song_id)
    return song_url

def getQQmusicCloud(song_info):
    print("开始爬取<<{song_name}>>评论".format(song_name=song_info[0]))
    try:
        crawler = Crawler(song_info[1])
        hot_data = crawler.getHot()
        print("爬取完毕")
        print("开始生成词云")
        try:
            to_file = to_file_base + song_info[0] + '.jpg'
            word_cloud.creatWorldClound(hot_data, load_bg, to_file)
            print("生成词云完毕")
        except:
            print("生成词云失败")
    except:
        print("爬取评论失败")
    time.sleep(2)

if __name__ == '__main__':
    url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?' \
          '&topid=4&type=top&song_begin=0&song_num={song_num} &g_tk=5381&jsonpCallback='.format(song_num=song_num)
    resopnse = requests.get(url, headers=header, proxies=proxies).text
    datas_json = json.loads(resopnse)
    song_list = datas_json['songlist']
    songs_info = ([song['data']['songname'], getSongUrl(song_id = song['data']['songid'])] for song in song_list)

    print("----start----")
    pool = Pool(3)
    try:
        results = pool.map(getQQmusicCloud, songs_info)
    except Exception as e:
        print(e)

    pool.close()
    pool.join()
    print("----end----")