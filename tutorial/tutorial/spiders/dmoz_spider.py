import scrapy
import re


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["book.douban.com"]
    custom_settings = {
        "USER_AGENT": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    }
    start_urls = [
        "https://book.douban.com/subject/34799583/",
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        # print(response.body)
        #(http\://)?([a-z0-9_-]+\.)+(com|net|cn|org){1}(\/[a-z0-9_-]+)*\.?(?!jpg|jpeg|gif|png|bmp)
        url = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                         str(response.body))
        print(url)
        with open('%s.txt' % filename, 'wb') as f:
            f.write(response.body)
        return url


