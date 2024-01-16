# 《Python数据分析极简入门》
## 第2节 3 Pandas数据查看

这里我们创建一个`DataFrame`命名为`df`：

```python
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



查看前n行


```python
df.head(2)
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
  </tbody>
</table>
</div>



查看后n行


```python
df.tail(2)
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



查看随机N行


```python
df.sample(2)
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
      <th>1</th>
      <td>8</td>
      <td>35</td>
      <td>56</td>
      <td>98</td>
      <td>39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>54</td>
      <td>69</td>
      <td>48</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



#### 按列选取

单列选取，我们有3种方式可以实现

第一种，直接在`[]`里面写上要筛选的列名


```python
df['a']
```




    0    81
    1     8
    2    13
    3    70
    4    63
    Name: a, dtype: int64



第二种，在`.iloc[]`里的`,`前面写上要筛选的行索引，在`,`后面写上要筛选的列索引。其中`:`代表所有，`0:3`代表从索引0到2


```python
df.iloc[0:3,0]
```




    0    81
    1     8
    2    13
    Name: a, dtype: int64



第三种，直接`.`后面写上列名


```python
df.a
```




    0    81
    1     8
    2    13
    3    70
    4    63
    Name: a, dtype: int64



同样的，选择多列常见的也有3种方式：

第一种，直接在`[]`里面写上要筛选的列名组成的列表`['a','c','d']`


```python
df[['a','c','d']]
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
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81</td>
      <td>24</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>56</td>
      <td>98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>55</td>
      <td>36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>69</td>
      <td>48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>97</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



第二种，在`.iloc[]`里面行索引位置写`：`选取所有行，列索引位置写上要筛选的列索引组成的列表`[0,2,3]`


```python
df.iloc[:,[0,2,3]]
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
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81</td>
      <td>24</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>56</td>
      <td>98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>55</td>
      <td>36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>69</td>
      <td>48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>97</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



第三种，在`.loc[]`里面的行索引位置写`：`来选取所有行，在列索引位置写上要筛选的列索引组成的列表`['a','c','d']`


```python
df.loc[:,['a','c','d']]
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
      <th>c</th>
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81</td>
      <td>24</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>8</td>
      <td>56</td>
      <td>98</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>55</td>
      <td>36</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>69</td>
      <td>48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>97</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



#### 按行选取

直接选取第一行


```python
df[0:1]
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
  </tbody>
</table>
</div>



用`loc`选取第一行 


```python
df.loc[0:0]
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
  </tbody>
</table>
</div>



选取任意多行


```python
df.iloc[[1,3],]
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
      <th>1</th>
      <td>8</td>
      <td>35</td>
      <td>56</td>
      <td>98</td>
      <td>39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>54</td>
      <td>69</td>
      <td>48</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



选取连续多行


```python
df.iloc[1:4,:]
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
  </tbody>
</table>
</div>



#### 指定行列

指定行列值


```python
df.iat[2,2] # 根据行列索引
```




    55




```python
df.at[2,'c'] # 根据行列名称
```




    55



指定行列区域


```python
df.iloc[[2,3],[1,4]]
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
      <th>b</th>
      <th>e</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>39</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>54</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>



以上是关于如何查看一个DataFrame里的数据，包括用`[]`、`iloc`、`iat`等方式选取数据，接下来我们来看如何用条件表达式来筛选数据：


---