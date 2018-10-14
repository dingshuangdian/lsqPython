# Create by dingshuangdian
# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
FLAG=False
def login(func):
    def inner(*args, **kwargs):
        global FLAG
        '''登陆程序'''
        username = input('username:')
        password = input('password:')
        if username == 'boss_gold' and password == '222222':

            ret = func(*args, **kwargs)  # func是被装饰的函数
        else:
            print('登陆失败')

        return ret

    return inner


@login
def shoplist_add():
    print('增加一件物品')


@login
def shoplist_del():
    print('删除一件物品')
