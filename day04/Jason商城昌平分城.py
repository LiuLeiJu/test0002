'''
    任务：
        优化购物小条
        10机械革命优惠券，0.5     2   0 3
        20张卫龙辣条优惠券 0.3   4    1 4 6  8 9
        15张HUA WEI WATCH 0.8   3    2 5 7
        随机抽取一张优惠券。


    商城：
        1.准备一些商品
        2.有空的购物车
        3.钱包
        4.结算
    流程：
        看你输入的产品存不存在，
            若存在
                若钱够了：
                    将商品添加到购物车
                    钱包余额减去商品的钱
                若钱不够
                    温馨：
            若不存在
                温馨提示：
            非法输入：
        退出：
            打印购物小条
'''

import random

shop = [
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["洗衣机",3000],
    ["机械革命",5000],
    ["卫龙辣条",4.5],
    ["老干妈辣酱",20],
]

# 1.准备好钱包

money = input("亲输入您的初始余额：")
money = int(money)


print("欢迎进入jason商城,输入q或者Q退出该商城")
index = random.randint(0,9)
if index == 0 or index == 3:
    print("恭喜你，获得了一张机械革命优惠券 0.5")
    index = 4
elif index in[1,4,6,8,9]:
    print("恭喜你，获得了一张卫龙辣条优惠券 0.3")
    index = 5
elif index in [2,5,7]:
    print("恭喜你，获得了一张HUA WEI WATCH 0.8折")
    index = 1


# 2. 准备一个空的购物车
mycart = []



# 3.开始购物

i  = 0
while i < 20:
    for key,value in enumerate(shop):
        print(key,value)
    # 请输入您要卖的商品
    chose = input("请输入您要买的商品:")

    if chose.isdigit():
        chose = int(chose) # "1" --> 1
        if chose > len(shop)-1 or chose < 0: # 9 > 7
            print("该商品不存在！别瞎弄！")
        else:
            if money > shop[chose][1]:
                if chose == index and index == 4:
                    index = 9
                    print("使用机械革命优惠券 0.5")
                    money = money - shop[chose][1]*(1-0.5)
                elif chose == index and index == 5:
                    index = 9
                    print("使用卫龙辣条优惠券 0.3")
                    money = money - shop[chose][1] * (1 - 0.3)
                elif chose == index and index == 1:
                    index = 9
                    print("使用HUA WEI WATCH 0.8折")
                    money = money - shop[chose][1]*(1-0.8)
                else:
                    money = money - shop[chose][1]
                mycart.append(shop[chose])
                print("恭喜，商品添加成功！您的余额为：￥",money,"\n")

            else:
                print("温馨提示：您的银行卡余额不足，穷鬼！请买其他商品！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")

    i = i + 1

# 4. 打印结算购物小条
print("以下是您的购物小条，请拿好！！！！么么哒！\n")
print("".center(30,"-"))
pay=0
amount=1
for key,value in enumerate(mycart):
    print(key+1,value)
    amount+=1
    pay+=value[1]
if amount !=0:
    print("数量：",amount-1,"\t总金额：",pay,"\t销售员:小明")
print("".center(30,"-"))










