# Create by dingshuangdian
# 闭包：嵌套函数，内部函数调用外部函数的变量
# def outer():
#     a = 1
#
#     def inner():
#         print(a)
#
#     print(inner.__closure__)  # 打印是否闭包
#
#
# outer()


def outer():
    a = 1

    def inner():
        print(a)

    return inner  # 返回函数地址


inn = outer()  # 调用函数地址
inn()  # 使用闭包好处延长变量生存时间,节省变量重复创建删除

# import urllib  #模块


# 闭包的应用
from urllib.request import urlopen


# ret = urlopen('http://www.xiaohua100.cn/index.html').read()
# print(ret)
# def get_url():
#     url = 'http://www.xiaohua100.cn/index.html'
#     ret = urlopen(url).read()
#     print(ret)
#
# get_url()

def get_url():
    url = 'https://www.taobao.com/'

    def get():
        ret = urlopen(url).read()
        print(ret)

    return get


get_func = get_url()
get_func()
