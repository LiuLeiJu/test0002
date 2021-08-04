#!/usr/bin/python3

import random


def login():
    print("欢迎登录幸运数字系统")
    while True:
        name=input("请输入您的帐号:")
        passwd=input("请输入您的密码：")
        if(name=="root" and passwd=="admin"):
            count=game()
            state=0
            if(count<=10):
                print("您好，是否开启第新一轮游戏(是：1,不是：2)：")
            else:
                break
            state=input()
            if(state=="1"):
                game()
            else:
                print("Game Over")
            break
        else:
            print("帐号或密码错误","\n")




def game():
    count=1
    num=random.randint(0,10000)
    print(num)
    while True:
        choose=int(input("请输入您要猜的数字："))
        if(choose>num):
            print("对不起，您输入的数字大了")
            count+=1
        elif(choose<num):
            print("对不起，您输入的数字小了")
            count+=1
        else:
            print("恭喜您，猜对了幸运数字",num,"获得奖金10000金币")
            break
        if(count>10):
            print("系统锁定，游戏结束")
            return 11
    return count

if __name__=='__main__':
    login()
