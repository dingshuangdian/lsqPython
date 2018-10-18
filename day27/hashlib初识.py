# hashlib
# 登录认证
# 加密 --》解密
# 摘要算法
# 两个字符串：
# 不管算法多么不同，摘要的功能始终不变
# 对于相同的字符串使用同一个算法进行摘要，得到的值总是相同的
# 使用不同算法对相同的字符串进行摘要，得到的值应该不同
# 不管使用什么算法，hashlib的方式永远不变

import hashlib  # 提供摘要算法的模块

# 加盐
# 动态加盐
# 用户名 密码
# 使用用户名的一部分或者 直接使用整个用户名作为盐
md5 = hashlib.md5('加盐', encoding='utf-8')
md5.update(b'alex3714')
print(md5.hexdigest())

# 摘要算法
# 密码的密文存储
# 文件的一致性验证
# 在下载的时候 检查我们下载的文件和远程服务器上的文件是否一致
# 两台机器上的两个文件 你想检查这两个文件是否相等


# 用户 输入用户名
# 用户输入 密码
# 明文大的密码进行摘要 拿到一个密文的密码

# 写入文件

user = input('username:')
pwd = input('password:')
with open('userinfo') as f:
    for line in f:
        user, passwd, role = line.split('|')
        print(user, passwd, role)
        md5 = hashlib.md5()
        md5.update(bytes(pwd, encoding='utf-8'))
        md5_pwd = md5.hexdigest()
        print(md5_pwd)
        if user == user and md5_pwd == passwd:
            print('登录成功')

        else:
            print('登录失败')
# 整体摘要跟拆开摘要结果一样
# md5 = hashlib.md5()
# md5.update(b'alex')
# md5.update(b'3714')
# md5.hexdigest()




