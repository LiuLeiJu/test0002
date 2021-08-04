#!/usr/bin/python3

import random


def login():
    print("欢迎登录幸运数字系统")
    while True:
        count=1
        name=input("请输入您的帐号:")
        passwd=input("请输入您的密码：")
        if(name=="root" and passwd=="admin"):
            count=game(count)
            state=0
            if(count<=10):
                print("您好，是否开启第新一轮游戏(是：1,不是：2)：")
            else:
                break
            state=input()
            if(state=="1"):
                game(count)
            else:
                print("Game Over")
            break
        else:
            print("帐号或密码错误","\n")




def game(count):
    num=random.randint(0,10000)
    print(num)
    while True:
        choose=int(input("请输入您要猜的数字："))
        if(choose>num):
            print("对不起，您输入的数字大了")
        elif(choose<num):
            print("对不起，您输入的数字小了")
        else:
            print("恭喜您，猜对了幸运数字",num,"获得奖金10000金币")
            count+=1
            break
        count+=1
        if(count>10):
            print("5000金币没了，游戏结束")
            return 11
    return count

if __name__=='__main__':
    login()
