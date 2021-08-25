import random
from mysqlUtil import update
from mysqlUtil import select

class bank:
    __brank_names = []
    __branks = {}
    __brank_name = None

    def setBrank_name(self,brank_name):
        self.__brank_name = brank_name

    def produce_account(self):
        account = ''
        for i in range(0, 9):
            account += str(random.randint(1, 9))
        return account

    def interface(self):
        print("*" * 30 + "\n*中国银行账户管理系统V1.0*\n" + "*" * 30)
        option = ['开户', '存钱', '取钱', '转账', '查询', 'Bye!']
        for i in range(1, len(option) + 1):
            print("*", i, ".", option[i - 1], "\t" * 5, "*")

    def produce_address(self):
        country = input("请输入您的国家：")
        province = input("请输入您的省份：")
        street = input("请输入您的街道：")
        doorplate = input("请输入您的门牌号:")
        return country + province + street + doorplate

    # 开户(添加用户，传入参数：用户的所有信息。返回值：整型值（1：成功，2：用户已存在，3：用户库已满）)
    def user_add(self):
        # 账号
        account = self.produce_account()
        # 姓名:
        name = input("请输入您的姓名：")
        # 密码
        passwd = input("请输入您的密码：")
        # 地址
        address = self.produce_address()
        # 存款余额
        try:
            money = int(input("请输入您的存款余额:"))
        except ValueError:
            print("开户失败")
            return 4
        self.brank(account, name, passwd, address, self.__brank_name, money)
        '''
        if self.__brank_name == "icbc":
            self.brank(account, name, passwd, address, self.__brank_name, money)
        elif self.__brank_name == "abc":
            card = input("请输入卡的种类(1:金卡,0:普通卡)")
            self.brank(account, name, passwd, address, self.__brank_name, money, card)
         '''
    def brank(self,account, name, passwd, address, brank_name, money, card=0):
        if brank_name  in self.__brank_names:
            self.__brank_names.append(brank_name)
            self.__branks[brank_name] = [
                {"账号": account, "姓名": name, "密码": passwd, "存款": money, "用户居住地址": address, "开户行": brank_name,
                 "卡种类": card}]
            self.insert_user(account, name, passwd, money, address, brank_name, card)
            print("开户成功，账号为：", account)
            print("测试时使用：", self.__branks)
            return 1
        else:
            for target in self.__branks[brank_name]:
                if name == target["姓名"]:
                    return 2
            if len(self.__branks[brank_name]) > 100:
                return 3
            self.__branks[brank_name].append(
                {"账号": account, "姓名": name, "密码": passwd, "存款": money, "用户居住地址": address, "开户行": brank_name,
                 "卡种类": card})
            self.insert_user(account, name, passwd, money, address, brank_name, card)
            print("开户成功，账号为：", account)
            print(self.__branks)
            return 1

    # 存钱（传入值：用户的帐号，存取的金额。返回值：布尔类型值）
    def deposite(self):
        account = input("请输入要存钱的账号:")
        #self.__user_bank(brank_name, account)
        try:
            money = float(input("请输入要存的金钱数额:"))
        except ValueError or UnboundLocalError:
            print("输入有误")
        if self.__brank_name not in self.__brank_names or money <= 0:
            return False
        for i in range(0, len(self.__branks[self.__brank_name])):
            if account == self.__branks[self.__brank_name][i]['账号']:
                self.__branks[self.__brank_name][i]['存款'] += money
                self.update_user(money, account)
                return True
        else:
            return False

    # 查询账户(传入值:帐号，帐号密码，返回值：空)
    def select_accounts(self):
        account = input("请输入要查询的账号:")
        passwd = input("请输入您的密码:")
        if self.__brank_name not in self.__brank_names:
            return False
        for i in range(0, len(self.__branks[self.__brank_name])):
            if account == self.__branks[self.__brank_name][i]['账号']:
                if passwd != self.__branks[self.__brank_name][i]['密码']:
                    print("密码错误")
                    break
                else:
                    print(self.__branks[self.__brank_name][i])
                    break
        else:
            print("抱歉，没有该用户")

    # 取钱（传入值：用户的帐号，用户的密码，取钱金额。返回值：整型值（0：正常，1：帐号不存在，2：密码不对，3：钱不够）
    def withdraw(self):
        account = input("请输入要取钱的账号:")
        passwd = input("请输入您的密码：")
        #user_bank(brank_name, account)
        try:
            money = float(input("请输入要取的金钱数额:"))
        except ValueError or UnboundLocalError:
            print(2)
            return
        if self.__brank_name not in self.__brank_names or money <= 0:
            print(1)
            return
        for i in range(0, len(self.__branks[self.__brank_name])):
            if account == self.__branks[self.__brank_name][i]['账号']:
                if passwd != self.__branks[self.__brank_name][i]['密码']:  # 密码不正确
                    return 2
                if self.__branks[self.__brank_name][i]['存款'] >= money:
                    self.__branks[self.__brank_name][i]['存款'] -= money
                    self.update_user( -money, account)
                    print(self.__branks[self.__brank_name][i]['存款'])  # 取钱操作成功
                    return 0
                else:  # 钱不够
                    return 3
        else:  # 该银行没有该用户
            return 1

    def transfer_accounts(self):
        account_out = input("请输入要转出的账号:")
        brank_in = input("请输入转入银行名称:")
        account_in = input("请输入要转入的账号:")
        b.user_bank(account_in,brank_in)
        passwd_out = input("请输入要转出帐号的密码:")
        self.user_bank( account_in,brank_in)
        try:
            money = float(input("请输入要转出的金钱数额:"))
        except ValueError or UnboundLocalError:
            print("输入有误")
        if self.__brank_name not in self.__brank_names or money <= 0 or brank_in not in self.__brank_names:
            print("输入信息有误")
            return
        for i in range(0, len(self.__branks[self.__brank_name])):
            if account_out == self.__branks[self.__brank_name][i]['账号']:
                if passwd_out != self.__branks[self.__brank_name][i]['密码']:
                    print("密码不对")
                    return 2
                if self.__branks[self.__brank_name][i]['存款'] >= money:
                    self.__branks[self.__brank_name][i]['存款'] -= money
                    self.update_user(-money, account_out)
                    for i in range(0, len(self.__branks[brank_in])):
                        if account_in == self.__branks[brank_in][i]['账号']:
                            self.__branks[brank_in][i]['存款'] += money
                            self.update_user( money, account_in, bank=brank_in)
                            #commission_money = self.__commission(self.__branks[brank_out][i], self.__branks[brank_in][i], money)
                            #self.__branks[brank_out][i]['存款'] -= commission_money
                            #print("转账手续费是：", commission_money)
                            return 0
                    else:
                        print("抱歉，没有该转入用户")
                        return 1
                else:  # 钱不够
                    print("钱不够")
                    return 3
        else:
            print("抱歉，没有该转出用户")
            return 1

    def user_bank(self, uid,bank="icbc"):
        try:
            date = self.select_user(uid,bank)
            if bank not in self.__brank_names:
                self.__brank_names.append(bank)
                self.__branks[bank] = [{"账号": date[0], "姓名": date[1], "密码": date[2], "存款": float(date[3]), "用户居住地址": date[4],
                                 "开户行": date[5], "卡种类": date[6]}]
            else:
                self.__branks[bank].append(
                    {"账号": date[0], "姓名": date[1], "密码": date[2], "存款": float(date[3]), "用户居住地址": date[4],
                     "开户行": date[5], "卡种类": date[6]})
        except TypeError:
            print("sql语句错误")


    # 添加
    def insert_user(self, account, name, passwd, money, address, brank_name, card,bank="icbc"):
        money = float(money)
        sql = "INSERT INTO %s VALUES(%s,'%s','%s','%s','%s','%s','%s')"%(bank,account,name, passwd, money, address, brank_name, card)
        param = []
        update(sql, param)

    # 修改
    def update_user(self, money, uid,bank="icbc"):
        sql = "UPDATE %s SET money = money + %s WHERE uid=%s"%(bank,money, uid)
        param = []
        update(sql, param)

    # 查询abc
    def select_user(self,uid,bank):
        try:
            sql = "select * FROM %s where uid = %s"%(bank,uid)
            param = []
            return select(sql, param, mode="one")
        except UnboundLocalError:
            print("sql语句错误")

    def main(self):
        account = input("账户")
        self.user_bank(account)
        while True:
            self.interface()
            flag = input("请输入要办理业务的序号：")
            if flag == "1":
                print("\n欢迎开户")
                # 1：成功，2：用户已存在，3：用户库已满）
                state1 = self.user_add()
                if state1 == 1:
                    pass
                elif state1 == 2:
                    print("用户已存在\n")
                elif state1 == 3:
                    print("抱歉，该银行用户已满\n")
            elif flag == "2":
                print("\n欢迎存钱")
                state2 = self.deposite()
                if state2 is True:
                    print("存钱操作成功\n")
                else:
                    print("抱歉，存钱操作失败\n")
            elif flag == "3":
                print("\n欢迎取钱")
                state3 = self.withdraw()
                # 0：正常，1：帐号不存在，2：密码不对，3：钱不够
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
                self.transfer_accounts()
            elif flag == "5":
                print("\n查询账户")
                self.select_accounts()
            elif flag == "6":
                print("\n用户退出系统")
                break
            else:
                print("\n抱歉，请您正确的输入业务序号")



b = bank()
b.setBrank_name("icbc")
b.main()