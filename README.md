# qqmusic_cloud
该项目爬取qq音乐当日流行音乐排行歌曲热门评论，并将热门评论导出成成词云

## 首先定位歌曲列表
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/1.png)

### 选择其中一首歌曲，进行详细分析
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/2.png)
 
### 寻找评论json数据 api信息
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/3.png)
### 查询到json数据api，分析其url api
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/4.png)
### 分析url 去除无关关键字
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/5.png)
https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=5381&jsonpCallback=jsoncallback3431176182226039&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=214182478&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&callback=jsoncallback3431176182226039&domain=qq.com&ct=24&cv=101010

精简后

https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?biztype=1&topid=214182478&cmd=8&pagesize=25&callback=

分析结论，topid=214182478为因id
### api url分析完毕，分析json数据
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/6.png)
得到以下信息
jsonDatas['hot_comment']['commentlist']  获得评论列表
jsonData['rootcommentcontent']	获得评论数据
单曲分析完毕

## 进行歌曲列表分析
### 从单曲分析得知，需从歌曲列表中获取歌曲id
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/7.png)
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/8.png)

 

## 从json数据中分析可以得到，该json中有 songid，songname数据
对该json api url进行分析，精简其url
![image](https://github.com/NoIf96/qqmusic_cloud/blob/master/markdown_imgs/9.png)
原：https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?tpl=3&page=detail&date=2018-07-03&topid=4&type=top&song_begin=0&song_num=30&g_tk=5381&jsonpCallback=MusicJsonCallbacktoplist&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0


精简后
https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?&date=2018-07-03&topid=4&type=top&song_begin=0&song_num=30 &g_tk=5381&jsonpCallback=

### 考虑所需爬取歌曲数， 修改参数num
https://c.y.qq.com/v8/fcg-bin/fcg_v8_toplist_cp.fcg?&date=2018-07-03&topid=4&type=top&song_begin=0&song_num=100 &g_tk=5381&jsonpCallback=

### 依据其json数据分析得到以下信息
datas_json['songlist']  歌曲列表
data_json['data']['songname']	  歌曲名称
data_json['data']['songid']  歌曲id

### 拼接歌曲评论json api url
https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?biztype=1&topid={ data_json['data']['songid']}&cmd=8&pagesize=25&callback=

