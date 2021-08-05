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
brank_names=['1']
#银行用户(多银行用户)
branks={'1':[{"账号":"2222","姓名":"2222","密码":"2222","存款":0},{"账号":"3333","姓名":"2222","密码":"3333","存款":20}]}
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


def brank(account,name,passwd,brank_name):
    if brank_name not in brank_names:
        brank_names.append(brank_name)
        branks[brank_name]=[{"账号":account,"姓名":name,"密码":passwd,"存款":0}]
        print("开户成功，账号为：", account)
    else:
        if len(branks[brank_name]) >100:
            print("抱歉，该银行用户已满")
        branks[brank_name].append({"账号":account,"姓名":name,"密码":passwd,"存款":0})
        print("开户成功，账号为：",account)
    print(branks)



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
    print(address)
    #银行
    brank_name=input("请输入银行名称:")
    brank(account,name,passwd,brank_name)


# 存钱（传入值：用户的帐号，存取的金额。返回值：布尔类型值）
def deposite():
    account=input("请输入要存钱的账号:")
    money=float(input("请输入要存的金钱数额:"))
    for i in range(0,len(branks['1'])):
        if account==branks['1'][i]['账号']:
            branks['1'][i]['存款']+=money
            return True
    else:
        print("抱歉，没有该用户")
        return False


# 取钱（传入值：用户的帐号，用户的密码，取钱金额。返回值：整型值（0：正常，1：帐号不存在，2：密码不对，3：钱不够）
def withdraw():
    account = input("请输入要取钱的账号:")
    passwd=input("请输入您的密码：")
    money = float(input("请输入要取的金钱数额:"))
    for i in range(0,len(branks['1'])):
        if account==branks['1'][i]['账号']:
            if passwd!=branks['1'][i]['密码']:
                print("密码不对")
                return 2
            if branks['1'][i]['存款']>=money:
                branks['1'][i]['存款']-=money
                print(branks['1'][i]['存款'])
                return 0
            else: #钱不够
                print("钱不够")
                return 3
    else:
        print("抱歉，没有该用户")
        return 1


# 转账(传入值：转出的帐号，转入的账户，转出帐号的密码，转出的金额。返回值：0：正常，1：帐号不对，2：密码不对，3：钱不够）
def transfer_accounts():
    account_out = input("请输入要转出的账号:")
    account_in =input("请输入要转入的账号:")
    passwd_out = input("请输入要转出帐号的密码:")
    money = float(input("请输入要转出的金钱数额:"))
    for i in range(0,len(branks['1'])):
        if account_out==branks['1'][i]['账号']:
            if passwd_out!=branks['1'][i]['密码']:
                print("密码不对")
                return 2
            if branks['1'][i]['存款']>=money:
                branks['1'][i]['存款']-=money
                for i in range(0, len(branks['1'])):
                    if account_in == branks['1'][i]['账号']:
                        branks['1'][i]['存款'] += money
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


# 查询账户(传入值:帐号，帐号密码，返回值：空)
def select_accounts():
    account =input("请输入要查询的账号:")
    passwd=input("请输入您的密码:")
    for i in range(0,len(branks['1'])):
        if account==branks['1'][i]['账号']:
            if passwd!=branks['1'][i]['密码']:
                print("密码错误")
                break
            else:
                print(branks['1'][i])
                break
    else:
        print("抱歉，没有该用户")


def main():
    while True:
        interface()
        flag = input("请输入要办理业务的序号：")
        if flag == "1":
            print("欢迎开户")
            user_add()
        elif flag == "2":
            print("欢迎存钱")
            deposite()
        elif flag == "3":
            print("欢迎取钱")
            withdraw()
        elif flag == "4":
            print("欢迎转账")
            transfer_accounts()
        elif flag == "5":
            print("查询账户")
            select_accounts()
        elif flag == "6":
            print("用户退出系统")
            break
        else:
            print("抱歉，请您正确的输入业务序号")


if __name__ == '__main__':
    main()



