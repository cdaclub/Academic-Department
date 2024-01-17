#!/usr/bin/env python
# coding: utf-8

# ## Pandas 文本数据

# Pandas提供了许多用于处理文本数据的功能。下面是一些常用的 Pandas 文本数据处理功能：

# In[278]:


import pandas as pd


# #### 1、cat() 拼接字符串 

# In[279]:


d = pd.DataFrame(['a', 'b', 'c'],columns = ['A'])
d


# 将某列元素拼接一列特定字符串

# In[280]:


d['A'].str.cat(['A', 'B', 'C'], sep=',')


# 将某列的元素合并为一个字符串

# In[281]:


d['A'].str.cat(sep=',')


# #### 2、split() 切分字符串 

# In[282]:


import numpy as np
import pandas as pd
d = pd.DataFrame(['a_b_c', 'c_d_e', np.nan, 'f_g_h'],columns = ['A'])
d


# 将某列的字符串元素进行切分

# In[283]:


d['A'].str.split('_')


# #### 3、get() 获取指定位置的字符串 

# In[284]:


d = pd.DataFrame(['a_b_c', 'c_d_e', np.nan, 'f_g_h'],columns = ['A'])
d['A']


# In[285]:


d['A'].str.get(2)


# #### 4、join() 对每个字符都用给定的字符串拼接起来（不常用） 

# In[286]:


d = pd.DataFrame(['a_b_c', 'c_d_e', np.nan, 'f_g_h'],columns = ['A'])
d['A']


# In[287]:


d['A'].str.join("!")


# #### 5、contains() 是否包含表达式 （很常用）

# In[288]:


d['A'].str.contains('d')


# In[289]:


d.fillna('0')[d.fillna('0')['A'].str.contains('d')]


# In[290]:


d.fillna('0')[d['A'].fillna('0').str.contains('d|e')]

#表示或的关系用"A|B"，表示且用'A.*B|B.*A'


# #### 6、replace() 替换 

# In[291]:


d['A'].str.replace("_", ".")


# #### 7、repeat() 重复 

# In[292]:


d['A'].str.repeat(3)


# #### 8、pad() 左右补齐 

# In[293]:


d['A'].str.pad(10, fillchar="0")


# In[294]:


d['A'].str.pad(10, side="right", fillchar="?")


# #### 9、center() 中间补齐

# In[295]:


d['A'].str.center(10, fillchar="?")


# #### 10、ljust() 右边补齐

# In[296]:


d['A'].str.ljust(10, fillchar="?")


# #### 11、rjust() 左边补齐

# In[297]:


d['A'].str.rjust(10, fillchar="?")


# #### 12、zfill() 左边补0 

# In[298]:


d['A'].str.zfill(10)


# #### 13、wrap() 在指定的位置加回车符号 

# In[299]:


d['A'].str.wrap(3)


# #### 14、slice() 按给定点的开始结束位置切割字符串 

# In[300]:


d['A'].str.slice(1,3)


# #### 15、slice_replace() 使用给定的字符串，替换指定的位置的字符 

# In[301]:


d['A'].str.slice_replace(1, 3, "?")


# #### 16、count() 计算给定单词出现的次数 

# In[302]:


d['A'].str.count("b")


# #### 17、startswith() 判断是否以给定的字符串开头 

# In[303]:


d['A'].str.startswith("a")


# #### 18、endswith() 判断是否以给定的字符串结束

# In[304]:


d['A'].str.endswith("e")


# #### 19、findall() 查找所有符合正则表达式的字符，以数组形式返回 

# In[305]:


d['A'].str.findall("[a-z]")


# #### 20、match() 检测是否全部匹配给点的字符串或者表达式 

# In[306]:


d['A'].str.match("[d-z]")


# #### 21、extract() 抽取匹配的字符串出来，注意要加上括号，把你需要抽取的东西标注上 

# In[307]:


d['A'].str.extract("([d-z])")


# #### 22、len() 计算字符串的长度 

# In[308]:


d['A'].str.len()


# #### 23、strip() 去除前后的空白字符 

# In[309]:


df = pd.DataFrame(['a_b  ', '  d_e  ', np.nan, 'f_g  '],columns = ['B'])
df['B']


# In[310]:


df['B'].str.strip()


# #### 24、rstrip() 去除后面的空白字符 

# In[311]:


df['B'].str.rstrip()


# #### 25、lstrip() 去除前面的空白字符 

# In[312]:


df['B'].str.lstrip()


# #### 26、partition() 把字符串数组切割称为DataFrame，注意切割只是切割称为三部分，分隔符前，分隔符，分隔符后 

# In[313]:


d['A'] .str.partition('_')


# #### 27、rpartition() 从右切起 

# In[314]:


d['A'].str.rpartition('_')


# #### 28、lower() 全部小写 

# In[315]:


d['A'].str.lower() 


# #### 29、upper() 全部大写 

# In[316]:


d['A'].str.upper() 


# #### 30、find() 从左边开始，查找给定字符串的所在位置 

# In[317]:


d['A'].str.find('d')


# #### 31、rfind() 从右边开始，查找给定字符串的所在位置 

# In[318]:


d['A'].str.rfind('d')


# #### 32、index() 查找给定字符串的位置，注意，如果不存在这个字符串，那么会报错！ 

# In[319]:


d['A'].str.index('_')


# #### 33、rindex() 从右边开始查找，给定字符串的位置 

# In[320]:


d['A'].str.rindex('_')


# #### 34、capitalize() 首字符大写 

# In[321]:


d['A'].str.capitalize()


# #### 35、swapcase() 大小写互换 

# In[322]:


d['A'].str.capitalize()


# #### 36、isalnum() 是否全部是数字和字母组成 

# In[323]:


d['A'].str.isalnum()


# #### 37、isalpha() 是否全部是字母 

# In[324]:


d['A'].str.isalpha()


# #### 38、isdigit() 是否全部都是数字 

# In[325]:


d['A'].str.isdigit()


# #### 39、isspace() 是否空格 

# In[326]:


d['A'].str.isspace()


# #### 40、islower() 是否全部小写 

# In[327]:


d['A'].str.islower()


# #### 41、isupper() 是否全部大写 

# In[328]:


d['A'].str.isupper()


# #### 42、istitle() 是否只有首字母为大写，其他字母为小写 

# In[329]:


d['A'].str.istitle()


# #### 43、isnumeric() 是否是数字 

# In[330]:


d['A'].str.isnumeric()


# #### 44、isdecimal() 是否全是数字 

# In[331]:


d['A'].str.isdecimal()


# ## Pandas 时序数据

# 在Pandas中，时间序列（Time Series）是一种特殊的数据类型，用于处理时间相关的数据。Pandas提供了丰富的功能和方法，方便对时间序列数据进行处理和分析。下面是一些针对时间序列的常用操作：

# #### 创建时间序列数据

# 方式① 使用`to_datetime`创建时间序列：直接传入列表即可

# In[332]:


import pandas as pd

# 将列表转换为时间戳
date_range = pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03'])
date_range


# 方式② 使用`pd.date_range()`创建一段连续的时间范围：使用指定参数即可

# In[333]:


import pandas as pd
date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
date_range


# 其中，start是起始日期，end是结束日期，freq是频率，这里设置为'D'表示每天。

# 方式③ 使用`Timestamp()`函数创建一个特定的时间戳：使用指定参数即可

# In[334]:


import pandas as pd

timestamp = pd.Timestamp(year=2023, month=1, day=1, hour=12, minute=30, second=45)
timestamp


# 方式④ 使用 datetime 模块创建时间戳：使用指定参数即可

# In[335]:


import pandas as pd
from datetime import datetime

timestamp = datetime(2023, 1, 1, 12, 30, 45)
print(timestamp)


# #### 时长数据计算

# 计算一下两个时间数据之差

# In[336]:


import pandas as pd

# 创建两个固定时间
start_time = pd.Timestamp('2024-01-01 12:00:00')
end_time = pd.Timestamp('2024-01-02 14:30:00')

# 计算时间差
time_diff = end_time - start_time
time_diff 


# 一个固定时间加上`pd.Timedelta`类型的时间差

# In[337]:


pd.Timestamp('2024-01-02 14:30:00')+pd.Timedelta('1 days 02:30:00')


# #### 时序索引

# 接下来，我们看看日期做索引的情况
# 
# 将日期作为索引创建时间序列：

# In[338]:


import pandas as pd
data = [1, 2, 3, 4, 5]
dates = pd.date_range(start='2024-01-01', periods=5, freq='D')
ts = pd.Series(data, index=dates)
ts


# 其中，periods是时间序列的长度，freq是频率，这里设置为'D'表示每天。
# 
# 时间序列的索引和切片：
# 使用日期进行索引：

# In[339]:


import pandas as pd
ts['2024-01-01']


# 使用日期范围进行切片：

# In[340]:


import pandas as pd
ts['2024-01-01':'2024-01-05']


# 也可以使用切片操作对数据进行访问

# In[341]:


import pandas as pd
ts[1:4]


# 时间序列的重采样：
# 将时间序列从高频率转换为低频率：

# In[342]:


import pandas as pd
ts.resample('W').mean()


# 其中，'W'表示按周进行重采样，mean()表示计算每周的平均值。
# 
# 时间序列的滚动计算：
# 计算滚动平均值：

# In[343]:


import pandas as pd
ts.rolling(window=3).mean()


# 其中，window=3表示窗口大小为3，即计算每3个数据的平均值。
# 
# 时间序列的时间偏移：
# 将时间序列向前或向后移动：

# In[344]:


import pandas as pd
ts.shift(1)


# 其中，1表示向后移动1个时间单位。

# #### 时间访问器dt

# 在 Pandas 中，可以使用 dt 访问器来访问时间戳或时间序列中的各个时间部分，例如年、月、日、小时、分钟、秒等。通过使用 dt 访问器，你可以方便地提取和操作时间信息。
# 
# 下面是一些常用的 dt 访问器的示例：

# In[345]:


import pandas as pd

# 创建一个时间序列
timestamps = pd.Series(pd.date_range('2023-01-01', periods=5, freq='D'))
timestamps


# In[346]:


# 提取年份
year = timestamps.dt.year
year


# In[347]:


# 提取月份
month = timestamps.dt.month
month


# In[348]:


# 提取日期
day = timestamps.dt.day
day


# In[349]:


# 提取小时
hour = timestamps.dt.hour
hour


# In[350]:


# 提取分钟
minute = timestamps.dt.minute
minute


# In[351]:


# 提取秒数
second = timestamps.dt.second
second


# In[352]:


# 获取季度
quarter = timestamps.dt.quarter
quarter


# In[355]:


# 获取周数
week = timestamps.dt.isocalendar().week
week


# In[356]:


# 获取星期几的名称
day_name = timestamps.dt.day_name()
day_name


# In[357]:


# 获取该日期是一年中的第几天
day_of_year = timestamps.dt.dayofyear
day_of_year


# In[358]:


# 获取该日期是一周中的第几天（星期一为1，星期日为7）
day_of_week = timestamps.dt.dayofweek + 1
day_of_week


# In[359]:


# 获取该日期是一个月中的第几天
day_of_month = timestamps.dt.day
day_of_month


# In[360]:


# 获取该日期所在月份的最后一天
end_of_month = timestamps.dt.daysinmonth
end_of_month


# #### 时长转化

# In[362]:


import pandas as pd

# 创建时间戳序列
ts = pd.Series(pd.to_timedelta(np.arange(10),unit='m'))
ts


# In[363]:


# 提取时间戳中的秒数
seconds = ts.dt.seconds
seconds


# In[364]:


seconds = ts.dt.to_pytimedelta()
seconds


# 以上是Pandas针对时间序列的一些常用操作和示例代码

# ## Pandas 窗口数据

# Pandas提供了窗口函数（Window Functions）用于在数据上执行滑动窗口操作，可以对数据进行滚动计算、滑动统计等操作。下面是一些常用的窗口函数：
# 
# 滚动计算函数：
# 移动平均值（Moving Average）：

# In[365]:


import pandas as pd
data = {'column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)
df


# In[366]:


df['MA'] = df['column'].rolling(window=3).mean()
df


# 其中，window=3表示窗口大小为3，即计算每3个数据的平均值。
# 
# 滚动求和（Rolling Sum）：

# In[367]:


import pandas as pd
df['Sum'] = df['column'].rolling(window=5).sum()
df


# 其中，window=5表示窗口大小为5，即计算每5个数据的和。
# 
# 滑动统计函数：
# 滑动最大值（Rolling Maximum）：

# In[368]:


import pandas as pd
df['Max'] = df['column'].rolling(window=7).max()
df


# 其中，window=7表示窗口大小为7，即计算每7个数据的最大值。
# 
# 滑动最小值（Rolling Minimum）：

# In[369]:


import pandas as pd
df['Min'] = df['column'].rolling(window=7).min()
df


# 其中，window=7表示窗口大小为7，即计算每7个数据的最小值。
# 
# 滑动标准差（Rolling Standard Deviation）：

# In[370]:


import pandas as pd
df['Std'] = df['column'].rolling(window=5).std()
df


# 其中，window=5表示窗口大小为5，即计算每5个数据的标准差。
# 
# 自定义窗口函数：
# 可以使用rolling().apply()方法来应用自定义的窗口函数：

# In[371]:


import pandas as pd

def custom_function(data):
    # 自定义的窗口函数逻辑
    return max(data) - min(data)

df['Result'] =df['column'].rolling(window=3).apply(custom_function)
df


# 其中，custom_function是自定义的窗口函数，data是窗口中的数据，result是窗口函数的计算结果。
# 以上是Pandas窗口函数的一些常用操作和示例代码。需要注意的是，在使用窗口函数时，需要根据实际需求选择合适的窗口大小和窗口函数，并确保数据的顺序和窗口大小的一致性。

# ## Pandas 数据读写

# Pandas提供了多种读取数据的方法，包括读取CSV、Excel、SQL数据库等。

# #### CSV

# 写出`csv`文件

# In[372]:


import pandas as pd
import numpy as np

data = np.random.rand(10, 10)  # 生成一个10行10列的随机数矩阵
columns = ['col' + str(i) for i in range(10)]  # 列名为col0, col1, ..., col9

df = pd.DataFrame(data, columns=columns)
df


# In[373]:


df.to_csv('./output/foo.csv')  # 请注意需要在你的代码文件夹目录下建一个\output 文件夹才能写入


# 读入刚刚写出的文件

# In[374]:


pd.read_csv('./output/foo.csv')


# ### EXCEL

# 写出`excel`文件

# In[375]:


df.to_excel('./output/foo.xlsx', sheet_name='Sheet1',index = None)


# 读取`excel`文件

# In[376]:


pd.read_excel('./output/foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])


# #### HDF

# 写出`hdf`文件

# In[377]:


df.to_hdf('./output/foo.h5','df')


# 读入刚刚写出的文件

# In[378]:


pd.read_hdf('./output/foo.h5','df').head()


# #### MySQL

# 写出到mysql里

# In[379]:


from sqlalchemy import create_engine
import pandas as pd


# In[382]:


mysql_engine=create_engine("mysql+pymysql://root:password@localhost/test")
df.to_sql(pust_table_name,mysql_engine,if_exists='replace',index =  False) #  注意 mysql_engine一定要正确配置


# 读入刚刚写出的文件

# In[383]:


df = pd.read_sql("""
select a,b
from pust_table_name;
""",mysql_engine) # 再次强调，mysql_engine一定要正确配置，实在有问题可以私信 aiu_cda
df


# ## Pandas 表格样式

# Pandas 的样式是一个可视化的方法，像Excel一样对特定数据进行加粗、标红、背景标黄等，为了让数据更加清晰醒目，突出数据的逻辑和特征。

# 假如我们有这样一个`DataFrame`，我们需要通过表格样式给它做各种标注：

# In[622]:


#读取数据
import pandas as pd
import numpy as np
df = df = pd.DataFrame(
    {'A': ['孙云', '郑成', '冯敏', '王忠', '郑花', '孙华', '赵白', '王花', '黄成', '钱明', '孙宇'],
     'B': [79, 70, 39, 84, 87, 26, 29, 47, 32, 22, 99],
     'C': [28, 77, 84, 26, 29, 47, 32, 22, 99, 76, 44],
     'D': [18, 53, 78, 4, 36, 88, 79, 47, 54, 25, 14]})
df


# #### 字体颜色

# 首先来看一个对文字标注颜色的例子：eg.我们想把成绩超过80的分数用红色标注出来
# 
# 我们需要先定义一个函数，根据条件返回不同的颜色

# In[623]:


def color_negative_red(val):
    color = 'red' if val > 80 else 'black'
    return 'color: %s' % color


# 应用这个自定义函数后就可以得到：

# In[624]:


df.set_index('A').style.applymap(color_negative_red)


# #### 背景高亮

# 接着 eg. 我们假设有学生没有去考试，想看看哪些学生没有考试，把这部分进行背景高亮显示

# 数据如下：

# In[407]:


df1 = df.copy()
df1.iloc[1,1] = np.NaN
df1.iloc[2,1] = np.NaN
df1


# 换句话说，就是用背景高亮标记出空值，应用`.highlight_null() `即可将空值高亮显示,同时用`null_color`参数可以指定该高亮的颜色。

# In[408]:


#把空值设置高亮

df1.style.highlight_null(null_color = 'blue'#修改颜色
                       )


# #### 极值背景高亮

# 接着我们想看看 eg. 标记出每个科目的最高分数

# 换句话说，需要查找DataFrame每一列的最大值，通过 highlight_max() 方法用于将最大值高亮显示，并通过color参数修改高亮颜色

# In[409]:


#设置极大值高亮
df.set_index('A').style.highlight_max(color = 'red'#修改颜色
                      )


# 通过 `highlight_min()` 方法可以将最小值高亮显示

# In[427]:


df.set_index('A').style.highlight_min(color = 'yellow' #修改颜色
)


# 同时显示极大值和极小值，并使用指定颜色：通过 `highlight_min()` 方法和  `highlight_max()` 方法再指定一下颜色即可

# In[428]:


df.set_index('A').style.highlight_min(color = 'green').highlight_max(color = 'red')


# #### 横向对比

# 再来看看横向对比的例子 eg. 需要标记出每个学生的单科最高分数: 通过参数 axis ，横向对比大小，并把最大值进行高亮显示即可

# In[432]:


df.set_index('A').style.highlight_max(axis = 1)


# 同样的，也可以通过参数 subset ，选定一列对最大值进行高亮显示

# In[435]:


#指定列进行比较
df.set_index('A').style.highlight_max(subset = ['B'])


# #### 背景渐变

# eg. 用不同的颜色来标注成绩，背景颜色越深，成绩越高

# 通过调用 background_gradient() 方法，从而创建一个渐变的背景效果。

# In[436]:


df.style.background_gradient()


# 同样地，针对单个列，指定颜色系列如下：

# In[437]:


df.style.background_gradient(subset = ['B'],cmap = 'BuGn')


# 刚才我们是默认颜色渐变的范围了，接着我们来看如何指定颜色渐变的范围，来展现成绩的高低

# 通过调用 `background_gradient()` 方法，用了两个参数 low=0.5 和 high=0 表示渐变的起始值和结束值

# In[438]:


#低百分比和高百分比范围，更换颜色时避免使用所有色域
df.style.background_gradient(low = 0.5,high = 0)


# 接着我们看看如何对特定范围内的值就行标注

# eg. 假如需要把60分以上的分数用颜色标注出来

# 通过参数 vmin 和参数 vmax 设置渐变的最小值和最大值，就可以展现出来。

# In[442]:


df.style.background_gradient(vmin = 60,vmax = 100)


# eg. 用此次考试成绩表，添加标题

# 通过.set_caption() 方法为DataFrame 即可设置标题。

# In[443]:


#添加标题
df.style.set_caption("三年级二班学生成绩表")


# 通过以上内容的学习，我们快速学习Pandas样式的基本操作，接下来，再用两个案例详细说明一下

# 案例一：将科目分数小于60的值，用红色进行高亮显示

# In[445]:


#将学生没有及格的科目标记为红色
df.style.applymap(lambda x: 'background-color:red' if x<60 else '', subset = pd.IndexSlice[:,['B','C','D']])


# 案例二：标记总分低于120分的分数

# 将每个学生的分数，进行加总和计算平均数，并保留两位小数,把分数低于120的学生，用红色进行标记即可

# In[450]:


#通过使用.assign() 来计算学生三门课程的总分和平均值
(df.set_index('A').assign(sum_s = df.set_index('A').sum(axis = 1))
    .style.applymap(lambda x: 'background-color:red' if x<120 else '',subset = pd.IndexSlice[:,['sum_s']])
    .format({'avg':"{:.2f}"}))


# ## Pandas 可视化

# > 一图胜千言 A picture is worth a thousand words.

# 常见的可视化图有如下几种：
# - line:折线图
# - pie:饼图
# - bar:柱状图
# - hist:直方图
# - box:箱型图
# - area:面积图
# - scatter：散点图

# In[543]:


#用于处理解决中文乱码问题和负号问题。
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文问题
plt.rcParams['axes.unicode_minus'] = False #显示负号


# #### line:折线图

# 折线图一般用于描述数据的**趋势**：

# In[571]:


import pandas as pd
import numpy as np
import random
df = pd.DataFrame({'A': ['a', 'b', 'c', 'd','e', 'f','g','h','i'],
                   'B': ['L', 'L', 'M', 'L','M', 'M','M','L','L'],
                   'C': [107, 177, 139, 38, 52, 38,87,38,56],
                   'D': [22, 59, 38, 59, 59, 82,89,48,88]}).set_index('A')
df


# 一组数据的折线图如下：

# In[572]:


df['C'].plot.line(
      )


# 再来看一下两组数据的折线图

# In[573]:


df[['C','D']].plot.line()


# #### pie:饼图

# 饼图一般用于展示数据的占比关系

# In[574]:


np.random.seed(123)
df1 = pd.Series(3*np.random.rand(4),index = ['a','b','c','d'],name = '占比')
df1


# 看看以上四个数据的占比情况

# In[575]:


df1.plot.pie()


# #### bar:柱状图

# 柱状图一般用于各种类型数据的对比。

# 一组数据的柱状图

# In[577]:


df['C'].plot.bar()


# 两组数据的柱状图

# In[578]:


df[['C','D']].plot.bar()


# 横向柱状图

# In[579]:


df.plot.barh()


# 其他几种柱状图

# In[580]:


df.assign(a = df.C- 70).plot.bar()


# In[581]:


df.plot.bar(stacked = True)


# In[582]:


df.plot.barh(stacked = True)


# In[583]:


df.head(5).plot.barh(stacked = True,colormap='cool')


# #### hist:直方图

# 直方图用于展示数据的分布情况

# In[616]:


np.random.seed(123)
df2 = pd.DataFrame({'a':np.random.randn(1000)+1,
                   'b':np.random.randn(1000),
                   'c':np.random.randn(1000)-1},
                  columns = ['a','b','c'])
df2


# 先来看下一组数据的直方图

# In[585]:


df2['a'].plot.hist()


# 多组数据的直方图

# In[586]:


df2.plot.hist()


# 指定分箱数量的直方图

# In[587]:


#堆叠，指定分箱数量
df2.plot.hist(stacked = True,bins = 30)


# #### box:箱型图

# 箱型图用于展示数据的分布、识别异常值以及比较不同组之间的差异。

# 一组数据的箱型图

# In[588]:


df.boxplot('C')


# 再来看看用两列数据来画两个箱型图

# In[589]:


import pandas as pd
import numpy as np
import random
df = pd.DataFrame({'A': ['a', 'b', 'c', 'd','e', 'f','g','h','i'],
                   'B': ['L', 'L', 'M', 'L','M', 'M','M','L','L'],
                   'C': [107, 177, 139, 38, 52, 38,87,38,56],
                   'D': [22, 59, 38, 59, 59, 82,89,48,88]}).set_index('A')
df


# In[590]:


df.boxplot(['C','D'])


# 横向箱线图

# In[592]:


df.boxplot(['C','D'],vert = False)


# #### area:面积图

# 面积图是一种常见且有效的数据可视化工具，用于展示数据的趋势、比较不同组之间的差异以及理解数据的部分与整体关系。广泛应用于统计学、经济学、市场调研、环境科学等领域，并为数据分析和决策提供了重要的支持。

# In[593]:


np.random.seed(123)
df4 = pd.DataFrame(np.random.rand(10,4),columns = ['a','b','c','d'])
df4


# 一组数据的面积图

# In[595]:


df4['a'].plot.area()


# 多组数据的面积图

# In[596]:


df4[['a','b','c','d']].plot.area()


# #### scatter：散点图

# 散点图用于发现变量之间的关系、探索异常情况、进行聚类分析以及支持预测和模型建立

# In[627]:


np.random.seed(123)
df = pd.DataFrame(np.random.randn(10,2),columns = ['B','C']).cumsum()
df


# 看一下这两列数据的散点图

# In[628]:


df.assign(avg = df.mean(1)).plot.scatter(x='C',y = 'B')


# **致谢**
# 
# 《Python数据分析极简入门》图文系列教程的写作过程中参考了诸多经典书籍，包括:
# 
# Wes McKinney 's 《Python for Data Analysis》;
# 
# 小甲鱼老师的《零基础入门学习Python》；
# 
# 李庆辉老师的 《深入浅出Pandas》;
# 
# 在此一并感谢以上内容的作者！
# 
# > 怕什么真理无穷,进一寸有一寸的欢喜。你每每往前进一寸，你的天空，便有一片新的明朗。你便会有一片新的开阔。诸位加油，我们下个系列见！

# In[ ]:




