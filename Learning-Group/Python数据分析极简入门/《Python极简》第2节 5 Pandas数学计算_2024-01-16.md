# 《Python数据分析极简入门》

## 第2节 5 Pandas数学计算


```python
import pandas as pd
d =  np.array([[81, 28, 24, 25, 96],
       [ 8, 35, 56, 98, 39],
       [13, 39, 55, 36,  3],
       [70, 54, 69, 48, 12],
       [63, 80, 97, 25, 70]])
df = pd.DataFrame(data = d,
                  columns=list('abcde'))
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81</td>
      <td>28</td>
      <td>24</td>
      <td>25</td>
      <td>96</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>35</td>
      <td>56</td>
      <td>98</td>
      <td>39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>39</td>
      <td>55</td>
      <td>36</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>54</td>
      <td>69</td>
      <td>48</td>
      <td>12</td>
    </tr>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>80</td>
      <td>97</td>
      <td>25</td>
      <td>70</td>
    </tr>
  </tbody>
</table>
</div>



#### 聚合计算

聚合计算是指对数据进行汇总和统计的操作。常用的聚合计算方法包括计算均值、求和、最大值、最小值、计数等。


```python
df['a'].mean()
```




    47.0




```python
df['a'].sum()
```




    235




```python
df['a'].max()
```




    81




```python
df['a'].min()
```




    8




```python
df['a'].count()
```




    5




```python
df['a'].median() # 中位数
```




    63.0




```python
df['a'].var() #方差
```




    1154.5




```python
df['a'].skew() # 偏度
```




    -0.45733193928530436




```python
df['a'].kurt() # 峰度
```




    -2.9999915595685325




```python
df['a'].cumsum() # 累计求和
```




    0     81
    1     89
    2    102
    3    172
    4    235
    Name: a, dtype: int64




```python
df['a'].cumprod() # 累计求积
```




    0          81
    1         648
    2        8424
    3      589680
    4    37149840
    Name: a, dtype: int64




```python
df['a'].diff() # 差分
```




    0     NaN
    1   -73.0
    2     5.0
    3    57.0
    4    -7.0
    Name: a, dtype: float64




```python
df['a'].mad() # 平均绝对偏差
```




    29.2



#### 按行、列聚合计算



```python
df.sum(axis=0)  # 按列求和汇总到最后一行
```




    a    235
    b    236
    c    301
    d    232
    e    220
    dtype: int64




```python
df.sum(axis=1)  # 按行求和汇总到最后一列 
```




    0    254
    1    236
    2    146
    3    253
    4    335
    dtype: int64




```python
df.describe() # 描述性统计
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>47.000000</td>
      <td>47.200000</td>
      <td>60.200000</td>
      <td>46.400000</td>
      <td>44.000000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>33.977934</td>
      <td>20.656718</td>
      <td>26.395075</td>
      <td>30.369392</td>
      <td>39.083244</td>
    </tr>
    <tr>
      <th>min</th>
      <td>8.000000</td>
      <td>28.000000</td>
      <td>24.000000</td>
      <td>25.000000</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>13.000000</td>
      <td>35.000000</td>
      <td>55.000000</td>
      <td>25.000000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>63.000000</td>
      <td>39.000000</td>
      <td>56.000000</td>
      <td>36.000000</td>
      <td>39.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>70.000000</td>
      <td>54.000000</td>
      <td>69.000000</td>
      <td>48.000000</td>
      <td>70.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>81.000000</td>
      <td>80.000000</td>
      <td>97.000000</td>
      <td>98.000000</td>
      <td>96.000000</td>
    </tr>
  </tbody>
</table>
</div>



#### agg函数

对整个DataFrame批量使用多个聚合函数


```python
df.agg(['sum', 'mean','max','min','median'])
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>sum</th>
      <td>235.0</td>
      <td>236.0</td>
      <td>301.0</td>
      <td>232.0</td>
      <td>220.0</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>47.0</td>
      <td>47.2</td>
      <td>60.2</td>
      <td>46.4</td>
      <td>44.0</td>
    </tr>
    <tr>
      <th>max</th>
      <td>81.0</td>
      <td>80.0</td>
      <td>97.0</td>
      <td>98.0</td>
      <td>96.0</td>
    </tr>
    <tr>
      <th>min</th>
      <td>8.0</td>
      <td>28.0</td>
      <td>24.0</td>
      <td>25.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>median</th>
      <td>63.0</td>
      <td>39.0</td>
      <td>56.0</td>
      <td>36.0</td>
      <td>39.0</td>
    </tr>
  </tbody>
</table>
</div>



对DataFramed的某些列应用不同的聚合函数


```python
df.agg({'a':['max','min'],'b':['sum','mean'],'c':['median']})
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>max</th>
      <td>81.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>8.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>sum</th>
      <td>NaN</td>
      <td>236.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>NaN</td>
      <td>47.2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>median</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>56.0</td>
    </tr>
  </tbody>
</table>
</div>



#### apply、applymap、map函数

>注意其中applymap函数在新版已经被弃用，这里的案例是基于pandas=1.3.2写的

在Python中如果想要对数据使用函数，可以借助apply(),applymap(),map()对数据进行转换，括号里面可以是直接函数式，或者自定义函数（def）或者匿名函数（lambda）

1、当我们要对数据框（DataFrame）的数据进行按行或按列操作时用apply()


```python
df.apply(lambda x :x.max()-x.min(),axis=1)
#axis=1，表示按行对数据进行操作
#从下面的结果可以看出，我们使用了apply函数之后，系统自动按行找最大值和最小值计算，每一行输出一个值
```




    0    72
    1    90
    2    52
    3    58
    4    72
    dtype: int64




```python
df.apply(lambda x :x.max()-x.min(),axis=0)
#默认参数axis=0,表示按列对数据进行操作
#从下面的结果可以看出，我们使用了apply函数之后，系统自动按列找最大值和最小值计算，每一列输出一个值
```




    a    73
    b    52
    c    73
    d    73
    e    93
    dtype: int64



2、当我们要对数据框（DataFrame）的每一个数据进行操作时用applymap()，返回结果是DataFrame格式


```python
df.applymap(lambda x : 1 if x>60 else 0)
#从下面的结果可以看出，我们使用了applymap函数之后，
#系统自动对每一个数据进行判断，判断之后输出结果
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
      <th>d</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



3、当我们要对Series的每一个数据进行操作时用map()


```python
df['a'].map(lambda x : 1 if x>60 else 0)
```




    0    1
    1    0
    2    0
    3    1
    4    1
    Name: a, dtype: int64



总结：

`apply()` 函数可以在DataFrame或Series上应用自定义函数，可以在行或列上进行操作。

`applymap()` 函数只适用于DataFrame，可以在每个元素上应用自定义函数。

`map()` 函数只适用于Series，用于将每个元素映射到另一个值。

以上是数学运算部分，包括聚合计算、批量应用聚合函数，以及对Series和DataFrame进行批量映射，接下来我们来看如何对数据进行合并拼接

---
