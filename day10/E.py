

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


'''
t = test()
t.test_AC()
'''
t = test()
t.test_ST()