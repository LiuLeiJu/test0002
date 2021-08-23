

class student:
    __s_id = ""
    __name = ""
    __age = ""
    __height = 0
    __weight = 0
    __score = 0
    __address = ""
    __phone = ""

    def setStudent(self,s_id,name,age,height,weight,score,address,phone):
        self.setS_id(s_id)
        self.setName(name)
        self.setAge(age)
        self.setHeight(height)
        self.setWeight(weight)
        self.setScore(score)
        self.setAddress(address)
        self.setPhone(phone)

    def setS_id(self,s_id):
        self.__s_id = s_id

    def setName(self,name):
        self.__name = name

    def setAge(self,age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print("年龄设置错误")

    def setHeight(self,height):
        if height > 0:
            self.__height = height
        else:
            print("身高设置有误")

    def setWeight(self,weight):
        if weight > 0:
            self.__weight = weight
        else:
            print("体重设置有误")

    def setScore(self,score):
        if score > 0 and score <= 120:
            self.score = score
        else:
            print("分数设置有误")

    def setAddress(self,address):
        self.__address = address

    def setPhone(self,phone):
        self.__phone = phone

    def learn(self,learn_time):
        print(learn_time)

    def playGame(self,game):
        print(game)

    def biancheng(self,num):
        print(num)

    def qiuhe(self,*num):
        s = 0
        for i in num:
           s += i
        print(s)


class car:
    __car_category = ""
    __car_num = 0
    __car_color = ""
    __roil = 0

    def setCar(self,car_category,car_num,car_color,roil):
        self.setCar_category(car_category)
        self.setCar_num(car_num)
        self.setCar_color(car_color)
        self.setRoil(roil)

    def setCar_category(self,car_category):
        self.__car_category = car_category

    def setCar_num(self,car_num):
        if car_num > 0:
            self.__car_num = car_num
        else:
            print("车轮数设置有误")

    def setCar_color(self,car_color):
        self.__car_color = car_color

    def setRoil(self,roil):
        if roil > 0:
            self.__roil = roil
        else:
            print("油箱设置有误")

    def run(self,target):
        print(self.__car_category,self.__car_num,self.__car_color,self.__roil,target)




class monky:
    __sex = ""
    __color = ""
    __weight = 0

    def setMonky(self,sex,color,weight):
        self.setSex(sex)
        self.setColor(color)
        self.setWeight(weight)


    def setSex(self,sex):
        self.__sex = sex

    def setColor(self,color):
        self.__color = color

    def setWeight(self,weight):
        if weight > 0:
            self.__weight = weight
        else:
            print("体重设置有误")

    def fire(self,wupin):
        print("使用生火的材料是",wupin)

    def leran(self,*x):
        for i in x:
            print("学习事物",i)


'''
s1 = student()
s1.qiuhe(1,2,3)
'''
'''
f = car()
f.setCar("法拉利",4,"黑色",150)
f.run("赛车")
b = car()
b.setCar("宝马",4,"黑色",150)
b.run("赛车")
l = car()
l.setCar("铃木",4,"黑色",150)
l.run("赛车")
w = car()
w.setCar("五菱",4,"黑色",150)
w.run("赛车")
t = car()
t.setCar("拖拉机",4,"黑色",150)
t.run("赛车")
'''

m = monky()
m.leran("汽车","飞机")