#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None
        url_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
        headers = {
            'User-Agent': url_agent
        }
        response = requests.get(url,headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None

if __name__ == '__main__':
    a = HtmlDownloader()
    print(a.download('http://theater.mtime.com/China_Fujian_Province_Xiamen/'))