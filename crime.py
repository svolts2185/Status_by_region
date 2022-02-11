import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


sum_crimes=[]      #범죄 누적합
crimes_num=[]  #지역별 범죄 건수

crime=pd.read_csv("C:/Data/경찰청_범죄 발생 지역별 통계.csv",engine='python')

crime=crime.drop([crime.columns[0],crime.columns[1]],axis=1)

for i in crime:
    sum_crimes.append(crime[i].cumsum())

region=["Seoul","Busan","Daegu","Incheon","Gwangju","Daejeon","Ulsan","Sejong"]

population=[10022181,3513777,2487829,2925815,1472199,1518775,1173534,210884]  #KOSIS참고

for i in sum_crimes:
    crimes_num.append(int(i[37]))

value=[]

for i,j in zip(crimes_num,population):
    value.append(i/j*100)

dic_crime={}

for i,j in zip(region,value):
    dic_crime[i]=j

dic_crime=sorted(dic_crime.items(),key=lambda x:x[1])

colors=['lightgrey','silver','darkgray','darkgrey','dimgray','dimgrey','black','black']

x=np.arange(8)
plt.bar(x,[j for i,j in dic_crime],width=0.6,color=colors)
plt.xticks(x,[i for i,j in dic_crime])
plt.show()