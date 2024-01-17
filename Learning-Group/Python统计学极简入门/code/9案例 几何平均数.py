#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy import stats as sts

# 假设有一个基金的年回报率
annual_returns = [-22.1, 28.7, 10.9, 4.9,15.8,5.5,-37,26.5,15.1,2.1]

# 计算增长因子：1+回报率/100
growth_factors = 1 + np.array(annual_returns)/100

# 计算增长因子的几何平均数
geo_mean = sts.gmean(growth_factors) 

# 打印结果
print("年平均增长率为:", (geo_mean-1)*100)


# In[2]:


geo_mean


# In[3]:


100*((geo_mean)**10)


# 因此，第1年年初投资额为100，第 10 年年末价值将为133.4492688303314

# 如果在计算增长因子的平均数的时候没有用几何平均数而是用算术平均数：

# In[5]:


ari_mean  = np.sum(np.array(growth_factors))/10
ari_mean  


# In[6]:


100*((ari_mean)**10)


# 如果平均增长因子确实为1.0504的话，第1年年初在该基金投资100 美元，第10年年末将增加到100x1.0504=163.451美元。但是，利用表3-2 中的年回报率，我们看到最初的100美元投资额第10 年年末的价值为 133.45 美元。这个基金经理的平均年回报率为5.04%的声明极度夸大了该基金的实际增长率。

# 这个问题是样本平均数只适合于加法过程。对于乘法过程，诸如增长率的应用，几何平均数是合适的位置度量。
# 
# 在财务、投资和银行业的问题中，几何平均数的应用尤为常见，当你任何时候想确定过去几个连续时期的平均变化率时，都能应用几何平均数。其他通常的应用包括物种总体、农作物产量、污染水平以及出生率和死亡率的变化。
# 
# 注意，几何平均数也可以用于发生在所有时间长度的连续时期的任何数量的变化率。除了年变化率外，几何平均数也常常用于发现季度、月、周以及天的平均变化率。

# In[7]:


from  scipy.stats import chi2_contingency
import numpy as np
data = np.array([[15,10], [10,26]])
chi2, p, dof, expected  = chi2_contingency(data,correction =False)
print(f'卡方值={chi2}, p值={p}, 自由度={dof}')


# In[ ]:




