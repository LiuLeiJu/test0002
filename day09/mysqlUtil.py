import pymysql



host="localhost"
user="root"
password="123456"
database="bank"

def update(sql,param):
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor()
    cursor.execute(sql,param)
    conn.commit()
    cursor.close()
    conn.close()


def select(sql,param,mode="many",size=1):
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