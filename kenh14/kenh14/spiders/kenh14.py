import scrapy
import requests
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class Kenh14VnSpider(scrapy.Spider):
    name = 'kenh14.vn'
    home_page = 'https://kenh14.vn'
    start_urls = [
        "https://kenh14.vn"
    ]

    def parse(self, response):
        with open("response/kenh14_vn.html", 'wb') as f:
            f.write(response.body)
            f.close()

        for url in response.xpath('//a/@href').extract():
            if '.html' in url or '.chn' in url:
                if 'kenh14.vn' not in url:
                    yield scrapy.Request(self.home_page + url, callback=self.parse_link)
                else:
                    yield scrapy.Request(url, callback=self.parse_link)

    def parse_link(self, response):
        file_name = response.url.split('/')[-1]
        file_name = file_name.replace('.', '_')
        file_name = file_name.replace('.chn', '')
        file_name = file_name.replace('.html', '')
        file_name = file_name + '.html'
        with open("response/%s" % file_name, 'wb') as f:
            f.write(response.body)
            f.close()
        # for item_link in response.xpath('//a/@href').extract():
        # yield scrapy.Request(self.home_page + item_link, callback=self.parse_single_item)

    #  def parse_img(self, response):
    #     os.listdir()
    #    with open("./image/%s" % response.url.split('/')[-1], 'wb+') as f:
    #       f.write(response.body)
