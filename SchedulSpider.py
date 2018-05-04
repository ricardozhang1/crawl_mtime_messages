#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawl_mtime.Downloader import HtmlDownloader
from crawl_mtime.HtmlParser import HtmlParser
from crawl_mtime.StorageDB import DataOutPut
import time
import random


class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutPut()

    def crawl(self,root_url):
        content = self.downloader.download(root_url)  #使用下载器下载页面,返回的是HTML页面
        urls = self.parser.parser_url(root_url,content)  #将下载的页面交给解析函数处理,返回的是电影的ID
        for url in urls:
            try:
                t = '201853'+time.strftime("%H%M%S",time.localtime())+str(random.randint(1000,9999))
                rank_url = 'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F{0}%2F&t={1}&Ajax_CallBackArgument0={2}'.format(url,t,url)

                rank_content = self.downloader.download(rank_url)
                data = self.parser.parser_json(rank_url,rank_content)
                self.output.store_data(data)
            except Exception as e:
                print("Crawl Fail")
        self.output.output_end()
        print("Crawl Finish")


if __name__ == '__main__':
    spider = SpiderMan()
    spider.crawl('http://theater.mtime.com/China_Fujian_Province_Xiamen/')


