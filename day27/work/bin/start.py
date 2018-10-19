# 获取当前文件所在路径 getcwd

from os import getcwd, path

from sys import path as sys_path

# sys_path.insert(0, path.dirname(getcwd()))
# print(getcwd())
# print(path.dirname(getcwd()))
# 修改sys.path,把学生管理系统这个路径写到sys.path列表中
# 之后所有的模块导入，都是基于学生管理系统

from day27.work.core import main

if __name__ == '__main__':
    main.main()

# start文件
# 配置文件怎么用
# 登录成功之后使用反射来获取身份对应的类
# 经常会用的功能的封装:MyPickle类
