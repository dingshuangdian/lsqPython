# 格式化输出
# %s d

name = input('请输入姓名:')
age = input('请输入年龄:')
height = input('请输入身高:')
job = input('请输入工作:')
hobbie = input('你的爱好:')
# msg = "我叫%s,今年%s 身高%s" % (name, age, height)
msg = '''-------------info of %s --------------
Name:%s
age:%s
height:%s
job:%s
hobbie:%s
学习进度为:3%%


''' % (name, name, age, height, job, hobbie)
print(msg)

# while else

count = 0
while count <= 5:
    count += 1
    if count == 3:
        break
        print("Loop", count)
else:
    print("没被break打断循环正常执行完成！")
