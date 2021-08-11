

def cacluate(*parameter):
    sum = 0
    result = []
    target = list(parameter)
    for i in target:
        sum += i
    avg = sum/len(target)
    for i in target:
        if i > avg:
            result.append(i)
    return (avg, result)


def select(target_list,index):
    if index >= len(target_list):
        return -1
    else:
        return target_list[index]


def recursion_print(num):
    if num <=150:
        print(num)
        num+=1
        recursion_print(num)


sum = 0
def recursion_sum(num):
    global sum
    if num >0:
        sum += num
        num -=1
        recursion_sum(num)

语文 = ['小明', '小张', '小黄', '小杨']
数学 = ['小黄', '小李', '小王', '小杨', '小周']
英语 = ['小杨', '小张', '小吴', '小冯', '小周']

def student_sum(*account):
    sum = 0
    for items in  account:
        for item in items:
            sum += 1
    return sum

def students_print(*account):
    for items in account:
        for item in items:
            print(item)


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




def main():
    print("接收任意多个数,返回的是一个元组.元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数：")
    print(cacluate(4,3,1,2))
    print("接收一个列表和一个索引，返回这个列表中对应索引的数据，如果索引超出范围，返回-1:")
    print(select([0,1,2,3],1))
    print("1~150之间的数的打印-方法的递归调用:")
    recursion_print(1)
    print("递归，求1~300所有数的和:")
    recursion_sum(300)
    print(sum)
    print("求选课学生总共有多少人:")
    print(student_sum(语文,数学,英语))
    print("求只选了第一个学科的人的数量和对应的名字:")
    print(student_sum(语文))
    students_print(语文)
    print("求只选了一门学科的学生的数量和对应的名字")
    account = input("请输入要查询的科目(语文，数学，英语)：")
    if account=='语文':
        print(student_sum(语文))
        students_print(语文)
    elif account == '数学':
        print(student_sum(语文))
        students_print(语文)
    elif account == '英语':
        print(student_sum(语文))
        students_print(语文)
    else:
        print("输入有误")
    rmal()


if __name__=="__main__":
    main()