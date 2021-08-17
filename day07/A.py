
import xlrd

wb = xlrd.open_workbook(filename=r".\2020年每个月的销售情况.xlsx",encoding_override=True)

date_month=[]
for i in range(0,12):
    st = wb.sheet_by_index(i)
    date = {}
    for x in range(1,st.nrows):
        if st.cell_value(x,1) not in date:
            date[st.cell_value(x, 1)] = []
            de = []
            for y in range(2,st.ncols):
                de.append(st.cell_value(x,y))
            date[st.cell_value(x, 1)] = [de]
        else:
            de = []
            for y in range(2,st.ncols):
                de.append(st.cell_value(x,y))
            date[st.cell_value(x, 1)].append(de)

    for x in date:
        sold_sum = 0
        for y in date[x]:
            sold_sum += y[2]
        if sold_sum <= date[x][0][1]:
            pass
        else:
            sold_sum = date[x][0][1]
        date[x] = [date[x][0][0],date[x][0][1],sold_sum]
    date_month.append(date)



#销售总额
def gross_sales(date_month):
    sum_slaes = 0
    for i in date_month:
        for y in i:
            sum_slaes += (i[y][0]*i[y][2])
    return format(sum_slaes,'.2f')

#每件衣服的销售占比（件数）
def any_proportion(date_month):
    sum_total = 0
    sum_category = {}
    for i in date_month:
        for y in i:
            sum_total += i[y][2]
            if y not in sum_category:
                sum_category[y] = [i[y][2]]
            else:
                sum_category[y].append(i[y][2])
    for i in sum_category:
        s = sum(sum_category[i])
        sum_category[i] = format((s/sum_total*100),'.2f')
    return sum_category



#每件衣服的销售额占比
def any_sales_proportion(date_month):
    sum_total = gross_sales(date_month)
    sum_category = {}
    sum_total = 0
    sum_category = {}
    for i in date_month:
        for y in i:
            sum_total += i[y][2]
            if y not in sum_category:
                sum_category[y] = [i[y][0]]
                sum_category[y].append(i[y][2])
            else:
                sum_category[y].append(i[y][2])
    for i in sum_category:
        s = sum(sum_category[i])-sum_category[i][0]
        sum_category[i] = format((s*sum_category[i][0]/sum_total),'.2f')
    return sum_category


#最畅销的衣服
def sale_well(date_month):
    date = any_proportion(date_month)
    s = 0
    for i in date:
        if float(date[i]) > s:
            s = float(date[i])
    for i in date:
        if float(date[i]) == s:
            s = i
    return s

#每个季度最畅销的衣服
def quarter_sale_well(date_month):
    date_1 = []
    date_2 = []
    date_3 = []
    date_4 = []
    for i in range(12):
        if i in [1,2,3]:
            date_1.append(date_month[i])
        if i in [4,5,6]:
            date_2.append(date_month[i])
        if i in [7,8,9]:
            date_3.append(date_month[i])
        if i in [10,11,0]:
            date_4.append(date_month[i])
    print("第一季度：",sale_well(date_1))
    print("第二季度：",sale_well(date_2))
    print("第三季度：",sale_well(date_3))
    print("第四季度：",sale_well(date_4))


#全年销售量最低的衣服
def sales_few(date_month):
    date = any_proportion(date_month)
    s = 100
    for i in date:
        if float(date[i]) < s:
            s = float(date[i])
    for i in date:
        if float(date[i]) == s:
            s = i
    return s


#每件衣服的月销售额占比
def month_proportion(date_month):
    sum_month = []
    sum_category = {}
    m = 1
    for i in date_month:
        print("第",m,"月:")
        sum_total = 0
        for y in i:
            sum_total+= (i[y][0] * i[y][2])
        sum_month.append(sum_total)
        for y in i:
            price = i[y][0]*i[y][2]
            proportion = format(price/sum_total*100,'.2f')
            print(y,"的月销售额为：",proportion)
        m +=1


print("销售总额:\n",gross_sales(date_month))
print()
print("每件衣服的销售占比(件数):\n",any_proportion(date_month))
print()
#每件衣服的月销售额占比
month_proportion(date_month)
print()
print("每件衣服的销售额占比:\n",any_sales_proportion(date_month))
print()
print("全年最受欢迎的衣服是:\n",sale_well(date_month))
print()
quarter_sale_well(date_month)
print()
print("全年销售量最低的衣服:\n",sales_few(date_month))
