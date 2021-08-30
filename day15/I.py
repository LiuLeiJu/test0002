

def getDate():
    file = open(file=r"C:\Users\Administrator\Desktop\baidu_x_system.log",mode="r+",encoding="utf-8")
    dates = file.readlines()
    date = []
    for i in dates:
        date.append(i.split(" ")[0])
    file.close()
    return date


def getMaxCount(date):
    set1 = set(date)
    target = list(set1)
    s = 0
    ip = ""
    for i in target:
        if date.count(i) > s:
            s = date.count(i)
            ip = i
    print(ip, "出现了最多", s, "次")

date = getDate()
getMaxCount(date)






