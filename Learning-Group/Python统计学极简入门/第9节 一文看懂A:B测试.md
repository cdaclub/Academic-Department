## 一文看懂A/B测试（含Python代码实现流程、假设检验原理及2个案例）


前面学完了统计学的基础内容，以及t检验、F检验、卡方检验等。本节我们尝试再用“MVP”的思路来梳理A/B测试：实施的流程、假设检验原理（z检验、t检验应用场景的区别）及分组的注意事项（设计AA分组对比原分组的分布以确保分组的科学性），最后用2个小案例结合Python代码来演示假设检验的过程。


AB测试是一种常用的实验设计方法，用于**比较两个或多个不同的版本（例如产品、网页设计、广告等）在某个指标上的表现差异**。而**假设检验是AB测试的统计分析方法**，用于**判断这些差异是否具有统计学意义。**

1. 假设检验的一般步骤
    - (1) 提出原假设H0和备择假设H1
    - (2) 用均值之差 或者 比例之差作为检验统计量 z检验 或者 t检验，并计算统计量及p值
    - (3) 根据p值与显著性水平判断是否拒绝H0

2. 基于假设检验的AB测试步骤
    - (1) H0假设:A组转化率等于B组转化率 H1假设:A组转化率不等于B组转化率
    - (2) 用均值之差t检验 或者 比例之差z检验; 并计算统计量及p值
    - (3) 判断p值是否小于显著性水平0.05，判断是否拒绝H0


### 案例9-1 使用基于均值的假设检验进行AB测试 



```python
# 随机生成两组样本数据
import numpy as np
from scipy import stats
# 假设有两个版本 A 和 B
# 生成样本数据，这里使用正态分布作为例子
np.random.seed(0)
sample_A = np.random.normal(loc=91, scale=4, size= 1000)
sample_B = np.random.normal(loc=95, scale=4, size= 1000)
# 计算样本均值和标准差
mean_A = np.mean(sample_A)
mean_B = np.mean(sample_B)
std_A = np.std(sample_A)
std_B = np.std(sample_B)
```

步骤1: 提出原假设H0和备择假设H1

H0:版本 A 和 B 在统计上存在显著差异

H2:版本 A 和 B 在统计上没有显著差异

步骤2: 使用均值之差的t检验，计算出t统计量的值和P值如下


```python
# 假设零假设为版本 A 和 B 的均值相等
# 使用独立样本 t 检验进行假设检验
t_statistic, p_value = stats.ttest_ind(sample_A, sample_B)
print(t_statistic, p_value)
```

    -24.206499153286355 9.893622835346878e-114


步骤3: 进行假设检验


```python
# 步骤5: 判断结果

alpha = 0.05  # 设置显著性水平
if p_value < alpha:
    print("拒绝零假设（无差异），版本 A 和 B 在统计上存在显著差异")
else:
    print("接受零假设（无差异），版本 A 和 B 在统计上没有显著差异")
```

    拒绝零假设（无差异），版本 A 和 B 在统计上存在显著差异


值得注意的是，通常情况下我们在做AB测试前需要做AA测试，也就是从A里面通过不同的抽样方式选定一定样本AA，再与A进行测试


#### AA测试（简单随机抽样）


```python
# 简单随机抽样
sample_AA1 = np.random.choice(sample_A,int(len(sample_A)*0.2)) 
```


```python
# 假设零假设为版本 A 和 B 的均值相等
# 使用独立样本 t 检验进行假设检验
t_statistic, p_value = stats.ttest_ind(sample_A, sample_AA1)
# 步骤5: 判断结果

alpha = 0.05  # 设置显著性水平
if p_value < alpha:
    print(f"p = {p_value} < 0.05，拒绝零假设（无差异），版本 A 和 AA1 在统计上存在显著差异")
else:
    print(f"p = {p_value} > 0.05,接受零假设（无差异），版本 A 和 AA1 在统计上没有显著差异")
```

    p = 0.8914256267444793 > 0.05,接受零假设（无差异），版本 A 和 AA1 在统计上没有显著差异



```python
import seaborn as sns
import matplotlib.pyplot as plt

# 绘制 sample_A 和 sample_AA, 的分布曲线图
plt.figure(figsize=(10, 6))
sns.histplot(sample_A, kde=True, color='blue', label='Sample A')
sns.histplot(sample_AA1, kde=True, color='orange', label='Sample AA1')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Sample A and Sample AA')
plt.legend()
plt.show()
```



![](https://files.mdnice.com/user/33324/455a9996-1ea8-4f0d-b497-53b891d8b2aa.png)



#### AA测试（分层抽样）


```python
## 分层抽样
layers = np.repeat(['A','B','C','D','E'], 200)

# 在每个分层中抽样
s1 = np.random.choice(sample_A[layers=='A'], size=40) 
s2 = np.random.choice(sample_A[layers=='B'], size=40) 
s3 = np.random.choice(sample_A[layers=='C'], size=40) 
s4 = np.random.choice(sample_A[layers=='D'], size=40) 
s5 = np.random.choice(sample_A[layers=='E'], size=40) 


sample_AA2 =np.concatenate([s1, s2, s3, s4, s5])
```


```python
# 假设零假设为版本 A 和 B 的均值相等
# 使用独立样本 t 检验进行假设检验
t_statistic, p_value = stats.ttest_ind(sample_A, sample_AA2)
# 步骤5: 判断结果

alpha = 0.05  # 设置显著性水平
if p_value < alpha:
    print(f"p = {p_value} < 0.05，拒绝零假设（无差异），版本 A 和 AA2 在统计上存在显著差异")
else:
    print(f"p = {p_value} > 0.05,接受零假设（无差异），版本 A 和 AA2 在统计上没有显著差异")
```

    p = 0.6702407975402769 > 0.05,接受零假设（无差异），版本 A 和 AA2 在统计上没有显著差异



```python
import seaborn as sns
import matplotlib.pyplot as plt

# 绘制 sample_A 和 sample_AA, 的分布曲线图
plt.figure(figsize=(10, 6))
sns.histplot(sample_A, kde=True, color='blue', label='Sample A')
sns.histplot(sample_AA2, kde=True, color='orange', label='Sample AA2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Sample A and Sample AA2')
plt.legend()
plt.show()
```


![](https://files.mdnice.com/user/33324/59eb1f88-b356-47ea-a0d2-2416c2737791.png)



#### AA测试（系统抽样）


```python
# 系统抽样
k = 5 # 每隔3个取一个
sample_AA3 = sample_A[::k] 
```


```python
# 假设零假设为版本 A 和 B 的均值相等
# 使用独立样本 t 检验进行假设检验
t_statistic, p_value = stats.ttest_ind(sample_A, sample_AA3)
# 步骤5: 判断结果

alpha = 0.05  # 设置显著性水平
if p_value < alpha:
    print(f"p = {p_value} < 0.05，拒绝零假设（无差异），版本 A 和 AA3 在统计上存在显著差异")
else:
    print(f"p = {p_value} > 0.05,接受零假设（无差异），版本 A 和 AA3 在统计上没有显著差异")
```

    p = 0.4730028024029992 > 0.05,接受零假设（无差异），版本 A 和 AA3 在统计上没有显著差异



```python
import seaborn as sns
import matplotlib.pyplot as plt

# 绘制 sample_A 和 sample_AA, 的分布曲线图
plt.figure(figsize=(10, 6))
sns.histplot(sample_A, kde=True, color='blue', label='Sample A')
sns.histplot(sample_AA3, kde=True, color='orange', label='Sample AA3')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Sample A and Sample AA3')
plt.legend()
plt.show()
```



![](https://files.mdnice.com/user/33324/70ab7586-78c3-4201-b046-8fc188f32b45.png)



### AB测试


```python
# 假设零假设为版本 A 和 B 的均值相等
# 使用独立样本 t 检验进行假设检验
t_statistic, p_value = stats.ttest_ind(sample_A, sample_B)
# 步骤5: 判断结果

alpha = 0.05  # 设置显著性水平
if p_value < alpha:
    print(f"p = {p_value} < 0.05，拒绝零假设（无差异），版本 A 和 B 在统计上存在显著差异")
else:
    print(f"p = {p_value} > 0.05,接受零假设（无差异），版本 A 和 B 在统计上没有显著差异")
```

    p = 9.893622835346878e-114 < 0.05，拒绝零假设（无差异），版本 A 和 B 在统计上存在显著差异



```python
import seaborn as sns
import matplotlib.pyplot as plt

# 绘制 sample_A 和 sample_B 的分布曲线图
plt.figure(figsize=(10, 6))
sns.histplot(sample_A, kde=True, color='blue', label='Sample A')
sns.histplot(sample_B, kde=True, color='orange', label='Sample B')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Distribution of Sample A and Sample B')
plt.legend()
plt.show()
```



![](https://files.mdnice.com/user/33324/635ae71e-cd15-42fa-9c89-23b91741c84f.png)



在这个例子中，我们假设有两个版本 A 和 B，通过生成正态分布的样本数据进行比较。然后计算两个样本的均值和标准差，并使用独立样本 t 检验进行假设检验。根据显著性水平 alpha 的设定，判断是否拒绝零假设，进而得出结论。

---

### 案例：基于假设检验的支付宝点击率策略提升A-B测试效果分析


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```


```python
#加载数据
data = pd.read_csv('./data/audience_expansion/effect_tb.csv',header = None)

data.columns = ["dt","user_id","label","dmp_id"]
# dmp_id:营销策略编号（源数据文档未做说明，这个根据情况设定为1.对照组，2.营销策略一，3.营销策略二）
# user_id:支付宝用户id
# label:用户当天是否点击活动广告(0:未点击，1：点击)

data = data[["user_id","label","dmp_id"]]
data = data.drop_duplicates() #删除重复值
data.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>user_id</th>
      <th>label</th>
      <th>dmp_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1000004</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1000004</td>
      <td>0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



#### 计算3组营销策略的点击率的平均值

根据原始数据计算3营销策略的点击率如下：


```python
df = data.pivot_table(index = "dmp_id",columns = "label",values = "user_id",aggfunc = "count",margins = True)
df['crt'] = df[1] / df['All']
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>label</th>
      <th>0</th>
      <th>1</th>
      <th>All</th>
      <th>crt</th>
    </tr>
    <tr>
      <th>dmp_id</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>1881745</td>
      <td>23918</td>
      <td>1905663</td>
      <td>0.012551</td>
    </tr>
    <tr>
      <th>2</th>
      <td>404811</td>
      <td>6296</td>
      <td>411107</td>
      <td>0.015315</td>
    </tr>
    <tr>
      <th>3</th>
      <td>307923</td>
      <td>8282</td>
      <td>316205</td>
      <td>0.026192</td>
    </tr>
    <tr>
      <th>All</th>
      <td>2594479</td>
      <td>38496</td>
      <td>2632975</td>
      <td>0.014621</td>
    </tr>
  </tbody>
</table>
</div>



我们可以得到：

- 对照组 （dmp_id=1）的点击率0.012551 ，
- 策略1组（dmp_id=2）的点击率0.015315 ，
- 策略2组（dmp_id=2）的点击率0.026192 ，


```python
df['crt'][1:3]-0.012551 # 2
```




    dmp_id
    2    0.002764
    3    0.013641
    Name: crt, dtype: float64



从点击率来看，策略一和策略二在对照组的基础上都有一定的提升。

其中策略一提高了0.2个百分点，策略二提高了1.3个百分点，只有策略二满足了我们对点击率提升最小值1个百分点的要求

接下来需要进行假设验证，来看看策略二的点击率提升是否显著

#### 假设检验进行判断

记对照组点击率为p1，策略二点击率为p2，则：
- (1) H0假设: p1>=p2 策略2组点击率大于等于对照组点击率 H1假设:p1< p2 策略2组点击率小于对照组点击率
- (2) 计算A组和B组样本的转化率
- (3) 用转化率之差作为检验统计量 z检验
- (4) 计算p值
- (5) 判断p值是否小于显著性水平0.05，判断是否拒绝H0


```python
import numpy as np
import scipy.stats as stats

def proportion_test(p1, p2, n1, n2, side='two-sided'):
    """
    参数：
    p1: 样本1的比例
    p2: 样本2的比例
    n1: 样本1的数量
    n2: 样本2的数量
    side: 假设检验的方向，可选'two-sided'（双侧检验，默认）, 'greater'（右侧检验）, 'less'（左侧检验）

    返回值：
    z_value: Z统计量的值
    p_value: 对应的p值
    """
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z_value = (p1 - p2) / se

    if side == 'two-sided':
        p_value = 2 * (1 - stats.norm.cdf(np.abs(z_value)))
    elif side == 'greater':
        p_value = 1 - stats.norm.cdf(z_value)
    elif side == 'less':
        p_value = stats.norm.cdf(z_value)
    else:
        raise ValueError("Invalid side value. Must be 'two-sided', 'greater', or 'less'.")

    return z_value, p_value
```


```python

p1 = df.loc[1,'crt']
p2 = df.loc[3,'crt']
n1 = df.loc[1,'All']
n2 = df.loc[3,'All']

z_value, p_value = proportion_test(p1, p2, n1, n2, side='less')
# 选择双侧检验 alternative = 'two-sided'

print("Z_value:", z_value)
print("p_value:", p_value)
```

    Z_value: -59.44168632985996
    p_value: 0.0



```python
# 直接用 sp.proportions_ztest 函数也可以，注意带入的是人数而非比例

import statsmodels.stats.proportion as sp

p1 = df.loc[1,1]
p2 = df.loc[3,1]
n1 = df.loc[1,'All']
n2 = df.loc[3,'All']

z_value, p_value = sp.proportions_ztest([p1, p2],[n1, n2], alternative = "smaller")
# 选择双侧检验 alternative = 'two-sided'

print("Z_value:", z_value)
print("p_value:", p_value)
```

    Z_value: -59.44168632985996
    p_value: 0.0


可以看到，p约等于0 < 0.05。所以拒绝原假设，认为策略2点击率的提升在统计上是显著的。两种营销策略中，策略二对广告点击率有显著提升效果，因而在两组营销策略中应选择第二组进行推广
