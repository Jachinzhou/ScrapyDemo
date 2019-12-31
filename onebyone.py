import requests
import re
from fake_useragent import UserAgent
import random

ua = UserAgent()
url = "https://book.douban.com/subject/34799583/"
custom_settings = {
    "User-Agent": ua.chrome,
}


def obo(url):
    responed = requests.get(url, headers=custom_settings)
    # (http\://)?([a-z0-9_-]+\.)+(com|net|cn|org){1}(\/[a-z0-9_-]+)*\.?(?!jpg|jpeg|gif|png|bmp)
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                      str(responed.text))
    # print(urls)
    # print(urls.__len__())
    # print(urls[random.randint(1, urls.__len__())])
    return urls


if __name__ == '__main__':
    while obo(url):
        if obo(url):
            url = obo(url)[random.randint(0, obo(url).__len__())]
            print(url)

            obo(url)
        else:
            url =obo(url)[random.randint(0, obo(url).__len__())]
