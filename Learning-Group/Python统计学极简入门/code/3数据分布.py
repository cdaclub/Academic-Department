#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import seaborn as sns

# 正态分布
mean = 3  # 均值
std = 4  # 标准差
size = 1000  # 生成1000个随机数

data = np.random.normal(mean, std, size=size)
sns.histplot(data, kde=True)


# In[2]:


import numpy as np
import seaborn as sns

# 标准正态分布
size = 1000  # 生成1000个随机数

data = np.random.standard_normal(size=size)
sns.histplot(data, kde=True)


# In[3]:


import numpy as np
import seaborn as sns

# t分布
df = 10  # 自由度
size = 1000  # 生成1000个随机数

data = np.random.standard_t(df, size=size)
sns.histplot(data, kde=True)


# In[4]:


import numpy as np
import seaborn as sns

#f分布

dfn = 5  # 分子自由度
dfd = 10  # 分母自由度
size = 1000  # 生成1000个随机数

data = np.random.f(dfn, dfd, size=size)
sns.histplot(data, kde=True)


# In[5]:


import numpy as np
import seaborn as sns

# 卡方分布
df = 5  # 自由度
size = 1000  # 生成1000个随机数

data = np.random.chisquare(df, size)
sns.histplot(data, kde=True)


# 补充：

# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2, t, f

# 生成正态分布的数据
mu = 0  # 均值
std1 = 1  # 标准差1
std2 = 3  # 标准差2
std3 = 10  # 标准差3

# 生成数据
data1 = np.random.normal(mu, 1, 1000)
data2 = np.random.normal(mu, 2, 1000)
data3 = np.random.normal(mu, 10, 1000)

# 绘制正态分布曲线
sns.kdeplot(data1, label='std=1')
sns.kdeplot(data2, label='std=2')
sns.kdeplot(data3, label='std=3')
# 添加标题和标签
plt.title('Normal Distribution')
plt.xlabel('x')
plt.ylabel('Density')
# 显示图形
plt.show()


# In[7]:


# 绘制卡方分布曲线
# sns.set(color_codes=True)
x = np.linspace(0, 10, 100)
y1 = chi2.pdf(x, 5)
y2 = chi2.pdf(x, 10)
sns.lineplot(x=x, y=y1, label='Chi-square(5)')
sns.lineplot(x=x, y=y2, label='Chi-square(10)')
plt.legend()
plt.show()


# In[8]:


# 绘制t分布曲线
# sns.set(color_codes=True)
x = np.linspace(-5, 5, 100)
y1 = t.pdf(x, 5)
y2 = t.pdf(x, 10)
sns.lineplot(x=x, y=y1, label='t(5)')
sns.lineplot(x=x, y=y2, label='t(10)')
plt.legend()
plt.show()


# In[9]:


# 绘制F分布曲线
# sns.set(color_codes=True)
x = np.linspace(0, 5, 100)
y1 = f.pdf(x, 5, 2)
y2 = f.pdf(x, 10, 5)
sns.lineplot(x=x, y=y1, label='F(5, 2)')
sns.lineplot(x=x, y=y2, label='F(10, 5)')
plt.legend()
plt.show()


# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm, f, t



# 绘制正态分布曲线
sns.set(color_codes=True)
x = np.linspace(-10, 10, 100)
y = norm.pdf(x, 0, 2)
sns.lineplot(x=x, y=y, label='Normal Distribution (mean=0, std=2)')
plt.legend()
plt.show()


# 绘制标准正态分布曲线
sns.set(color_codes=True)
x = np.linspace(-10, 10, 100)
y = norm.pdf(x, 0, 1)
sns.lineplot(x=x, y=y, label='Standard Normal Distribution')
plt.legend()
plt.show()


# 绘制F分布曲线
sns.set(color_codes=True)
x = np.linspace(0, 5, 100)
y1 = f.pdf(x, 5, 2)
y2 = f.pdf(x, 10, 5)
sns.lineplot(x=x, y=y1, label='F Distribution (dfn=5, dfd=2)')
sns.lineplot(x=x, y=y2, label='F Distribution (dfn=10, dfd=5)')
plt.legend()
plt.show()

# 绘制t分布曲线
sns.set(color_codes=True)
x = np.linspace(-5, 5, 100)
y1 = t.pdf(x, 5)
y2 = t.pdf(x, 10)
sns.lineplot(x=x, y=y1, label='t Distribution (df=5)')
sns.lineplot(x=x, y=y2, label='t Distribution (df=10)')
plt.legend()
plt.show()


# 求z值

# In[11]:


import scipy.stats
confidence = 0.95
alpha = 1 - confidence
z_score = scipy.stats.norm.isf(alpha / 2)
z_score


# 求t值

# In[12]:


import scipy.stats

confidence = 0.95
alpha = 1 - confidence
n = 30
t_score = scipy.stats.t.isf(alpha / 2, df=n-1)
t_score


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




