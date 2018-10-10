# 使用while循环输入123456 8910
num = 0
while num < 10:
    num += 1
    if num == 7:
        continue
    print(num)
# 求1-100的所有数的和
num1 = 0
total = 0
while num1 < 100:
    num1 += 1
    total = total + num1
print(total)

# 输出1-100内的所有奇数
num2 = 1
while num2 < 101:
    print(num2)
    num2 += 2
# 方法二:
count = 1
while count < 101:
    if count % 2 == 1:
        print(count)
    count += 1
# 输出1-100内所有的偶数
num3 = 0
while num3 < 98:
    num3 += 2
    print(num3)
# 求1-2+3-4+5...99的所有数的和
num4 = 0
total1 = 0
while num4 < 99:
    num4 += 1
    if num4 % 2 != 0:
        total1 = total1 + num4
    else:
        total1 = total1 - num4

print(total1)

# 用户登录(三次机会重试)
n = 1
while n <= 3:
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    n += 1

print("用户名密码错误超过3次，账号被锁定！")
