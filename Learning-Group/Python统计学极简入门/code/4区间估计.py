#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import scipy.stats
from scipy import stats as sts


def mean_interval(mean=None, sigma=None,std=None,n=None,confidence_coef=0.95):
    """
    mean:样本均值
    sigma: 总体标准差
    std: 样本标准差
    n:   样本量
    confidence_coefficient：置信系数
    confidence_level:置信水平 置信度
    alpha:显著性水平
    功能：构建总体均值的置信区间
    """
    alpha = 1 - confidence_coef
    z_score = scipy.stats.norm.isf(alpha / 2)            # z分布临界值
    t_score = scipy.stats.t.isf(alpha / 2, df = (n-1) )  # t分布临界值
   
    if n >= 30: 
        if sigma != None:
            me = z_score * sigma / np.sqrt(n)
            print("大样本，总体 sigma 已知：z_score:",z_score)
        elif sigma == None:
            me = z_score * std / np.sqrt(n)
            print("大样本，总体 sigma 未知 z_score",z_score)
        lower_limit = mean - me
        upper_limit = mean + me
    if n < 30 :
        if sigma != None:
            me = z_score * sigma / np.sqrt(n)
            print("小样本，总体 sigma 已知 z_score * sigma / np.sqrt(n) \nz_score = ",z_score)
        elif sigma == None:
            me = t_score * std / np.sqrt(n)
            print("小样本，总体 sigma 未知 t_score * std / np.sqrt(n) \nt_score = ",t_score)
        lower_limit = mean - me
        upper_limit = mean + me
    
    return (round(lower_limit, 1), round(upper_limit, 1))


# 网站流量UV区间估计:
# 
# 某网站近20天的流量uv数据如下，我们研究一下该网站的总体流量uv均值：

# In[9]:


import numpy as np
data = np.array([52,44,55,44,45,59,50,54,62,46,54,42,60,62,43,42,48,55,57,56])


# 均值为

# In[10]:


x_bar = data.mean()
x_bar


# 样本标准差为：

# In[11]:


x_std = sts.tstd(data,ddof = 1) #  ddof=1时,分母为n-1;ddof=0时,分母为n
x_std


# In[12]:


mean_interval(mean=x_bar, sigma=None,std= x_std,  n=len(data), confidence_coef=0.95)


# 于是我们有95%的把握，该网站的流量uv介于 `[48, 55]`之间

# In[13]:


def proportion_interval(p=None, n=None, confidence_coef =0.95):
    """
    p: 样本比例
    n: 样本量
    confidence_coef: 置信系数
    功能：构建总体比例的置信区间
    """
    alpha = 1 - confidence_coef
    z_score = scipy.stats.norm.isf(alpha / 2)  # z分布临界值
    
    me = z_score * np.sqrt((p * (1 - p)) / n) 
    lower_limit = p - me
    upper_limit = p + me
    
    return (round(lower_limit, 4), round(upper_limit, 4))


# In[14]:


p = 396/500
n = 500
proportion_interval(p=p, n=n, confidence_coef =0.95)

