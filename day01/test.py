#!/usr/bin/python3
import numpy as np
import pandas as pd
df=pd.read_excel('./12月份衣服销售数据.xlsx')
jia=df['价格/件']
sun=df['库存数量']
x=df['销售量/每日']

sum1=0
share=['羽绒服','牛仔裤','风衣','T血','皮草','衬衫']

def s(groups1):
    if(groups1['库存数量'].iloc[0]<groups1['销售量/每日'].sum()):
        return groups1['库存量']*groups1['价格/件'].iloc[0]
    else:
        return groups1['销售量/每日'].sum()*groups1['价格/件'].iloc[0]
        
    

for i in share:
    group=df.groupby('服装名称').get_group(i)
    sum1+=s(group)

    
print('总计：',sum1)
for i in share:
    group=df.groupby('服装名称').get_group(i)
    sum0=s(group)
    print(i,"%.2f"%(sum0/sum1*100)+'%')
