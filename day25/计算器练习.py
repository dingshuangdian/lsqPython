"""
实现能计算类似
1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))

等类似公式的计算器程序
"""
import re


# 表达式
def dealwith(express):
    # 将表达式中的符号处理了 +-替换成- --替换成+
    express_ = express.replace('+-', '-')
    express_ = express.replace('--', '+')
    return express_


def cal_exp_son(exp_son):
    # 只用来计算原子型的表达式  两个数之间的乘除法
    if '/' in exp_son:
        a, b = exp_son.split('/')
        return str(float(a) / float(b))
    elif '*' in exp_son:
        a, b = exp_son.split('*')
        return str(float(a) * float(b))


"""
# 计算么有括号的表达式
    # exp是没有经过处理的最内层带括号的表达式
    # 去空格"""


def cal_express_no_bracket(exp):
    exp = exp.strip('()')
    # 先乘除后加减
    while True:
        ret = re.search('\d+\.?\d*[*/]-?\d+\.?\d*', exp)
        if ret:
            exp_son = ret.group()  # 子表达式 最简单的 乘除法
            ret = cal_exp_son(exp_son)
            exp = exp.replace(exp_son, ret)
            exp = dealwith(exp)
        else:
            ret = re.findall('-?\d+\.?\d*', exp)
            sum = 0
            for i in ret:
                sum += float(i)
            return str(sum)


# 提取括号里面没有其他括号的表达式
def remove_bracket(new_express):
    while True:
        ret = re.search('\([^()]+\)', new_express)
        if ret:
            express_no_bracket = ret.group()  # 表达式，没括号
            print('匹配到内部不再有括号的值', express_no_bracket)
            ret = cal_express_no_bracket(express_no_bracket)
            new_express = new_express.replace(express_no_bracket, ret)
            new_express = dealwith(new_express)
        else:
            print('表达式中已经没有括号了:', new_express)
            ret = cal_express_no_bracket(new_express)
            return ret
            break


express = '1-2*((60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

new_express = express.replace(' ', '')
print(new_express)
res = remove_bracket(new_express)
print(res)

'''
正则
\([^()]\)

\d+\.?\d*[*/]-?\d+\.?\d*

-?\d+\.?\d*

'''
