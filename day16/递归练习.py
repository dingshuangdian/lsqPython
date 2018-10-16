# 递归练习

# 年龄练习

def age(n):
    if n == 4:
        return 20
    elif n > 0 and n < 4:
        return age(n + 1) + 2


print(age(1))

# 二分查找法

lis = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]


def find(l, aid, start=0, end=None):
    end = len(l) if end is None else end
    mid_index = (end - start) // 2 + start  # 计算中间值
    if start <= end and mid_index != len(l):
        if l[mid_index] > aid:
            return find(l, aid, start=start, end=mid_index - 1)
        elif l[mid_index] < aid:
            return find(l, aid, start=mid_index + 1, end=end)
        else:
            return mid_index, aid
    else:
        return '值不存在'


print(find(lis, 900))
