#!/usr/bin/python3

import random

# 界面
def interface():
    print("*"*30+"\n*中国工商银行账户管理系统V1.0*\n"+"*" * 30)
    option = ['开户', '存钱', '取钱', '转账', '查询', 'Bye!']
    for i in range(1, len(option)+1):
        print("*", i, ".", option[i - 1], "\t"*5, "*")


# 用户：帐号（str：系统随机产生的8位数字）,姓名(str),密码(int:6位数字),地址，存款余额（int），开户行（银行的名称（str））
# 地址：国家（str),省份(str)，街道(str),门牌号(str)
# 银行：能储存100用户的库（字典),本银行名称（比如：终归哦工商银行的昌平支行，str)
#银行名称(多银行使用，跨行使用)
brank_names=['中国农业银行']
#银行用户(多银行用户)
#branks={'1':[{"账号":"2222","姓名":"2222","密码":"2222","存款":0},{"账号":"3333","姓名":"2222","密码":"3333","存款":20}]}
branks={}
def produce_account():
    account = ''
    for i in range(0,9):
        account += str(random.randint(1,9))
    return account

def produce_address():
    country=input("请输入您的国家：")
    province=input("请输入您的省份：")
    street=input("请输入您的街道：")
    doorplate=input("请输入您的门牌号:")
    return country+province+street+doorplate


def brank(account,name,passwd,address,brank_name,money,card):
    if brank_name not in brank_names:
        brank_names.append(brank_name)
        branks[brank_name]=[{"账号":account,"姓名":name,"密码":passwd,"存款":money,"用户居住地址":address,"开户行":brank_name,"卡种类":card}]
        print("开户成功，账号为：", account)
        print("测试时使用：",branks)
        return 1
    else:
        for target in branks[brank_name]:
            if name == target["姓名"]:
                return 2
        if len(branks[brank_name]) >100:
            return 3
        branks[brank_name].append({"账号":account,"姓名":name,"密码":passwd,"存款":money,"用户居住地址":address,"开户行":brank_name,"卡种类":card})
        print("开户成功，账号为：",account)
        print(branks)
        return 1



# 开户(添加用户，传入参数：用户的所有信息。返回值：整型值（1：成功，2：用户已存在，3：用户库已满）)
def user_add():
    #账号
    account=produce_account()
    #姓名:
    name=input("请输入您的姓名：")
    #密码
    passwd=input("请输入您的密码：")
    #地址
    address=produce_address()
    #银行
    brank_name=input("请输入银行名称:")
    # 存款余额
    try:
        money = int(input("请输入您的存款余额:"))
    except ValueError:
        print("开户失败")
        return 4
    if brank_name == "中国工商银行":
        brank(account,name,passwd,address,brank_name,money,0)
    elif brank_name == "中国农业银行":
        card = input("请输入卡的种类(1:金卡,0:普通卡)")
        brank(account, name, passwd, address, brank_name, money,card)



def ABC(user_out,money):
    if user_out["卡种类"] == "0" and money>20000 and user_out['开户行'] == "中国农业银行":
        print("普通卡权限不足")
        return 0
    elif user_out["卡种类"] == "1" and money >50000 and user_out['开户行'] == "中国农业银行":
        print("金卡权限不足")
        return 0
    else:
        return 1




# 存钱（传入值：用户的帐号，存取的金额。返回值：布尔类型值）
def deposite():
    brank_name = input("请输入银行名称:")
    account=input("请输入要存钱的账号:")
    try:
        money=float(input("请输入要存的金钱数额:"))
    except ValueError or UnboundLocalError:
        print("输入有误")
    if brank_name not in brank_names or money <= 0:
        return False
    for i in range(0,len(branks[brank_name])):
        if account==branks[brank_name][i]['账号']:
            branks[brank_name][i]['存款']+=money
            return True
    else:
        return False


# 取钱（传入值：用户的帐号，用户的密码，取钱金额。返回值：整型值（0：正常，1：帐号不存在，2：密码不对，3：钱不够）
def withdraw():
    brank_name = input("请输入银行名称:")
    account = input("请输入要取钱的账号:")
    passwd=input("请输入您的密码：")
    try:
        money = float(input("请输入要取的金钱数额:"))
    except ValueError or UnboundLocalError:
        return
    if brank_name not in brank_names or money <= 0:
        return
    for i in range(0,len(branks[brank_name])):
        if account==branks[brank_name][i]['账号']:
            if passwd!=branks[brank_name][i]['密码']: #密码不正确
                return 2
            if branks[brank_name][i]['存款']>=money:
                if ABC(branks[brank_name][i],money) == 0:
                    return
                branks[brank_name][i]['存款']-=money
                print(branks[brank_name][i]['存款']) #取钱操作成功
                return 0
            else: #钱不够
                return 3
    else: #该银行没有该用户
        return 1


# 转账(传入值：转出的帐号，转入的账户，转出帐号的密码，转出的金额。返回值：0：正常，1：帐号不对，2：密码不对，3：钱不够）
def transfer_accounts():
    brank_out = input("请输入转出银行名称:")
    account_out = input("请输入要转出的账号:")
    brank_in = input("请输入转入银行名称:")
    account_in =input("请输入要转入的账号:")
    passwd_out = input("请输入要转出帐号的密码:")
    try:
        money = float(input("请输入要转出的金钱数额:"))
    except ValueError or UnboundLocalError:
        print("输入有误")
    if brank_out not in brank_names or money <= 0 or brank_in not in brank_names:
        print("输入信息有误")
        return
    for i in range(0,len(branks[brank_out])):
        if account_out==branks[brank_out][i]['账号']:
            if passwd_out!=branks[brank_out][i]['密码']:
                print("密码不对")
                return 2
            if branks[brank_out][i]['存款']>=money:
                if ABC(branks[brank_out][i],money) == 0:
                    return
                branks[brank_out][i]['存款']-=money
                for i in range(0, len(branks[brank_in])):
                    if account_in == branks[brank_in][i]['账号']:
                        branks[brank_in][i]['存款'] += money
                        commission_money = commission(branks[brank_out][i],branks[brank_in][i],money)
                        branks[brank_out][i]['存款'] -= commission_money
                        print("转账手续费事：",commission_money)
                        return 0
                else:
                    print("抱歉，没有该转入用户")
                    return 1
            else: #钱不够
                print("钱不够")
                return 3
    else:
        print("抱歉，没有该转出用户")
        return 1

#手续费（两个银行先用这个方式，多个银行之间用list更高效）
def commission(user_out,user_in,money):
    if user_out['开户行'] == user_in['开户行'] and user_out['开户行'] == "中国工商银行":
        if money <= 5000 or user_out['用户居住地址'][2:4] == user_in['用户居住地址'][2:4]:
            print(user_in['用户居住地址'][2:4])
            return 0
        elif money <= 10000:
            return 5
        elif money <= 50000:
            return 7.5
        else:
            if 0.015*money >=25:
                return 25
            return 0.015*money
    if user_out['开户行'] == user_in['开户行'] and user_out['开户行'] == "中国农业银行":
        if money <= 5000:
            return 0
        elif money <= 10000:
            return 5
        elif money <= 50000:
            return 7.5
        else:
            if 0.015 * money >= 25:
                return 25
            return 0.015 * money
    if user_out['开户行'] != user_in['开户行'] and user_out['开户行'] == "中国工商银行":
        if money <= 5000:
            return 0
        elif money <= 10000:
            return 5
        elif money <= 50000:
            return 7.5
        else:
            if 0.015 * money >= 25:
                return 25
            return 0.015 * money
    if user_out['开户行'] != user_in['开户行'] and user_out['开户行'] == "中国农业银行":
        if money <= 5000:
            return 0
        elif money <= 10000:
            return 5
        elif money <= 50000:
            return 7.5
        else:
            if 0.015 * money >= 25:
                return 25
            return 0.015 * money

#{'中国工商银行': [{'账号': '875849823', '姓名': '刘磊举', '密码': '123456', '存款': 50, '用户居住地址': '中国河北朝阳街3巷四号', '开户行': '中国工商银行'}], '中国农业银行': [{'账号': '954597285', '姓名': '刘磊举', '密码': '123456','存款': 50, '用户居住地址': '中国河北朝阳街3巷四号', '开户行': '中国农业银行'}]}




# 查询账户(传入值:帐号，帐号密码，返回值：空)
def select_accounts():
    brank_name = input("请输入银行名称:")
    account =input("请输入要查询的账号:")
    passwd=input("请输入您的密码:")
    if brank_name not in brank_names:
        return False
    for i in range(0,len(branks[brank_name])):
        if account==branks[brank_name][i]['账号']:
            if passwd!=branks[brank_name][i]['密码']:
                print("密码错误")
                break
            else:
                print(branks[brank_name][i])
                break
    else:
        print("抱歉，没有该用户")



def main():
    while True:
        interface()
        flag = input("请输入要办理业务的序号：")
        if flag == "1":
            print("\n欢迎开户")
            #1：成功，2：用户已存在，3：用户库已满）
            state1 = user_add()
            if state1 == 1:
                pass
            elif state1 == 2:
                print("用户已存在\n")
            elif state1 == 3:
                print("抱歉，该银行用户已满\n")
        elif flag == "2":
            print("\n欢迎存钱")
            state2 = deposite()
            if state2 is True:
                print("存钱操作成功\n")
            else:
                print("抱歉，存钱操作失败\n")
        elif flag == "3":
            print("\n欢迎取钱")
            state3 = withdraw()
            #0：正常，1：帐号不存在，2：密码不对，3：钱不够
            if state3 == 0:
                print("取钱操作成功\n")
            elif state3 == 1:
                print("抱歉，没有该用户\n")
            elif state3 == 2:
                print("密码不对\n")
            elif state3 == 3:
                print("钱不够\n")
            else:
                print("输入信息有误\n")
        elif flag == "4":
            print("\n欢迎转账")
            transfer_accounts()
        elif flag == "5":
            print("\n查询账户")
            select_accounts()
        elif flag == "6":
            print("\n用户退出系统")
            break
        else:
            print("\n抱歉，请您正确的输入业务序号")


if __name__ == '__main__':
    main()


