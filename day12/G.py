from threading import Thread
from time import sleep

bread_num = 0
sur = 0


class cook_person(Thread):
    name = ""
    __count = 0

    def run(self) -> None:
        global bread_num
        global sur
        while True:
            if bread_num < 500:
                bread_num += 1
                print(self.name,"生成1个面包","面包篮有",bread_num)
            if bread_num >= 500:
                sleep(2)
            if sur == 6:
                return


class customer(Thread):
    name = ""
    __count = 0

    __money = 3000
    def run(self) -> None:
        global bread_num
        global sur
        while True:
            if self.__money >= 3 and bread_num>=1:
                bread_num -= 1
                self.__money -= 3
                print(self.name,"购买1个面包","面包篮有",bread_num,"剩余金额为",self.__money)
            if  bread_num<=0:
                sleep(3)
            if self.__money < 3:
                sur += 1
                return 1

def test():
    c1=cook_person()
    c1.name = "厨师1"
    c2=cook_person()
    c2.name = "厨师2"
    c3=cook_person()
    c3.name = "厨师3"
    c1.start()
    c2.start()
    c3.start()


    p1=customer()
    p1.name = "顾客1"
    p2=customer()
    p2.name = "顾客2"
    p3=customer()
    p3.name = "顾客3"
    p4=customer()
    p4.name = "顾客4"
    p5=customer()
    p5.name = "顾客5"
    p6=customer()
    p6.name = "顾客6"
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()


test()






