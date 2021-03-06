# coding:utf-8
from com.cz2415.girl_spider import url_manger, html_parser, html_outputer, html_downloader


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manger.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOuter()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print ('craw %d : %s' % (count, new_url))
                html_cout = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cout)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
            except:
                print ('Jcraw failed')
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://www.169pic.com/guoneimeinv/2018/0124/40628.html"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
