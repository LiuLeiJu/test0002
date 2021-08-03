#!/usr/bin/python3


def s():
    start=1
    print("        *")
    while(start<=7):
        print(" "*(7-start),"*"*start,end="")
        print("*"*start)
        start+=1



#正常9*9
def normal():
    i=1
    while(i<=9):
        j=1
        while(j<=i):
            print(i,"*",j,"=",(i*j),end="")
            print("\t",end="")
            j+=1
        print("\n")
        i+=1


#倒序9*9
def rmal():
    i=9
    while(i>=1):
        j=1
        while(j<=i):
            print(j,"*",i,"=",(i*j),end="")
            print("\t",end="")
            j+=1
        print("\n")
        i-=1


if __name__=='__main__':
    s()
