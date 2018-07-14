# coding=utf-8

from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba


def creatWorldClound(data, readfile, tofile):
    backgroud_Image = plt.imread(readfile)  # 加载背景图
    word_cloud = WordCloud(background_color='white',  # 设置背景颜色
                           mask=backgroud_Image,  # 设置背景图片
                           max_words=2000,  # 设置最大现实的字数
                           font_path=r'C:\Windows\Fonts\simfang.ttf',  # 设置字体格式，如不设置显示不了中文
                           max_font_size=50,  # 设置字体最大值
                           random_state=24,  # 设置有多少种随机生成状态，即有多少种配色方案
                           )

    text = ' '.join(jieba.cut(' '.join(data), cut_all=False))  # 将评论进行分词
    word_cloud.generate(text)  # 加载分词后评论
    image_colors = ImageColorGenerator(backgroud_Image)  # 从背景图中获取颜色
    word_cloud.recolor(color_func=image_colors)
    word_cloud.to_file(tofile)  # 保存词云图
