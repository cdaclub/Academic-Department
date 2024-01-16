# 《Python数据分析极简入门》

## 第2节 7 Pandas分组聚合

分组聚合（group by）顾名思义就是分2步：

- **先分组**：根据某列数据的值进行分组。用`groupby()`对某列进行分组
- **后聚合**：将结果应用聚合函数进行计算。在`agg()`函数里应用聚合函数计算结果，如`sum()、mean()、count()、max()、min()`等，用于对每个分组进行聚合计算。


```python
import pandas as pd
import numpy as np
import random
```


```python
df = pd.DataFrame({'A': ['a', 'b', 'a', 'b','a', 'b'],
                   'B': ['L', 'L', 'M', 'N','M', 'M'],
                   'C': [107, 177, 139, 3, 52, 38],
                   'D': [22, 59, 38, 50, 60, 82]})

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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>L</td>
      <td>107</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>L</td>
      <td>177</td>
      <td>59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>M</td>
      <td>139</td>
      <td>38</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>N</td>
      <td>3</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>M</td>
      <td>52</td>
      <td>60</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>M</td>
      <td>38</td>
      <td>82</td>
    </tr>
  </tbody>
</table>
</div>



**单列分组**

① 对单列分组后应用`sum`聚合函数


```python
df.groupby('A').sum()
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
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>298</td>
      <td>120</td>
    </tr>
    <tr>
      <th>b</th>
      <td>218</td>
      <td>191</td>
    </tr>
  </tbody>
</table>
</div>



② 对单列分组后应用单个指定的聚合函数


```python
df.groupby('A').agg({'C': 'min'}).rename(columns={'C': 'C_min'})
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
      <th>C_min</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>52</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



③ 对单列分组后应用多个指定的聚合函数


```python
df.groupby(['A']).agg({'C':'max','D':'min'}).rename(columns={'C':'C_max','D':'D_min'})
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
      <th>C_max</th>
      <th>D_min</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>139</td>
      <td>22</td>
    </tr>
    <tr>
      <th>b</th>
      <td>177</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>



**两列分组**

① 对多列分组后应用`sum`聚合函数：


```python
df.groupby(['A', 'B']).sum()
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
      <th></th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>L</th>
      <td>107</td>
      <td>22</td>
    </tr>
    <tr>
      <th>M</th>
      <td>191</td>
      <td>98</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">b</th>
      <th>L</th>
      <td>177</td>
      <td>59</td>
    </tr>
    <tr>
      <th>M</th>
      <td>38</td>
      <td>82</td>
    </tr>
    <tr>
      <th>N</th>
      <td>3</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>



② 对两列进行`group` 后，都应用`max`聚合函数


```python
df.groupby(['A','B']).agg({'C':'max'}).rename(columns={'C': 'C_max'})
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
      <th></th>
      <th>C_max</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>L</th>
      <td>107</td>
    </tr>
    <tr>
      <th>M</th>
      <td>139</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">b</th>
      <th>L</th>
      <td>177</td>
    </tr>
    <tr>
      <th>M</th>
      <td>38</td>
    </tr>
    <tr>
      <th>N</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



③ 对两列进行分组`group` 后，分别应用`max`、`min`聚合函数


```python
df.groupby(['A','B']).agg({'C':'max','D':'min'}).rename(columns={'C':'C_max','D':'D_min'})
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
      <th></th>
      <th>C_max</th>
      <th>D_min</th>
    </tr>
    <tr>
      <th>A</th>
      <th>B</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>L</th>
      <td>107</td>
      <td>22</td>
    </tr>
    <tr>
      <th>M</th>
      <td>139</td>
      <td>38</td>
    </tr>
    <tr>
      <th rowspan="3" valign="top">b</th>
      <th>L</th>
      <td>177</td>
      <td>59</td>
    </tr>
    <tr>
      <th>M</th>
      <td>38</td>
      <td>82</td>
    </tr>
    <tr>
      <th>N</th>
      <td>3</td>
      <td>50</td>
    </tr>
  </tbody>
</table>
</div>



**补充1：** 应用自定义的聚合函数


```python
df = pd.DataFrame({'A': ['a', 'b', 'a', 'b','a', 'b'],
                   'B': ['L', 'L', 'M', 'N','M', 'M'],
                   'C': [107, 177, 139, 3, 52, 38],
                   'D': [22, 59, 38, 50, 60, 82]})

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
      <th>D</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>L</td>
      <td>107</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>L</td>
      <td>177</td>
      <td>59</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>M</td>
      <td>139</td>
      <td>38</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>N</td>
      <td>3</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>M</td>
      <td>52</td>
      <td>60</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>M</td>
      <td>38</td>
      <td>82</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 使用自定义的聚合函数计算每个分组的最大值和最小值
def custom_agg(x):
    return x.max() - x.min()
result =  df[['B','C']].groupby('B').agg({'C': custom_agg})
result
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
      <th>C</th>
    </tr>
    <tr>
      <th>B</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>L</th>
      <td>70</td>
    </tr>
    <tr>
      <th>M</th>
      <td>101</td>
    </tr>
    <tr>
      <th>N</th>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



**补充2：** 开窗函数（类似于SQL里面的`over partition by`）：

使用transform函数计算每个分组的均值


```python
# 使用transform函数计算每个分组的均值
df['B_C_std'] =  df[['B','C']].groupby('B')['C'].transform('mean')
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
      <th>D</th>
      <th>B_C_std</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>L</td>
      <td>107</td>
      <td>22</td>
      <td>142.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>L</td>
      <td>177</td>
      <td>59</td>
      <td>142.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>a</td>
      <td>M</td>
      <td>139</td>
      <td>38</td>
      <td>76.333333</td>
    </tr>
    <tr>
      <th>3</th>
      <td>b</td>
      <td>N</td>
      <td>3</td>
      <td>50</td>
      <td>3.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>a</td>
      <td>M</td>
      <td>52</td>
      <td>60</td>
      <td>76.333333</td>
    </tr>
    <tr>
      <th>5</th>
      <td>b</td>
      <td>M</td>
      <td>38</td>
      <td>82</td>
      <td>76.333333</td>
    </tr>
  </tbody>
</table>
</div>



**补充3：** 分组聚合拼接字符串 pandas实现类似 group_concat 功能

假设有这样一个数据：


```python
df = pd.DataFrame({
    '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
    '科目': ['语文', '数学', '英语', '语文', '数学', '英语']
})

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
      <th>姓名</th>
      <th>科目</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>语文</td>
    </tr>
    <tr>
      <th>1</th>
      <td>张三</td>
      <td>数学</td>
    </tr>
    <tr>
      <th>2</th>
      <td>张三</td>
      <td>英语</td>
    </tr>
    <tr>
      <th>3</th>
      <td>李四</td>
      <td>语文</td>
    </tr>
    <tr>
      <th>4</th>
      <td>李四</td>
      <td>数学</td>
    </tr>
    <tr>
      <th>5</th>
      <td>李四</td>
      <td>英语</td>
    </tr>
  </tbody>
</table>
</div>



**补充：按某列分组，将另一列文本拼接合并**

按名称分组，把每个人的科目拼接到一个字符串：


```python
# 对整个group对象中的所有列应用join 连接元素
(df.astype(str)# 先将数据全转为字符
.groupby('姓名')# 分组
.agg(lambda x : ','.join(x)))[['科目']]# join 连接元素
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
      <th>科目</th>
    </tr>
    <tr>
      <th>姓名</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>张三</th>
      <td>语文,数学,英语</td>
    </tr>
    <tr>
      <th>李四</th>
      <td>语文,数学,英语</td>
    </tr>
  </tbody>
</table>
</div>