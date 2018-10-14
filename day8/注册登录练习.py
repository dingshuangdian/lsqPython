# Create by dingshuangdian
username = input('请输入注册的用户名:')
password = input('请输入注册的密码:')
with open('list_of_info', mode='w', encoding='utf-8') as f:
    f.write('{}\n{}'.format(username, password))
print('注册成功')
lis = []
i = 0
while i < 3:
    username = input('请输入注册的用户名:')
    password = input('请输入注册的密码:')
    with open('list_of_info', mode='r+', encoding='utf-8') as f1:
        for line in f1:
            lis.append(line)
    if username == lis[0].strip() and password == lis[1].strip():
        print('登陆成功')
        break
    else:
        print('账号或者密码错误')

    i += 1
