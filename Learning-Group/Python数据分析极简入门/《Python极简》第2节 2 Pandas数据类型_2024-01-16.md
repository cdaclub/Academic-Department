# 《Python数据分析极简入门》
## 第2节 2 Pandas数据类型

Pandas 有两种自己独有的基本数据结构。需要注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以 Python 中有的数据类型在这里依然适用。我们分别看一下这两种数据结构：


#### Series

Series：一维数组。该结构能够放置各种数据类型，比如字符、整数、浮点数等

我们先引入pandas包，这里有一个约定成俗的写法`import pandas as pd` 将pandas引入，并命其别名为pd

接着将列表`[2,3,5,7,11]`放到pd.Series()里面


```python
import pandas as pd
s = pd.Series([2,3,5,7,11],name = 'A')
s
```




    0     2
    1     3
    2     5
    3     7
    4    11
    Name: A, dtype: int64



Time- Series：以时间为索引的Series

同样的，将列`['2024-01-01 00:00:00', '2024-01-01 03:00:00','2024-01-01 06:00:00']` 放到pd.DatetimeIndex()里面


```python
dts1 = pd.DatetimeIndex(['2024-01-01 00:00:00', '2024-01-01 03:00:00','2024-01-01 06:00:00'])
dts1
```




    DatetimeIndex(['2024-01-01 00:00:00', '2024-01-01 03:00:00',
                   '2024-01-01 06:00:00'],
                  dtype='datetime64[ns]', freq=None)



还有另外一种写法`pd.date_range` 可以按一定的频率生成时间序列


```python
dts2 = pd.date_range(start='2024-01-01', periods=6, freq='3H')
dts2
```




    DatetimeIndex(['2024-01-01 00:00:00', '2024-01-01 03:00:00',
                   '2024-01-01 06:00:00', '2024-01-01 09:00:00',
                   '2024-01-01 12:00:00', '2024-01-01 15:00:00'],
                  dtype='datetime64[ns]', freq='3H')




```python
dts3 = pd.date_range('2024-01-01', periods=6, freq='d')
dts3
```




    DatetimeIndex(['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04',
                   '2024-01-05', '2024-01-06'],
                  dtype='datetime64[ns]', freq='D')



#### DataFrame

DataFrame：二维的表格型数据结构,可以理解为Series的容器，通俗地说，就是可以把Series放到DataFrame里面。

它是一种二维表格型数据的结构，既有行索引，也有列索引。行索引是 index，列索引是 columns。类似于初中数学里，在二维平面里用坐标轴来定位平面中的点。


注意，DataFrame又是Pandas的核心!接下来的内容基本上以DataFrame为主

先来看看如何创建DataFrame，上面说过Series也好，DataFrame也罢，本质上都是容器。

千万别被”容器“这个词吓住了，通俗来说，就是里面可以放东西的东西。

**从字典创建DataFrame**

相当于给里面放dict：先创建一个字典`d`,再把`d`放进了`DataFrame`里命名为`df`


```python
d = {'A': [1, 2, 3], 
     'B': [4, 5, 6],
     'C': [7, 8, 9]}
df = pd.DataFrame(data = d)
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
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>5</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>6</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



**从列表创建DataFrame**

先创建了一个列表`d`,再把`d`放进了`DataFrame`里命名为`df`


```python
d = [[4, 7, 10],[5, 8, 11],[6, 9, 12]]
df1 = pd.DataFrame(
    data = d,
    index=['a', 'b', 'c'],
    columns=['A', 'B', 'C'])
df1
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>4</td>
      <td>7</td>
      <td>10</td>
    </tr>
    <tr>
      <th>b</th>
      <td>5</td>
      <td>8</td>
      <td>11</td>
    </tr>
    <tr>
      <th>c</th>
      <td>6</td>
      <td>9</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



**从数组创建DataFrame**

数组（array）对你来说可能是一个新概念，在Python里面，创建数组需要引入一个类似于Pandas的库，叫做Numpy。与前面引入Pandas类似，我们用 `import numpy as np`来引入numpy，命其别名为np。

同样的，先创建一个数组`d`,再把`d`放进了`DataFrame`里命名为`df`


```python
import numpy as np
d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df2 = pd.DataFrame(data = d,
                   index=['a', 'b', 'c'],
                   columns=['A', 'B', 'C'])
df2
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
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1</td>
      <td>2</td>
      <td>3</td>
    </tr>
    <tr>
      <th>b</th>
      <td>4</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>c</th>
      <td>7</td>
      <td>8</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



以上，我们用了不同的方式来创建DataFrame，接下来，我们看看创建好后，如何查看数据

---
