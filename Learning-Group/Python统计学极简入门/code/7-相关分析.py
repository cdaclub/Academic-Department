#!/usr/bin/env python
# coding: utf-8

# ## 统计学相关系数

# 前面的假设检验、方差分析基本上都是围绕差异性分析，不论是单个总体还是两个总体及以上，总之都是属于研究“区别”，从本节开始，我们关注“联系”，变量之间的关系分为 **函数关系和相关关系。** 本节这里重点探讨的是不同类型变量之间的相关性。除表中列出的常用方法外，还有Tetrachoric、$\phi$相关系数等方式

# 变量类型|变量类型|相关系数计算方法|示例
# -|-|-|-
# 连续型变量|连续型变量|Pearson(正态)/Spearman(非正态)|商品曝光量和购买转化率
# 二分类变量（无序）|连续型变量|Point-biserial|性别和疾病指数
# 无序分类变量|连续型变量|方差分析|不同教育水平的考试成绩
# 有序分类变量|连续型变量|连续指标离散化后当做有序分类|商品评分与购买转化率
# 二分类变量|二分类变量|数学公式: $\chi^2 $检验 联合 Cramer's V|性别和是否吸烟
# 二分类变量（有序）|连续型变量|Biserial| 乐器练习时间与考级是否通过
# 无序分类变量|无序分类变量|数学公式: $ \chi^2 $检验 / Fisher检验|手机品牌和年龄段
# 有序分类变量|无序分类变量|数学公式: $ \chi^2 $检验 |满意度和手机品牌
# 有序分类变量|有序分类变量|Spearman /Kendall Tau相关系数|用户等级和活跃程度等级

# ### 连续型变量 vs 连续型变量  : Pearson / Spearmanr

# #### Pearson
# Pearson相关系数度量了两个连续变量之间的线性相关程度；

# In[58]:


import random 
import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame({'商品曝光量':[1233,1333,1330,1323,1323,1142,1231,1312,1233,1123],
     '购买转化率':[0.033,0.034,0.035,0.033,0.034,0.029,0.032,0.034,0.033,0.031]})
df


# - Pandas计算Pearson相关系数

# In[59]:


pd.Series.corr(df['商品曝光量'], df['购买转化率'],method = 'pearson') # pearson相关系数


# - scipy计算Pearson相关系数

# In[60]:


import scipy.stats as stats

# 假设有两个变量X和Y
X = df['商品曝光量']
Y = df['购买转化率']

# 使用spearmanr函数计算斯皮尔曼相关系数和p值
corr, p_value = stats.pearsonr(X, Y)

print("Pearson相关系数:", corr)
print("p值:", p_value)


# #### Spearman等级相关系数
# Spearman等级相关系数可以衡量非线性关系变量间的相关系数，是一种非参数的统计方法，可以用于定序变量或不满足正态分布假设的等间隔数据；

# In[61]:


import random 
import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame({'品牌知名度排位':[9,4,3,6,5,8,1,7,10,2],
     '售后服务质量评价排位':[8,2,5,4,7,9,1,6,10,3]})
df


# - Pandas计算spearman相关系数

# In[62]:


pd.Series.corr(df['品牌知名度排位'], df['售后服务质量评价排位'],method = 'spearman') # spearman秩相关


# - scipy计算spearman相关系数

# In[63]:


import scipy.stats as stats

# 假设有两个变量X和Y
X = df['品牌知名度排位']
Y = df['售后服务质量评价排位']

# 使用spearmanr函数计算斯皮尔曼相关系数和p值
corr, p_value = stats.spearmanr(X, Y)

print("斯皮尔曼相关系数:", corr)
print("p值:", p_value)


# **结论**:`p = 0.0008＜0.05`，表明两变量之间的正向关系很显著。

# ### 二分类变量（自然）vs 连续型变量	:Point-biserial

# 假设我们想要研究性别对于某种疾病是否存在影响。我们有一个二元变量“性别”（男、女）和一个连续型变量“疾病指数”。我们想要计算性别与疾病指数之间的相关系数，就需要用到Point-biserial相关系数。

# In[64]:


import scipy.stats as stats

# 创建一个列表来存储数据
gender = [0, 1, 0, 1, 1, 0]
disease_index = [3.2, 4.5, 2.8, 4.0, 3.9, 3.1]

# 使用pointbiserialr函数计算Point-biserial相关系数和p值
corr, p_value = stats.pointbiserialr(gender, disease_index)

print("Point-biserial相关系数:", corr)
print("p值:", p_value)


# **结论**:`p = 0.007＜0.05`，表明两变量之间的正向关系很显著。即性别与疾病指数正相关

# ### 无序分类变量 vs 	连续型变量	： ANOVA

# 假设我们想要比较不同教育水平的学生在CDA考试成绩上是否存在显著差异。我们有一个无序分类变量“教育水平”（高中、本科、研究生）和一个连续型变量“考试成绩”。

# In[65]:


import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# 创建一个DataFrame来存储数据
data = pd.DataFrame({
    '教育水平': ['高中', '本科', '本科', '研究生', '高中', '本科', '研究生'],
    '考试成绩': [80, 90, 85, 95, 75, 88, 92]
})

# 使用ols函数创建一个线性模型
model = ols('考试成绩 ~ C(教育水平)', data=data).fit()

# 使用anova_lm函数进行方差分析
anova_table = sm.stats.anova_lm(model, typ=2)
anova_table


# **结论**:`p = 0.0102＜0.05`，拒绝原假设，表明两变量之间的正向关系很显著。教育水平与考试成绩正相关

# ### 有序分类变量 vs 	连续型变量

# 将连续型变量离散化后当做有序分类，然后用 有序分类变量 VS 有序分类变量的方法

# ### 二分类变量 vs 	二分类变量  ：$ \chi^2 $检验 联合 Cramer's V

# 一项研究调查了不同性别的成年人对在公众场合吸烟的态度，结果如表所示。那么，性别与对待吸烟的态度之间的相关程度
# 
# -|赞同|反对
# -|-|-
# 男|15|10
# 女|10|26
# 

# In[66]:


import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([[15, 10],
                     [10, 26]])
observed

chi2, p, dof, expected = chi2_contingency(observed,correction =False) # correction =False
# 卡方值 
# P值 
# 自由度： 
# 与原数据数组同维度的对应期望值

chi2, p


# **结论**:`p = 0.0118＜0.05`，拒绝原假设，表明两变量之间的正向关系很显著。

# In[67]:


phi = np.sqrt(chi2/n)
print("phi's V:", phi)


# > 卡方检验时有多种指标(SPSSAU提供五类)可表示效应量，可结合数据类型及交叉表格类型综合选择
# - 第一：如果是2*2表格，建议使用Phi指标；
# - 第二：如果是3*3,或4*4表格，建议使用列联系数；
# - 第三：如果是n*n(n>4)表格，建议使用校正列联系数；
# - 第四：如果是m*n(m不等于n)表格，建议使用Cramer V指标；
# - 第五：如果X或Y中有定序数据，建议使用Lambda指标；

# In[68]:


# 计算Cramer's V 
# 注：这里只是示例一下，实际m≠n的数据才用Cramer's V 
contingency_table = observed
n = contingency_table.sum().sum()
phi_corr = np.sqrt(chi2 / (n * min(contingency_table.shape) - 1))
v = phi_corr / np.sqrt(min(contingency_table.shape) - 1)

print("Cramer's V:", v)


# ### 二分类变量（有序）	连续型变量：	 Biserial	

# In[69]:


import numpy as np
from scipy.stats import pearsonr

# 生成随机的二元变量
binary_variable = np.random.choice([0, 1], size=100)

# 生成随机的连续变量
continuous_variable = np.random.normal(loc=0, scale=1, size=100)


# 注：此处的代码未经严格考证，请谨慎使用
def biserial_correlation(binary_variable, continuous_variable):
    binary_variable_bool = binary_variable.astype(bool)
    binary_mean = np.mean(binary_variable_bool)
    binary_std = np.std(binary_variable_bool)
    
    binary_variable_norm = (binary_variable_bool - binary_mean) / binary_std
    
    corr, _ = pearsonr(binary_variable_norm, continuous_variable)
    biserial_corr = corr * (np.std(continuous_variable) / binary_std)
    
    return biserial_corr

# 计算Biserial相关系数
biserial_corr = biserial_correlation(binary_variable, continuous_variable)

print("Biserial相关系数:", biserial_corr)


# ### 无序分类变量 vs 	无序分类变量	
# 
# 参考 $ \chi^2 $检验

# ### 有序分类变量	vs  无序分类变量
# 
# 参考 $ \chi^2 $检验 

# ### 有序分类变量	vs  有序分类变量

# #### Kendall秩相关系数
# Kendall秩相关系数也是一种非参数的等级相关度量，类似于Spearman等级相关系数。

# In[70]:


import random 
import numpy as np
import pandas as pd

np.random.seed(10)
df = pd.DataFrame({'品牌知名度排位':[9,4,3,6,5,8,1,7,10,2],
     '售后服务质量评价排位':[8,2,5,4,7,9,1,6,10,3]})
df


# In[71]:


pd.Series.corr(df['品牌知名度排位'], df['售后服务质量评价排位'],method = 'kendall') # Kendall Tau相关系数


# In[72]:


from scipy.stats import kendalltau

# 两个样本数据
x = df['品牌知名度排位']
y = df['售后服务质量评价排位']

# 计算Kendall Tau相关系数
correlation, p_value = kendalltau(x, y)

print("Kendall Tau相关系数:", correlation)
print("p值:", p_value)


# In[ ]:





# ----

# ### 补充案例 $\Phi$ 相关系数案例

# #### 性别与对待吸烟的态度之间的相关性
#    
# 一项研究调查了不同性别的成年人对在公众场合吸烟的态度，结果如表所示。那么，性别与对待吸烟的态度之间的相关系数是（）.
# 
# -|赞同|反对
# -|-|-
# 男|15|10
# 女|10|26
# 
# 
# 
# A．0.12
# B．0.32
# C．0.48
# D．0.54

# #### φ相关系数的定义及公式

# 问：φ相关系数的定义及公式：
# 1.测度2×2列联表中数据相关程度
# 
# 2.对于2×2列联表，φ系数的值在0～1之间
# 
# 3. φ相关系数计算公式为
# 
# 
# 
# 
# 
# 
# #### φ相关系数
# $ \phi = \sqrt{\frac{\chi^{2}}{n}} $ 
# n为实际频数的总个数，即样本容量
# 
# $ \chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$ 
# 
# 其中，$\chi^2$为卡方值，$O_{ij}$为观察值，$E_{ij}$为期望值。
# 

# 方法1 按公式手动计算$\phi$

# In[76]:


a = 15
b = 10
c =10
d =26

observed = [[a, b],
            [c, d]]


# In[77]:


n = a + b + c + d
chi = ((a*d - b*c)**2 * n) / ((a + b) * (c + d) * (a + c) * (b + d))
chi


# In[78]:


phi = np.sqrt(chi/n)
phi 


# 方法2：用scipy.stats里面的chi2_contingency计算$\chi$值，再计算$\phi$

# In[79]:


import numpy as np
from scipy.stats import chi2_contingency

observed = np.array([[15, 10],
                     [10, 26]])
observed


# In[80]:


chi2, p, dof, expected = chi2_contingency(observed,correction =False) # correction =False 通过设置correction参数来控制是否进行校正
# 卡方值 
# P值 
# 自由度： 
# 与原数据数组同维度的对应期望值

chi2


# In[81]:


n = observed.sum()
phi = np.sqrt(chi2 / n)

print("Phi相关系数:", phi)


# In[82]:


pd.DataFrame(observed)


# In[83]:


import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# 创建一个DataFrame来存储数据
data = pd.DataFrame({
    '教育水平': ['高中', '本科', '本科', '研究生', '高中', '本科', '研究生'],
    '职业类型': ['技工', '技工', '白领', '白领', '技工', '白领', '白领']
})

# 创建一个列联表
contingency_table = pd.crosstab(data['教育水平'], data['职业类型'])

# 使用chi2_contingency函数进行卡方检验
chi2, p_value, _, _ = chi2_contingency(contingency_table,correction =False)

# 计算Cramer's V
n = contingency_table.sum().sum()
phi_corr = np.sqrt(chi2 / (n * min(contingency_table.shape) - 1))
v = phi_corr / np.sqrt(min(contingency_table.shape) - 1)

print("Cramer's V:", v)
print("p值:", p_value)


# In[ ]:





# [Pearson、Spearman、Kendall、Polychoric、Polyserial相关系数简介及R计算](https://mp.weixin.qq.com/s/5gZ3LvQ3pN8RZyMkNAxlMQ)

# [要做相关性分析，该如何选择正确的统计方法？](https://mp.weixin.qq.com/s?__biz=MzI2OTQyMzc5MA==&mid=2247507766&idx=1&sn=fa9db440c2fd8dac4586c2577f873e62&chksm=eae21af7dd9593e1f4a3a7ba506b3479e2e4e2f66d9a10504ae140218b1f2680076ff6544870&scene=27)

# [相关分析最全总结](https://zhuanlan.zhihu.com/p/396580986?utm_id=0)

# [Pearson、Spearman、Kendall、Polychoric、Polyserial相关系数简介及R计算](https://mp.weixin.qq.com/s/5gZ3LvQ3pN8RZyMkNAxlMQ)

# In[ ]:




