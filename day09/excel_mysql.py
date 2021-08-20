import xlrd
import pymysql

host="localhost"
user="root"
password="123456"

def update(sql,param,database):
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor()
    cursor.execute(sql,param)
    conn.commit()
    cursor.close()
    conn.close()

def select(sql,param,database,mode="many",size=1):
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute(sql, param)
    if mode == "all":
        date = cursor.fetchall()
    elif mode == "one":
        date = cursor.fetchone()
    elif mode == "many":
        date = cursor.fetchmany(size)
    else:
        date = 0
    conn.commit()
    cursor.close()
    conn.close()
    return date



def get_xlsx(path):
    wb = xlrd.open_workbook(filename=path,encoding_override=True)
    total_date = []
    for i in range(0,12):
        dates = []
        st = wb.sheet_by_index(i)
        for x in range(0,st.nrows):
            date = []
            for y in range(0,st.ncols):
                date.append(st.cell_value(x,y))
            dates.append(date)
        total_date.append(dates)
    return total_date

def save_sql(database,total_date):
    for j in range(len(total_date)):
        dates = total_date[j]
        j+=1
        sql = 'CREATE TABLE month%s(clothes_date VARCHAR(10) NULL,clothes_name VARCHAR(20) NULL,clothes_price VARCHAR(10) NULL,clothes_quantity VARCHAR(10) NULL,clothes_sales VARCHAR(10) NULL);'
        param=[j]
        update(sql,param,database)
        for i in range(1,len(dates)):
            sql = 'INSERT INTO month%s VALUES(%s,%s,%s,%s,%s)'
            param = [j,dates[i][0],dates[i][1],dates[i][2],dates[i][3],dates[i][4]]
            update(sql,param,database)


def get_sql(database):
    dates = []
    for i in range(1,13):
        sql = 'select * from month%s'
        param=[i]
        date = select(sql,param,database,mode="all")
        dates.append(date)
    print(dates)



total_date = get_xlsx(r"C:\Users\Administrator\Desktop\2020.xlsx")
save_sql("excel",total_date)

#get_sql("excel")
