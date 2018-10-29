import requests
from urllib.request import urlopen
from multiprocessing import Pool


# 200 网页正常的返回
# 404 网页找不到
# 502 504
def get(url):
    response = requests.get(url)
    if response.status_code == 200:
        return url, response.content.decode('utf-8')


def get_urllib(url):
    ret = urlopen(url)
    return ret.read().decode('utf-8')


def call_back(args):
    url, content = args
    print(url, len(content))


if __name__ == '__main__':
    url_lst = [
        'https://www.cnblogs.com/',
        'http://www.baidu.com',
        'https://www.sogou.com/',
        'http://www.sohu.com/',
    ]
    p = Pool(5)
    for url in url_lst:
        p.apply_async(get, args=(url,), callback=call_back)
    p.close()
    p.join()
