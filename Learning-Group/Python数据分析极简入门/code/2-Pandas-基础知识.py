#!/usr/bin/env python
# coding: utf-8

# ## Pandas简介

# 说好开始学Python，怎么到了Pandas？
# 
# 前面说过，既然定义为极简入门，我们只抓核心中的核心。
# 
# 那怎么样挑核心重点呢？
# 
# 在你不熟悉的情况下，肯定需要请教别人，需要注意的是，不要去问应该学什么编程语言，而是去问，如果只学一门编程语言，应该学什么？
# 
# 这样，问题就从多分类的选择题，变成了一道优化题！有人说选择大于努力，而现实中的情况是，我们选的不是答案只有对与错的问题，而是在好、次好与更好之间选更好，这个道理看似简单，但却不容易做到，小到你学Python应该优先学什么，大到一个国家的资源配置应该优先发展什么？本质上都是最优化问题。
# 
# 回到今天的主题，如果学Python语言，但只学一个库，你要学什么？有人说人工智能好啊，我要学算法，错！算法再牛也需要你从底层的数据开始，所以答案肯定是Pandas，这属于做数据分析处理数据必知必会的内容。
# ![](https://pic4.zhimg.com/v2-c879e89d76b011a00c55acde413397da_r.jpg?source=172ae18b)
# 
# 今天的故事，要从08年北京奥运会那年说起，远在纽约一家量化投资公司的打工人[Wes McKinney](https://www.amazon.com/Wes-McKinney/e/B00E5SITSI%3Fref=dbs_a_mng_rwt_scns_share)
# ，由于在日常数据分析工作中 ~~想多摸会儿鱼~~ 备受Excel与SQL等工具的折磨，于是他开始构建了一个新项目 **Pandas**，用来解决数据处理过程中遇到的全部任务。
# 
# ![Wes McKinney](https://images-na.ssl-images-amazon.com/images/I/613hVcZv3LL._US230_.jpg)

# ### 什么是Pandas？
# 
# Pandas是一个开源的Python库，主要用于数据分析、数据处理、数据可视化。
# 
# Pandas作为Python数据分析的核心包，提供了大量的数据分析函数，包括数据处理、数据抽取、数据集成、数据计算等基本的数据分析手段。
# 
# Pandas的名称来自于面板数据（panel data）和python数据分析（data analysis）的简称。
# 
# 千万记得Pandas不是咱们的国宝大熊猫的复数形式！！！（尽管这一强调极有可能适得其反，但还是忍不住贴一张panda的图）
# 
# ![Panda](https://edu.cda.cn/files/course/2023/10-23/185646ea4907573475.jpg)
# 
# 
# 
# ### 为什么Pandas必学？
# 
# - 比SQL语句还要简洁，查询数据事半功倍！简单
# 
# - 基于Numpy数值计算，数据处理高效运算！高效
# 
# - 支持数值、文本和可视化，快速灵活完成数据需求！强大
# 
# 
# 如果用一个字来说明，那就是“快”。这个快指的是你从开始构思到写完代码的时间，毫不夸张地说，当你把数据需求用文字梳理清楚的时候，基本上也就相当于用Python实现了这一过程，因为在Python的世界，所见即所得
# 
# 
# ### 怎么学Pandas？
# 
# 把大象放进冰箱里需要三步，打开冰箱门、把大象塞进去、关上冰箱门。同样地，怎么学Pandas，也需要三步
# 
# 第一步，必须了解Pandas的数据结构。在之前的系列文章里面说过，学习语言学习的三板斧，数据结构，流程控制，自定义函数。这里pandas虽然只是一个库，但同样有其数据结构。
# - pandas 简介
# - pandas 数据类型
#     - Series
#     - DataFrame
# - pandas 数据查看
# 
# 第二步，必须学会用Pandas做数据处理。这是你做数据分析的基本功，里面包含如下内容
# 
# - pandas 条件查询
# - pandas 数据计算
# - pandas 合并连接
# - pandas 分组聚合
# - pandas 数据重塑
# 
# 第三步，掌握一些Pandas高阶与展示技巧。这是你分析或展示的必备技能
# 
# 
# - pandas 文本数据
# - pandas 时间数据
# - pandas 窗口数据
# - pandas 数据读写
# - pandas 表格样式
# - pandas 数据可视化

# ## Pandas数据类型

# Pandas 有两种自己独有的基本数据结构。需要注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以 Python 中有的数据类型在这里依然适用。我们分别看一下这两种数据结构：
# 
# 
# #### Series
# 
# Series：一维数组。该结构能够放置各种数据类型，比如字符、整数、浮点数等

# 我们先引入pandas包，这里有一个约定成俗的写法`import pandas as pd` 将pandas引入，并命其别名为pd
# 
# 接着将列表`[2,3,5,7,11]`放到pd.Series()里面

# In[2]:


import pandas as pd
s = pd.Series([2,3,5,7,11],name = 'A')
s


# Time- Series：以时间为索引的Series

# 同样的，将列`['2024-01-01 00:00:00', '2024-01-01 03:00:00','2024-01-01 06:00:00']` 放到pd.DatetimeIndex()里面

# In[2]:


dts1 = pd.DatetimeIndex(['2024-01-01 00:00:00', '2024-01-01 03:00:00','2024-01-01 06:00:00'])
dts1


# 还有另外一种写法`pd.date_range` 可以按一定的频率生成时间序列

# In[3]:


dts2 = pd.date_range(start='2024-01-01', periods=6, freq='3H')
dts2


# In[4]:


dts3 = pd.date_range('2024-01-01', periods=6, freq='d')
dts3


# #### DataFrame
# 
# DataFrame：二维的表格型数据结构,可以理解为Series的容器，通俗地说，就是可以把Series放到DataFrame里面。
# 
# 它是一种二维表格型数据的结构，既有行索引，也有列索引。行索引是 index，列索引是 columns。类似于初中数学里，在二维平面里用坐标轴来定位平面中的点。
# 
# 
# 注意，DataFrame又是Pandas的核心!接下来的内容基本上以DataFrame为主

# 先来看看如何创建DataFrame，上面说过Series也好，DataFrame也罢，本质上都是容器。
# 
# 千万别被”容器“这个词吓住了，通俗来说，就是里面可以放东西的东西。

# **从字典创建DataFrame**

# 相当于给里面放dict：先创建一个字典`d`,再把`d`放进了`DataFrame`里命名为`df`

# In[291]:


d = {'A': [1, 2, 3], 
     'B': [4, 5, 6],
     'C': [7, 8, 9]}
df = pd.DataFrame(data = d)
df


# **从列表创建DataFrame**

# 先创建了一个列表`d`,再把`d`放进了`DataFrame`里命名为`df`

# In[292]:


d = [[4, 7, 10],[5, 8, 11],[6, 9, 12]]
df1 = pd.DataFrame(
    data = d,
    index=['a', 'b', 'c'],
    columns=['A', 'B', 'C'])
df1


# **从数组创建DataFrame**

# 数组（array）对你来说可能是一个新概念，在Python里面，创建数组需要引入一个类似于Pandas的库，叫做Numpy。与前面引入Pandas类似，我们用 `import numpy as np`来引入numpy，命其别名为np。
# 
# 同样的，先创建一个数组`d`,再把`d`放进了`DataFrame`里命名为`df`

# In[293]:


import numpy as np
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df2 = pd.DataFrame(data = d,
                   index=['a', 'b', 'c'],
                   columns=['A', 'B', 'C'])
df2


# 以上，我们用了不同的方式来创建DataFrame，接下来，我们看看创建好后，如何查看数据

# ---

# ## Pandas数据查看

# 这里我们创建一个`DataFrame`命名为`df`

# In[294]:


import numpy as np
import pandas as pd
d =  np.array([[81, 28, 24, 25, 96],
       [ 8, 35, 56, 98, 39],
       [13, 39, 55, 36,  3],
       [70, 54, 69, 48, 12],
       [63, 80, 97, 25, 70]])
df = pd.DataFrame(data = d,
                  columns=list('abcde'))
df


# 查看前n行

# In[295]:


df.head(2)


# 查看后n行

# In[296]:


df.tail(2)


# 查看随机N行

# In[297]:


df.sample(2)


# #### 按列选取

# 单列选取，我们有3种方式可以实现

# 第一种，直接在`[]`里面写上要筛选的列名

# In[298]:


df['a']


# 第二种，在`.iloc[]`里的`,`前面写上要筛选的行索引，在`,`后面写上要删选的列索引。其中`:`代表所有，`0:3`代表从索引0到2

# In[299]:


df.iloc[0:3,0]


# 第三种，直接`.`后面写上列名

# In[300]:


df.a


# 同样的，选择多列常见的也有3种方式：

# 第一种，直接在`[]`里面写上要筛选的列名组成的列表`['a','c','d']`

# In[301]:


df[['a','c','d']]


# 第二种，在`.iloc[]`里面行索引位置写`：`选取所有行，列索引位置写上要筛选的列索引组成的列表`[0,2,3]`

# In[302]:


df.iloc[:,[0,2,3]]


# 第三种，在`.loc[]`里面的行索引位置写`：`来选取所有行，在列索引位置写上要筛选的列索引组成的列表`['a','c','d']`

# In[303]:


df.loc[:,['a','c','d']]


# #### 按行选取

# 直接选取第一行

# In[304]:


df[0:1]


# 用`loc`选取第一行 

# In[305]:


df.loc[0:0]


# 选取任意多行

# In[306]:


df.iloc[[1,3],]


# 选取连续多行

# In[307]:


df.iloc[1:4,:]


# #### 指定行列

# 指定行列值

# In[309]:


df.iat[2,2] # 根据行列索引


# In[311]:


df.at[2,'c'] # 根据行列名称


# 指定行列区域

# In[101]:


df.iloc[[2,3],[1,4]]


# 以上是关于如何查看一个DataFrame里的数据，包括用`[]`、`iloc`、`iat`等方式选取数据，接下来我们来看如何用条件表达式来筛选数据：
# 
# 
# ---

# ## Pandas条件查询

# 在pandas中，可以使用条件筛选来选择满足特定条件的数据

# In[117]:


import pandas as pd
d =  np.array([[81, 28, 24, 25, 96],
       [ 8, 35, 56, 98, 39],
       [13, 39, 55, 36,  3],
       [70, 54, 69, 48, 12],
       [63, 80, 97, 25, 70]])
df = pd.DataFrame(data = d,
                  columns=list('abcde'))
df


# In[118]:


# 单一条件
df[df['a']>60]
df.loc[df['a']>60]


# In[119]:


# 单一条件&多列
df.loc[(df['a']>60) ,['a','b','d']]


# In[120]:


# 多条件
df[(df['a']>60) & (df['b']>60)]


# In[121]:


# 多条件 筛选行 & 指定列筛选列
df.loc[(df['a']>60) & (df['b']>60) ,['a','b','d']]


# 以上是使用条件筛选来选取数据 ，接下来我们来看如何对数据进行数学计算
# 
# ---
# 

# ## Pandas数学计算

# In[10]:


import pandas as pd
import numpy as np
d =  np.array([[81, 28, 24, 25, 96],
       [ 8, 35, 56, 98, 39],
       [13, 39, 55, 36,  3],
       [70, 54, 69, 48, 12],
       [63, 80, 97, 25, 70]])
df = pd.DataFrame(data = d,
                  columns=list('abcde'))
df


# #### 聚合计算

# 聚合计算是指对数据进行汇总和统计的操作。常用的聚合计算方法包括计算均值、求和、最大值、最小值、计数等。

# In[11]:


df['a'].mean()


# In[12]:


df['a'].sum()


# In[13]:


df['a'].max()


# In[14]:


df['a'].min()


# In[15]:


df['a'].count()


# In[16]:


df['a'].median() # 中位数


# In[17]:


df['a'].var() #方差


# In[18]:


df['a'].skew() # 偏度


# In[19]:


df['a'].kurt() # 峰度


# In[20]:


df['a'].cumsum() # 累计求和


# In[21]:


df['a'].cumprod() # 累计求积


# In[22]:


df['a'].diff() # 差分


# In[23]:


df['a'].mad() # 平均绝对偏差


# #### 按行、列聚合计算
# 

# In[31]:


df


# In[32]:


df.sum(axis=0)  # 按列求和汇总到最后一行


# In[33]:


df.sum(axis=1)  # 按行求和汇总到最后一列 


# In[26]:


df.describe() # 描述性统计


# #### agg函数

# 对整个DataFrame批量使用多个聚合函数

# In[27]:


df.agg(['sum', 'mean','max','min','median'])


# 对DataFramed的某些列应用不同的聚合函数

# In[28]:


df.agg({'a':['max','min'],'b':['sum','mean'],'c':['median']})


# #### apply、applymap、map函数

# 在Python中如果想要对数据使用函数，可以借助apply(),applymap(),map()对数据进行转换，括号里面可以是直接函数式，或者自定义函数（def）或者匿名函数（lambad）

# 1、当我们要对数据框（DataFrame）的数据进行按行或按列操作时用apply()

# In[30]:


df


# In[29]:


df.apply(lambda x :x.max()-x.min(),axis=1)
#axis=1，表示按行对数据进行操作
#从下面的结果可以看出，我们使用了apply函数之后，系统自动按行找最大值和最小值计算，每一行输出一个值


# In[160]:


df.apply(lambda x :x.max()-x.min(),axis=0)
#默认参数axis=0,表示按列对数据进行操作
#从下面的结果可以看出，我们使用了apply函数之后，系统自动按列找最大值和最小值计算，每一列输出一个值


# 2、当我们要对数据框（DataFrame）的每一个数据进行操作时用applymap()，返回结果是DataFrame格式

# In[161]:


df.applymap(lambda x : 1 if x>60 else 0)
#从下面的结果可以看出，我们使用了applymap函数之后，
#系统自动对每一个数据进行判断，判断之后输出结果


# 3、当我们要对Series的每一个数据进行操作时用map()

# In[162]:


df['a'].map(lambda x : 1 if x>60 else 0)


# 总结：
# 
# `apply()` 函数可以在DataFrame或Series上应用自定义函数，可以在行或列上进行操作。
# 
# `applymap()` 函数只适用于DataFrame，可以在每个元素上应用自定义函数。
# 
# `map()` 函数只适用于Series，用于将每个元素映射到另一个值。

# 以上是数学运算部分，包括聚合计算、批量应用聚合函数，以及对Series和DataFrame进行批量映射，接下来我们来看如何对数据进行合并拼接
# 
# ---

# ## Pandas合并连接

# 在pandas中，有多种方法可以合并和拼接数据。常见的方法包括`append()`、`concat()`、`merge()`。

# ### 追加(Append)

# append()函数用于将一个DataFrame或Series对象追加到另一个DataFrame中。

# In[181]:


import pandas as pd
df1 = pd.DataFrame({'A': ['a', 'b'],
                   'B': [1, 2]})
df1


# In[182]:


df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'B': [2, 3, 4]})
df2


# In[183]:


df1.append(df2,ignore_index=True) 


# ### 合并(Concat)

# concat()函数用于沿指定轴将多个对象（比如Series、DataFrame）堆叠在一起。可以沿行或列方向进行拼接。

# 先看一个上下堆叠的例子

# In[1]:


df1 = pd.DataFrame({'A': ['a', 'b'],
                   'B': [1, 2]})
df1


# In[194]:


df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'B': [2, 3, 4]})
df2


# In[195]:


pd.concat([df1,df2],axis =0) # 上下拼接


# 再看一个左右堆叠的例子

# In[196]:


df1 = pd.DataFrame({'A': ['a', 'b']})
df1


# In[197]:


df2 = pd.DataFrame({'B': [1, 2],
                    'C': [2, 4]})
df2


# In[198]:


pd.concat([df1,df2],axis =1) # 左右拼接


# ### 连接（Merge）
# 
# `merge()`函数用于根据一个或多个键将两个DataFrame的行连接起来。类似于SQL中的JOIN操作。

# #### 数据连接 1 (pd.merge)

# 先看一下 `inner` 和 `outer`连接

# In[3]:


df1 = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': [1, 2, 3]})
df1


# In[4]:


df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'B': [2, 3, 4]})
df2


# In[5]:


pd.merge(df1,df2,how = 'inner')


# In[6]:


pd.merge(df1,df2,how = 'outer')


# #### 数据连接  2 (pd.merge)

# 再看左右链接的例子：

# In[7]:


df1 = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': [1, 2, 3]})
df1


# In[8]:


df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'C': [2, 3, 4]})
df2


# In[209]:


pd.merge(df1,df2,how = 'left',on = "A")  # 左连接


# In[210]:


pd.merge(df1,df2,how = 'right',on = "A") # 右连接


# In[211]:


pd.merge(df1,df2,how = 'inner',on = "A") # 内连接


# In[216]:


pd.merge(df1,df2,how = 'outer',on = "A") # 外连接


# 补充1个小技巧

# In[220]:


df1[df1['A'].isin(df2['A'])] # 返回在df1中列'A'的值在df2中也存在的行


# In[221]:


df1[~df1['A'].isin(df2['A'])] # 返回在df1中列'A'的值在df2中不存在的行


# ## Pandas分组聚合

# 分组聚合（group by）顾名思义就是分2步：
# 
# - **先分组**：根据某列数据的值进行分组。用`groupby()`对某列进行分组
# - **后聚合**：将结果应用聚合函数进行计算。在`agg()`函数里应用聚合函数计算结果，如`sum()、mean()、count()、max()、min()`等，用于对每个分组进行聚合计算。

# In[441]:


import pandas as pd
import numpy as np
import random


# In[458]:


df = pd.DataFrame({'A': ['a', 'b', 'a', 'b','a', 'b'],
                   'B': ['L', 'L', 'M', 'N','M', 'M'],
                   'C': [107, 177, 139, 3, 52, 38],
                   'D': [22, 59, 38, 50, 60, 82]})

df


# **单列分组**

# ① 对单列分组后应用`sum`聚合函数

# In[451]:


df.groupby('A').sum()


# ② 对单列分组后应用单个指定的聚合函数

# In[452]:


df.groupby('A').agg({'C': 'min'}).rename(columns={'C': 'C_min'})


# ③ 对单列分组后应用多个指定的聚合函数

# In[455]:


df.groupby(['A']).agg({'C':'max','D':'min'}).rename(columns={'C':'C_max','D':'D_min'})


# **两列分组**

# ① 对多列分组后应用`sum`聚合函数：

# In[456]:


df.groupby(['A', 'B']).sum()


# ② 对两列进行`group` 后，都应用`max`聚合函数

# In[438]:


df.groupby(['A','B']).agg({'C':'max'}).rename(columns={'C': 'C_max'})


# ③ 对两列进行分组`group` 后，分别应用`max`、`min`聚合函数

# In[433]:


df.groupby(['A','B']).agg({'C':'max','D':'min'}).rename(columns={'C':'C_max','D':'D_min'})


# **补充1：** 应用自定义的聚合函数

# In[468]:


df = pd.DataFrame({'A': ['a', 'b', 'a', 'b','a', 'b'],
                   'B': ['L', 'L', 'M', 'N','M', 'M'],
                   'C': [107, 177, 139, 3, 52, 38],
                   'D': [22, 59, 38, 50, 60, 82]})

df


# In[469]:


# 使用自定义的聚合函数计算每个分组的最大值和最小值
def custom_agg(x):
    return x.max() - x.min()
result =  df[['B','C']].groupby('B').agg({'C': custom_agg})
result


# **补充2：** 开窗函数（类似于SQL里面的`over partition by`）：
# 
# 使用transform函数计算每个分组的均值

# In[470]:


# 使用transform函数计算每个分组的均值
df['B_C_std'] =  df[['B','C']].groupby('B')['C'].transform('mean')
df


# **补充3：** 分组聚合拼接字符串 pandas实现类似 group_concat 功能

# 假设有这样一个数据：

# In[472]:


df = pd.DataFrame({
    '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
    '科目': ['语文', '数学', '英语', '语文', '数学', '英语']
})

df


# **补充：按某列分组，将另一列文本拼接合并**
# 
# 按名称分组，把每个人的科目拼接到一个字符串：

# In[473]:


# 对整个group对象中的所有列应用join 连接元素
(df.astype(str)# 先将数据全转为字符
.groupby('姓名')# 分组
.agg(lambda x : ','.join(x)))[['科目']]# join 连接元素


# #### 分组可视化

# In[58]:


# 先引入一下作图相关的库，以及解决字体和负号问题的代码
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']#['Eras Bold ITC']# ['DengXian'] # ['cmtt10'] #['SimSun-ExtB']# ['Microsoft PhagsPa'] ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问


# 假设我们有2个班学生的英语和数学考试成绩：

# In[60]:


# 生成12个月的产品销量数据
df = pd.DataFrame()
df['month'] = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['A'] = np.random.randint(100, 1000, size=12)
df['B'] = np.random.randint(100, 1000, size=12)


# In[64]:


df#.set_index('month').groupby('B').plot()


# In[25]:


mean2 = 75  # 第二列成绩的均值
std2 = 8  # 第二列成绩的标准差
scores2 = np.random.normal(mean2, std2, 1000)


np.round(scores2).astype(int)  # 取整


# In[35]:


# np.round(np.random.normal(80 , 10, 1000)).astype(int)


# In[49]:


import pandas as pd
np.random.seed(0)
df = pd.DataFrame({'学生ID':list(range(1,101)),
                   '班级': np.random.choice([1, 2], size=100),
                   '英语': np.round(np.random.normal(80 , 10, 100)).astype(int),# 取整
                   '数学': np.round(np.random.normal(80 , 10, 100)).astype(int)})
df


# In[54]:


df.set_index('学生ID').groupby('班级').plot()


# In[55]:


df[['班级','英语','数学']].set_index('班级').groupby('班级').hist()


# In[45]:


df[['班级','英语','数学']].set_index('班级').groupby('班级').boxplot()


# ## Pandas 数据重塑

# ### 数据重塑(Reshaping)

# 数据重塑，顾名思义就是给数据做各种变形，主要有以下几种：
# - df.pivot 数据变形
# - df.pivot_table 数据透视表
# - df.stack/unstack 数据堆叠
# - df.melt  数据融合
# - df.cross 数据交叉表

# ### df.pivot( )  数据变形
# 
# > 根据索引（index）、列（column）（values）值)， 对原有DataFrame(数据框)进行变形重塑,俗称长表转宽表

# In[496]:


import pandas as pd
import numpy as np


# In[498]:


df = pd.DataFrame(
    { '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
     '科目': ['语文', '数学', '英语', '语文', '数学', '英语'],
     '成绩': [91, 80, 100, 80, 100, 96]})
df


# 长转宽：使用 `df.pivot` 以`姓名`为`index`,以各`科目`为`columns`，来统计各科成绩：

# In[527]:


df = pd.DataFrame(
    { '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
     '科目': ['语文', '数学', '英语', '语文', '数学', '英语'],
     '成绩': [91, 80, 100, 80, 100, 96]})
df


# In[528]:


df.pivot(index='姓名', columns='科目', values='成绩')


# ### pd.melt() 数据融合

# In[530]:


df = pd.DataFrame(
    { '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
     '科目': ['语文', '数学', '英语', '语文', '数学', '英语'],
     '成绩': [91, 80, 100, 80, 100, 96]})
df1 = pd.pivot(df, index='姓名', columns='科目', values='成绩').reset_index()
df1


# 宽表变长表：使用 `df.pivot` 以`姓名`为标识变量的列`id_vars`,以各`科目`为`value_vars`，来统计各科成绩：

# In[531]:


df1.melt(id_vars=['姓名'], value_vars=['数学', '英语', '语文'])


# ### pd.pivot_table() 数据透视

# In[532]:


random.seed(1024)
df = pd.DataFrame(
    {'专业': np.repeat(['数学与应用数学', '计算机', '统计学'], 4),
     '班级': ['1班','1班','2班','2班']*3,
     '科目': ['高数', '线代'] * 6,
     '平均分': [random.randint(60,100) for i in range(12)],
     '及格人数': [random.randint(30,50) for i in range(12)]})
df


# 各个专业对应科目的及格人数和平均分

# In[533]:


pd.pivot_table(df, index=['专业','科目'],
               values=['及格人数','平均分'],
               aggfunc={'及格人数':np.sum,"平均分":np.mean})


# 补充说明：

# `df.pivot_table()`和`df.pivot()`都是Pandas中用于将长表转换为宽表的方法，但它们在使用方式和功能上有一些区别。
# 
# 1. 使用方式：
#    - `df.pivot()`方法接受三个参数：`index`、`columns`和`values`，分别指定新表的索引、列和值。
#    - `df.pivot_table()`方法接受多个参数，其中最重要的是`index`、`columns`和`values`，用于指定新表的索引、列和值。此外，还可以使用`aggfunc`参数指定对重复值进行聚合操作的函数，默认为均值。
# 
# 2. 处理重复值：
#    - `df.pivot()`方法在长表中存在重复值时会引发错误。因此，如果长表中存在重复值，就需要先进行去重操作，或者使用其他方法来处理重复值。
#    - `df.pivot_table()`方法可以在长表中存在重复值的情况下进行透视操作，并可以使用`aggfunc`参数指定对重复值进行聚合操作的函数，默认为均值。
# 
# 3. 聚合操作：
#    - `df.pivot()`方法不支持对重复值进行聚合操作，它只是简单地将长表中的数据转换为宽表。
#    - `df.pivot_table()`方法支持对重复值进行聚合操作。可以使用`aggfunc`参数来指定聚合函数，例如求均值、求和、计数等。
# 
# 总的来说，`df.pivot()`方法适用于长表中不存在重复值的情况，而`df.pivot_table()`方法适用于长表中存在重复值的情况，并且可以对重复值进行聚合操作。根据具体的数据结构和分析需求，选择合适的方法来进行转换操作。

# ### 数据堆叠(Stack/Unstack)
# 
# 参阅[stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack)

# In[534]:


df = pd.DataFrame({'专业': np.repeat(['数学与应用数学', '计算机', '统计学','物理学'], 6),
                   '班级': ['1班','2班','3班']*8,
                   '科目': ['高数', '线代'] * 12,
                   '平均分': [random.randint(60,100) for i in range(24)],
                   '及格人数': [random.randint(30,50) for i in range(24)]})

df2 = pd.pivot_table(df, index=['专业','科目'],  values=['及格人数','平均分'],
               aggfunc={'及格人数':np.sum,"平均分":np.mean})
df2


# In[535]:


stacked = df2.stack()


# “压缩”后的DataFrame或Series(具有MultiIndex作为索引)， [stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack) 的逆操作是[unstack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack)，默认情况下取消最后压缩的那个级别：

# 堆叠`stack()`，顾名思义就是把透视结果堆到一起。接下来我们把透视后堆叠的数据一步步展开`unstack()`：

# In[541]:


stacked.unstack()


# In[542]:


stacked.unstack(level=1)


# In[543]:


stacked.unstack(level=0)


# ### 数据交叉表（pd.crosstab）

# 交叉表显示了每个变量的不同类别组合中观察到的频率或计数。通俗地说，就是根据不同列的数据统计了频数

# In[65]:


df = pd.DataFrame(
    { 'High':  ["高", "高", "高", "中", "中", "中", "低", "低", "低", "高", "低"],
     'Weight': ["重", "轻", "中", "中", "轻", "重", "重", "轻", "中", "重", "轻"]
    })
df


# In[546]:


pd.crosstab(df['High'], df['Weight']) 


# 双层`crosstab`

# In[488]:


df = pd.DataFrame(
    { 'High':  ["高", "高", "高", "中", "中", "中", "低", "低", "低", "高", "低"],
     'Weight': ["重", "轻", "中", "中", "轻", "重", "重", "轻", "中", "重", "轻"],
     'Size':   ["大", "中", "小", "中", "中", "大", "中", "小", "小", "大", "小"]})
df


# In[489]:


pd.crosstab(df['High'], [df['Weight'], df['Size']], rownames=['High'], colnames=['Weight', 'Size']) 


# 另一种 宽表转长表 pd.wide_to_long() 

# In[548]:


np.random.seed(123)
df = pd.DataFrame({"A1970" : {0 : "a", 1 : "b", 2 : "c"},
                   "A1980" : {0 : "d", 1 : "e", 2 : "f"},
                   "B1970" : {0 : 2.5, 1 : 1.2, 2 : .7},
                   "B1980" : {0 : 3.2, 1 : 1.3, 2 : .1},
                   "X"     : dict(zip(range(3), np.random.randn(3)))
                  })
df["id"] = df.index
df


# 把`id` 列用作标识列

# In[551]:


pd.wide_to_long(df, ["A", "B"], i="id", j="year")


# In[552]:


df = pd.DataFrame({
    'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'ht1': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
    'ht2': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]
})
df


# 把`famid`, `birth` 两列用作标识列

# In[554]:


l = pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age')
l


# In[34]:


df=pd.DataFrame（{'姓名':['张三','张三','张三','李四','李四','李四'],'科目': ['语文','数学','英语','语文','数学','英语']}）


# In[37]:


df=pd.DataFrame({'姓名':['张三','张三','张三','李四','李四','李四'],'科目': ['语文','数学','英语','语文','数学','英语']})
df


# In[ ]:





# In[81]:


import pandas as pd

# 创建示例数据
data = {'Student': ['Alice', 'Bob', 'Alice', 'Bob', 'Charlie', 'Charlie'],
        'Subject': ['Math', 'Math', 'English', 'English', 'Math', 'English'],
        'Score': [85, 90, 88, 75, 92, 80]}
df = pd.DataFrame(data)


# In[82]:


df


# In[83]:


df.groupby(['Subject']).transform('mean')


# In[84]:


df.groupby(['Subject']).apply(np.mean)


# In[ ]:




