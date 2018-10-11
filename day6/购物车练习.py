'''
买家 卖家 商品 金钱
'''

li = [
    {'name': '苹果', 'price': 10},
    {'name': '香蕉', 'price': 20},
    {'name': '西瓜', 'price': 30},

]

# 把货物放在货架上
shopping_car = {}
print('欢迎光临兰桂坊水果店')
money = input('让我看看你的钱')
if money.isdigit() and int(money) > 0:
    for i, k in enumerate(li):
        print('序号{},商品{},价格{}'.format(i, k['name'], k['price']))
    choose = input('请输入您要购买的商品序号')
    if choose.isdigit() and int(choose) < len(li):
        num = input('输入您要购买的商品数量:')
        if num.isdigit():
            if int(money) >= li[int(choose)]['price'] * int(num):
                money = int(money) - li[int(choose)]['price'] * int(num)
                if li[int(choose)]['name'] in shopping_car:
                    shopping_car[li[int(choose)]['name']] = shopping_car[li[int(choose)]['name']] + int(num)
                else:
                    shopping_car[li[int(choose)]['name']] = int(num)
                print('购物车中的商品有{},您的余额为{}'.format(shopping_car, money))

            else:
                print('余额不足！')

    else:
        print('都说了是序号，你傻啊！')
