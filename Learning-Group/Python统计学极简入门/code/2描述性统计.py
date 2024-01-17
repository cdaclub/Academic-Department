#!/usr/bin/env python
# coding: utf-8

# In[167]:


## 使用 numpy 库里的 mean 函数
import numpy as np
data =  [2,23,4,17,12,12,13,16]
print(np.mean(data))


# In[168]:


# 使用 scipy 库里的 gmean 函数求几何平均数
from scipy import stats as sts
data = [2,23,4,17,12,12,13,16]
print(sts.gmean(data))


# In[169]:


# 使用 scipy 库里的 hmean 函数求调和平均数
from scipy import stats as sts
data = [2,23,4,17,12,12,13,16]
print(sts.hmean(data))


# In[170]:


# 使用 numpy 库里的 median 函数求调和平均数
import numpy as np
data =  [2,23,4,17,12,12,13,16]
print(np.median(data))


# In[171]:


# 使用 scipy 库里的 mode 函数求众数
from scipy import stats as sts
data =  [2,23,4,17,12,12,13,16]
print(sts.mode(data))


# In[172]:


from scipy import stats as sts  
data =  [2,23,4,17,12,12,13,16]
print(sts.scoreatpercentile(data,25)) #25分位数
print(sts.scoreatpercentile(data,75)) #75分位数


# In[173]:


import seaborn as sns
data = [2,23,4,17,12,12,13,16]
# 使用sns.boxplot()函数绘制箱线图
sns.boxplot(data=data)


# In[174]:


# 极差
import numpy as np
data =  [2,23,4,17,12,12,13,16]
print(np.ptp(data))


# In[175]:


# 四分位距
from scipy import stats as sts
data =  [2,23,4,17,12,12,13,16]
print(sts.scoreatpercentile(data,75)-sts.scoreatpercentile(data,25))


# In[176]:


# 方差
from scipy import stats as sts
data =  [2,23,4,17,12,12,13,16]
print(sts.tvar(data,ddof = 1))# ddof=1时,分母为n-1 样本方差 s² ;ddof=0时,分母为n 总体方差 σ²


# In[177]:


# 手动计算样本标准差
np.sqrt(((data - np.array(data).mean())**2).sum()/(len(data)-1)) # 分母为n-1


# In[178]:


# 手动计算总体标准差 
np.sqrt(((data - np.array(data).mean())**2).sum()/len(data))# 分母为n


# In[179]:


# scipy计算标准差
from scipy import stats as sts
data = [2,23,4,17,12,12,13,16]
print(sts.tstd(data,ddof = 1))# ddof=1时,分母为n-1 样本标准差 s ;ddof=0时,分母为n 总体标准差 σ


# - `numpy.std() `
# 默认是除以 $n$ 的 即是有偏的; numpy.std(ddof=1) 加入参数可以计算无偏的
# - `pandas.std() `
# 默认是除以 $n-1$ 的 即是无偏的; pandas.std(ddof=0) 加上参数可以计算有偏的

# In[180]:


# Numpy计算标准差
print('有偏（n）',np.std(data) ,'无偏（n-1）',np.std(data,ddof = 1))


# In[181]:


import pandas as pd
# Pandas计算标准差
print('有偏（n）',pd.Series(data).std(ddof=0) ,'无偏（n-1）',pd.Series(data).std(ddof=1))


# In[ ]:





# In[ ]:





# In[182]:


# 变异系数： 
from scipy import stats as sts
data = [2,23,4,17,12,12,13,16]
print(sts.tstd(data)/sts.tmean(data))
# 0.5513549709509329


# In[183]:


# 偏度
from scipy import stats as sts
data = [2,23,4,17,12,12,13,16]
print(sts.skew(data,bias=False)) # bias=False 代表计算的是总体偏度，bias=True 代表计算的是样本偏度


# In[184]:


# 峰度
from scipy import stats as sts
data = [2,23,4,17,12,12,13,16]
print(sts.kurtosis(data,bias=False)) # bias=False 代表计算的是总体峰度，bias=True 代表计算的是样本峰度


# In[ ]:




