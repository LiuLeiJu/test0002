#!/usr/bin/python3

import numpy as np
import pandas as pd

def num10():
    start=1
    date=[]
    while start <=10:
        print("请输入第",start,"个数字")
        score = int(input())
        date.append(score)
        start+=1

    date = np.array(date)
    print("您输入的最大值为",date.max())
    print("您输入的和为",date.sum())
    print("您输入的平均值为",date.mean())



def num3():
    start=1
    date=[]
    while start<=3:
        print("请您输入三角形的第",start,"条边")
        side = int(input())
        if(side>0):
            date.append(side)
            start+=1

    date.sort()
    if(date[0]+date[1]>date[2] and date[0]-date[1]<date[2]):
        if(date[0]==date[1] or date[0]==date[2] or date[1]==date[2]):
            print("等腰三角形")
        elif(date[0]==date[1]==date[2]):
            print("等边三角形")
        elif(date[0]**2+date[1]**2==date[2]**2):
            print("直角三角形")
        else:
            print("普通三角形")
    else:
        print("对不起，不能构成三角形")


def num2():
    A=65
    B=78

    A=A+B
    B=A-B
    A=A-B
    print(A,B)


def locking():
    start=1
    while(start<=3):
        name=input("请输入你的用户名：")
        passwd=input("请输入你的密码：")
        if(name=="root" and passwd=="admin"):
            print("欢迎用户",name,"登录")
            break
        else:
            start+=1
    else:
        print("登录锁定")


def sum100():
    start=1
    sum0=0
    while(start<=100):
        sum0+=start
        start+=1
    print(sum0)


def crawl():
    start=0
    day=0
    while(start<=20):
        start+=3
        if(start>20):
            print(day)
        else:
            day+=1
            start-=2



def num6():
    start=1
    date=[]
    while(start<=6):
        print("请输入您的第",start,"门成绩")
        score=int(input())
        date.append(score)
        start+=1

    date = np.array(date)
    print("您总成绩为",date.sum())
    print("您平均分为",date.mean())
    print("您最高分为",date.max())
    print("您最低分为",date.min())



if __name__=='__main__':
    num6()
