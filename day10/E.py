

class air_conditioner:
    __brand_name = ""
    __price = 0

    def setBrand_name(self,brand_name):
        self.__brand_name = brand_name

    def getBrand_name(self):
        return self.__brand_name

    def setPrice(self,price):
        if price > 0 :
            self.__price = price
        else:
            print("价格设置错误")

    def getPrice(self):
        return self.__price

    def setAir_conditioner(self,brand_name,price):
        self.setBrand_name(brand_name)
        self.setPrice(price)

    def start(self):
        print("空调开机了")

    def stop(self,duration):
        print("空调将在",duration,"分钟后自动关闭...")


class Student:
    __name = ""
    __age = 0

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        if age > 0 and age < 170:
            self.__age = age
        else:
            print("年龄设置有误")

    def getAge(self):
        return self.__age

    def setStudent(self,name,age):
        self.setName(name)
        self.setAge(age)

    def show(self):
        print("大家好，我叫",self.__name,"，今年",self.__age,"岁了！")

    def compare(self,student):

        if self.__age > student.getAge():
            print("我比同桌大",(self.__age-student.getAge()),"岁")
        elif self.__age < student.getAge():
            print("我比同桌大",(student.getAge()-self.__age),"岁")
        else:
            print("我比同桌一样大")



class person_phone:
    __name = "" #姓名
    __sex = ""  #性别
    __age = 0   #年龄
    __credit = 0    #手机剩余话费
    __poone_name = ""   #手机品牌
    __phone_battery = 0 #手机电池容量
    __phone_screen = 0  #手机屏幕大小
    __phone_standby = 0 #手机最大待机时长
    integrate = 0   #积分

    def setPerson_phone(self,name,sex,age,credit,poone_name,phone_battery,phone_screen,phone_standby,integrate):
        self.setName(name)
        self.setSex(sex)
        self.setAge(age)
        self.setPhone(credit,poone_name,phone_battery,phone_screen,phone_standby)
        self.setIntegrate(integrate)


    def setPhone(self,credit,poone_name,phone_battery,phone_screen,phone_standby):
        self.setCredit(credit)
        self.setPoone_name(poone_name)
        self.setPhone_battery(phone_battery)
        self.setPhone_screen(phone_screen)
        self.setPhone_standby(phone_standby)

    def setName(self,name):
        self.__name = name

    def setSex(self,sex):
        self.__sex = sex

    def setAge(self,age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print("年龄设置有误")

    def setCredit(self,credit):
        if credit > 0:
            self.__credit = credit
        else:
            print("手机剩余话费设置有误")

    def setPoone_name(self,poone_name):
        self.__poone_name = poone_name

    def setPhone_battery(self,phone_battery):
        if phone_battery > 0 :
            self.__phone_battery = phone_battery
        else:
            print("手机电池容量设置有误")

    def setPhone_screen(self,phone_screen):
        if phone_screen > 0:
            self._phone_screen = phone_screen
        else:
            print("手机屏幕大小设置有误")

    def setPhone_standby(self,phone_standby):
        if phone_standby > 0:
            self.__phone_standby = phone_standby
        else:
            print("手机最大待机时长设置有误")

    def setIntegrate(self,integrate):
        if integrate >= 0:
            self.__integrate = integrate
        else:
            print("积分设置有误")

    def call(self,phone_number,phone_time):
        if phone_number is None or self.__credit < 1:
            print("电话无法拨通")
        else:
            if  0 < phone_time and phone_time <= 10:
                self.__credit -=phone_time * 1
                self.__integrate += phone_time * 15
            elif 10 < phone_time and phone_time <= 20:
                self.__credit -= phone_time * 0.8
                self.__integrate += phone_time * 39
            elif phone_time > 20:
                self.__credit -= phone_time * 0.65
                self.__integrate += phone_time * 48
            else:
                print("输入的时间有误")

    def show(self):
        print(self.__name,self.__sex,self.__age,self.__credit,self.__poone_name,self.__phone_battery,self.__phone_screen,self.__phone_standby,self.__integrate)

class test:
    def test_AC(self):
        AC = air_conditioner()
        AC.setAir_conditioner("格力",30000)
        print(AC.getBrand_name())
        print(AC.getPrice())
        AC.start()
        AC.stop(5)

    def test_ST(self):
        st1=Student()
        st2=Student()
        st1.setStudent("小明",21)
        st2.setStudent("小蓝",20)
        st1.show()
        print(st1.getName())
        print(st1.getAge())
        st1.compare(st2)


    def test_pp(self):
        p1 = person_phone()
        p1.setPerson_phone("小明","男",18,50,"华为",20000,9.8,15,2)
        p1.show()
        p1.call("182313131",3)
        p1.show()


t = test()


#t.test_AC()

#t.test_ST()

t.test_pp()