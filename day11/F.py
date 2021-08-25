


class oldPhone:
    __phone_name = ""

    def setPhone_name(self,phone_name):
        self.__phone_name = phone_name

    def getPhone_name(self):
        return self.__phone_name

    def call(self,who):
        print("正在给%s打电话..."%who)


class newPhone(oldPhone):
    def call(self,who):
        print("语音拨号中...")
        super().call(who)

    def show(self):
        print("品牌为：%s的手机很好用..."%super().getPhone_name())

'''
p = newPhone()
p.setPhone_name("华为")
p.show()
p.call("小明")
'''

class cook_person:
    __name = ""
    __age = 0

    def setCook(self,name,age):
        self.setName(name)
        self.setAge(age)

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print("年龄设置有误")

    def getAge(self):
        return self.__age

    def cook(self):
        print("我会煮饭")

class saute_person(cook_person):
    def saute(self):
        print("我会炒菜")


class restaurant_person(saute_person):
    def cook(self):
        print("煮饭")

    def saute(self):
        print("炒菜")

'''
r = restaurant_person()
r.setName("小明")
r.setAge(18)
r.cook()
r.saute()
'''

class person:
    __age = 0
    __sex = "男"
    __name = ""

    def setPerson(self,age,sex,name):
        self.setAge(age)
        self.setSex(sex)
        self.setName(name)

    def setAge(self,age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print("年龄设置有误")

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("性别设置有误")

    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name


class worker(person):
    def work(self):
        print(super().getName(),"干活")

class student(person):
    __s_id = ""

    def setStudent(self,age,sex,name,s_id):
        super().setPerson(age,sex,name)
        self.setS_id(s_id)

    def setS_id(self,s_id):
        self.__s_id = s_id

    def getS_id(self):
        return self.__s_id

    def learn(self):
        print(super().getName(),"学习")

    def sing(self):
        print(super().getName(),"唱歌")


s = student()
s.setStudent(18,"男","小明",123456)
s.learn()
s.sing()

w = worker()
w.setPerson(18,"男","小蓝")
w.work()