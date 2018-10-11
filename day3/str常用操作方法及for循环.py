# str常用操作方法及for循环

# 字符串的索引与切片

# 字符串的操作

s = 'lsqPython'
s1 = s.capitalize()  # 首字母大写
print(s1)
# 全大写，全小写
s2 = s.upper()
s3 = s.lower()
print(s2, s3)

# 大小写翻转
s4 = s.swapcase()
print(s4)

# 首字母大写(空格、数字或者特殊字符隔开)
s11 = 'lsq&dsd lvy'
s5 = s11.title()
print(s5)
# 填充居中
s6 = s.center(20, '#')
print(s6)
# 公共方法
l = len(s)
print(l)
# 以什么开头结尾 endswith
s7 = s.startswith('lsq')
print(s7)
s71 = s.startswith('q', 2, 5)
print(s71)
# 查找元素，返回索引,找不到返回-1
s8 = s.find('P')
print(s8)
# index通过元素找索引，找不到报错
s9 = s.index('P')
print(s9)

# strip默认删除前后空格 rstrip lstrip
# 指定删除字符
ss = '#lsqPython$       '
s10 = ss.strip('$# ')
print(s10)
# username = input('请输入名字:').strip()

# count 计数

s11 = ss.count("l")
print(s11)

# split 分割 str - -->list
sss = ';lsq;dsd;my'
s12 = sss.split(';')
print(s12)

# format的三种玩法 格式化输出
sf = '我叫{},今年{},爱好{},我叫{}'.format('lsq', 21, 'dsd', 'lsq')
print(sf)

sf1 = '我叫{0},今年{1},爱好{2},我叫{0}'.format('lsq', 21, 'dsd')
print(sf1)

sf2 = '我叫{name},今年{age},爱好{hobby},我叫{name}'.format(name='lsq', age=21, hobby='dsd')
print(sf2)

# replace

s110 = "人民日报刊发署名文章：给中国对世界的贡献算算账"
s13 = s110.replace('算', '来', 1)
print(s13)
# for 循环
s111 = 'ndkjasfnsklfnslf'
for i in s111:
    print(i)
# demo
if 'ndk' in s111:
    print("ndk存在！")
