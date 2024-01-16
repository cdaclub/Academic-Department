# 《Python数据分析极简入门》

## 第3节 10 Pandas 时序数据

在Pandas中，时间序列（Time Series）是一种特殊的数据类型，用于处理时间相关的数据。Pandas提供了丰富的功能和方法，方便对时间序列数据进行处理和分析。下面是一些针对时间序列的常用操作：

#### 创建时间序列数据

方式① 使用`to_datetime`创建时间序列：直接传入列表即可


```python
import pandas as pd

# 将列表转换为时间戳
date_range = pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03'])
date_range
```




    DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03'], dtype='datetime64[ns]', freq=None)



方式② 使用`pd.date_range()`创建一段连续的时间范围：使用指定参数即可


```python
import pandas as pd
date_range = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
date_range
```




    DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
                   '2024-01-05', '2024-01-06', '2024-01-07', '2024-01-08',
                   '2024-01-09', '2024-01-10',
                   ...
                   '2024-12-22', '2024-12-23', '2024-12-24', '2024-12-25',
                   '2024-12-26', '2024-12-27', '2024-12-28', '2024-12-29',
                   '2024-12-30', '2024-12-31'],
                  dtype='datetime64[ns]', length=366, freq='D')



其中，start是起始日期，end是结束日期，freq是频率，这里设置为'D'表示每天。

方式③ 使用`Timestamp()`函数创建一个特定的时间戳：使用指定参数即可


```python
import pandas as pd

timestamp = pd.Timestamp(year=2023, month=1, day=1, hour=12, minute=30, second=45)
timestamp
```




    Timestamp('2023-01-01 12:30:45')



方式④ 使用 datetime 模块创建时间戳：使用指定参数即可


```python
import pandas as pd
from datetime import datetime

timestamp = datetime(2023, 1, 1, 12, 30, 45)
print(timestamp)
```

    2023-01-01 12:30:45


#### 时长数据计算

计算一下两个时间数据之差


```python
import pandas as pd

# 创建两个固定时间
start_time = pd.Timestamp('2024-01-01 12:00:00')
end_time = pd.Timestamp('2024-01-02 14:30:00')

# 计算时间差
time_diff = end_time - start_time
time_diff 
```




    Timedelta('1 days 02:30:00')



一个固定时间加上`pd.Timedelta`类型的时间差


```python
pd.Timestamp('2024-01-02 14:30:00')+pd.Timedelta('1 days 02:30:00')
```




    Timestamp('2024-01-03 17:00:00')



#### 时序索引

接下来，我们看看日期做索引的情况

将日期作为索引创建时间序列：


```python
import pandas as pd
data = [1, 2, 3, 4, 5]
dates = pd.date_range(start='2024-01-01', periods=5, freq='D')
ts = pd.Series(data, index=dates)
ts
```




    2024-01-01    1
    2024-01-02    2
    2024-01-03    3
    2024-01-04    4
    2024-01-05    5
    Freq: D, dtype: int64



其中，periods是时间序列的长度，freq是频率，这里设置为'D'表示每天。

时间序列的索引和切片：
使用日期进行索引：


```python
import pandas as pd
ts['2024-01-01']
```




    1



使用日期范围进行切片：


```python
import pandas as pd
ts['2024-01-01':'2024-01-05']
```




    2024-01-01    1
    2024-01-02    2
    2024-01-03    3
    2024-01-04    4
    2024-01-05    5
    Freq: D, dtype: int64



也可以使用切片操作对数据进行访问


```python
import pandas as pd
ts[1:4]
```




    2024-01-02    2
    2024-01-03    3
    2024-01-04    4
    Freq: D, dtype: int64



时间序列的重采样：
将时间序列从高频率转换为低频率：


```python
import pandas as pd
ts.resample('W').mean()
```




    2024-01-07    3.0
    Freq: W-SUN, dtype: float64



其中，'W'表示按周进行重采样，mean()表示计算每周的平均值。

时间序列的滚动计算：
计算滚动平均值：


```python
import pandas as pd
ts.rolling(window=3).mean()
```




    2024-01-01    NaN
    2024-01-02    NaN
    2024-01-03    2.0
    2024-01-04    3.0
    2024-01-05    4.0
    Freq: D, dtype: float64



其中，window=3表示窗口大小为3，即计算每3个数据的平均值。

时间序列的时间偏移：
将时间序列向前或向后移动：


```python
import pandas as pd
ts.shift(1)
```




    2024-01-01    NaN
    2024-01-02    1.0
    2024-01-03    2.0
    2024-01-04    3.0
    2024-01-05    4.0
    Freq: D, dtype: float64



其中，1表示向后移动1个时间单位。

#### 时间访问器dt

在 Pandas 中，可以使用 dt 访问器来访问时间戳或时间序列中的各个时间部分，例如年、月、日、小时、分钟、秒等。通过使用 dt 访问器，你可以方便地提取和操作时间信息。

下面是一些常用的 dt 访问器的示例：


```python
import pandas as pd

# 创建一个时间序列
timestamps = pd.Series(pd.date_range('2023-01-01', periods=5, freq='D'))
timestamps
```




    0   2023-01-01
    1   2023-01-02
    2   2023-01-03
    3   2023-01-04
    4   2023-01-05
    dtype: datetime64[ns]




```python
# 提取年份
year = timestamps.dt.year
year
```




    0    2023
    1    2023
    2    2023
    3    2023
    4    2023
    dtype: int64




```python
# 提取月份
month = timestamps.dt.month
month
```




    0    1
    1    1
    2    1
    3    1
    4    1
    dtype: int64




```python
# 提取日期
day = timestamps.dt.day
day
```




    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64




```python
# 提取小时
hour = timestamps.dt.hour
hour
```




    0    0
    1    0
    2    0
    3    0
    4    0
    dtype: int64




```python
# 提取分钟
minute = timestamps.dt.minute
minute
```




    0    0
    1    0
    2    0
    3    0
    4    0
    dtype: int64




```python
# 提取秒数
second = timestamps.dt.second
second
```




    0    0
    1    0
    2    0
    3    0
    4    0
    dtype: int64




```python
# 获取季度
quarter = timestamps.dt.quarter
quarter
```




    0    1
    1    1
    2    1
    3    1
    4    1
    dtype: int64




```python
# 获取周数
week = timestamps.dt.isocalendar().week
week
```




    0    52
    1     1
    2     1
    3     1
    4     1
    Name: week, dtype: UInt32




```python
# 获取星期几的名称
day_name = timestamps.dt.day_name()
day_name
```




    0       Sunday
    1       Monday
    2      Tuesday
    3    Wednesday
    4     Thursday
    dtype: object




```python
# 获取该日期是一年中的第几天
day_of_year = timestamps.dt.dayofyear
day_of_year
```




    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64




```python
# 获取该日期是一周中的第几天（星期一为1，星期日为7）
day_of_week = timestamps.dt.dayofweek + 1
day_of_week
```




    0    7
    1    1
    2    2
    3    3
    4    4
    dtype: int64




```python
# 获取该日期是一个月中的第几天
day_of_month = timestamps.dt.day
day_of_month
```




    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64




```python
# 获取该日期所在月份的最后一天
end_of_month = timestamps.dt.daysinmonth
end_of_month
```




    0    31
    1    31
    2    31
    3    31
    4    31
    dtype: int64



#### 时长转化


```python
import pandas as pd

# 创建时间戳序列
ts = pd.Series(pd.to_timedelta(np.arange(10),unit='m'))
ts
```




    0   0 days 00:00:00
    1   0 days 00:01:00
    2   0 days 00:02:00
    3   0 days 00:03:00
    4   0 days 00:04:00
    5   0 days 00:05:00
    6   0 days 00:06:00
    7   0 days 00:07:00
    8   0 days 00:08:00
    9   0 days 00:09:00
    dtype: timedelta64[ns]




```python
# 提取时间戳中的秒数
seconds = ts.dt.seconds
seconds
```




    0      0
    1     60
    2    120
    3    180
    4    240
    5    300
    6    360
    7    420
    8    480
    9    540
    dtype: int64




```python
seconds = ts.dt.to_pytimedelta()
seconds
```




    array([datetime.timedelta(0), datetime.timedelta(seconds=60),
           datetime.timedelta(seconds=120), datetime.timedelta(seconds=180),
           datetime.timedelta(seconds=240), datetime.timedelta(seconds=300),
           datetime.timedelta(seconds=360), datetime.timedelta(seconds=420),
           datetime.timedelta(seconds=480), datetime.timedelta(seconds=540)],
          dtype=object)



以上是Pandas针对时间序列的一些常用操作和示例代码