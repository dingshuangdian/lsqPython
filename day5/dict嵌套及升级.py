# dict嵌套及升级

dic = {
    'name': ['lsq', 'dsd', 'bsg', 'nmc'],
    'py9': {'num': 71, 'avg_age': 18},
    'age': 21

}

dic['age'] = 56
dic['name'].append('lvp')
dic['py9']['female'] = 6

info = input('>>>>>>>>')
for i in info:
    if i.isalpha():
        info = info.replace(i, '')
l = info.split()
print(len(l))
