import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import statsmodels.stats.weightstats
s = pd.read_excel("C:\\Users\\14418\\Desktop\\293934587_按文本_大学生消费水平_55_55(1).xlsx")
data=s['您的每月消费水平?']
result=data
result_dic={}
for item_str in result:
    if item_str not in result_dic:
        result_dic[item_str]=1
    else:
        result_dic[item_str]+=1
keys=result_dic.values()
 
df = pd.DataFrame(keys, columns =['value'])

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
plt.hist(x = data,
         
         color = 'steelblue', 
         edgecolor = 'black' 
         )
plt.xlabel('消费水平')
plt.ylabel('频数')
plt.title('消费水平分布')

plt.show()

u = df['value'].mean()
# 计算标准差
std = df['value'].std()  # 计算标准差


print(scipy.stats.kstest(df['value'], 'norm', (u, std)))
print('pvalue大于0.05可以认为满足正态分布')