# 《Python数据分析极简入门》

## 第2节 8-1 Pandas 数据重塑 - 数据变形


### 数据重塑(Reshaping)

数据重塑，顾名思义就是给数据做各种变形，主要有以下几种：
- df.pivot 数据变形
- df.pivot_table 数据透视表
- df.stack/unstack 数据堆叠
- df.melt  数据融合
- df.cross 数据交叉表

### df.pivot( )  数据变形

> 根据索引（index）、列（column）（values）值)， 对原有DataFrame(数据框)进行变形重塑,俗称长表转宽表

![](https://files.mdnice.com/user/33324/b25d756f-dc4b-4e42-bc78-acfc3c16788a.png)


```python
import pandas as pd
import numpy as np
```


```python
df = pd.DataFrame(
    { '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
     '科目': ['语文', '数学', '英语', '语文', '数学', '英语'],
     '成绩': [91, 80, 100, 80, 100, 96]})
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
      <th>成绩</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>语文</td>
      <td>91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>张三</td>
      <td>数学</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>张三</td>
      <td>英语</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3</th>
      <td>李四</td>
      <td>语文</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>李四</td>
      <td>数学</td>
      <td>100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>李四</td>
      <td>英语</td>
      <td>96</td>
    </tr>
  </tbody>
</table>
</div>



长转宽：使用 `df.pivot` 以`姓名`为`index`,以各`科目`为`columns`，来统计各科成绩：


```python
df = pd.DataFrame(
    { '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
     '科目': ['语文', '数学', '英语', '语文', '数学', '英语'],
     '成绩': [91, 80, 100, 80, 100, 96]})
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
      <th>成绩</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>语文</td>
      <td>91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>张三</td>
      <td>数学</td>
      <td>80</td>
    </tr>
    <tr>
      <th>2</th>
      <td>张三</td>
      <td>英语</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3</th>
      <td>李四</td>
      <td>语文</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>李四</td>
      <td>数学</td>
      <td>100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>李四</td>
      <td>英语</td>
      <td>96</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.pivot(index='姓名', columns='科目', values='成绩')
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
      <th>科目</th>
      <th>数学</th>
      <th>英语</th>
      <th>语文</th>
    </tr>
    <tr>
      <th>姓名</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>张三</th>
      <td>80</td>
      <td>100</td>
      <td>91</td>
    </tr>
    <tr>
      <th>李四</th>
      <td>100</td>
      <td>96</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>



### pd.melt() 数据融合


![](https://files.mdnice.com/user/33324/c891025b-544b-467c-9635-676b3c939aeb.png)

```python
df = pd.DataFrame(
    { '姓名': ['张三', '张三', '张三', '李四', '李四', '李四'],
     '科目': ['语文', '数学', '英语', '语文', '数学', '英语'],
     '成绩': [91, 80, 100, 80, 100, 96]})
df1 = pd.pivot(df, index='姓名', columns='科目', values='成绩').reset_index()
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
      <th>科目</th>
      <th>姓名</th>
      <th>数学</th>
      <th>英语</th>
      <th>语文</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>80</td>
      <td>100</td>
      <td>91</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>100</td>
      <td>96</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>



宽表变长表：使用 `pd.melt` 以`姓名`为标识变量的列`id_vars`,以各`科目`为`value_vars`，来统计各科成绩：


```python
df1.melt(id_vars=['姓名'], value_vars=['数学', '英语', '语文'])
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
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>张三</td>
      <td>数学</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>李四</td>
      <td>数学</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>张三</td>
      <td>英语</td>
      <td>100</td>
    </tr>
    <tr>
      <th>3</th>
      <td>李四</td>
      <td>英语</td>
      <td>96</td>
    </tr>
    <tr>
      <th>4</th>
      <td>张三</td>
      <td>语文</td>
      <td>91</td>
    </tr>
    <tr>
      <th>5</th>
      <td>李四</td>
      <td>语文</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
</div>



### pd.pivot_table() 数据透视


```python
random.seed(1024)
df = pd.DataFrame(
    {'专业': np.repeat(['数学与应用数学', '计算机', '统计学'], 4),
     '班级': ['1班','1班','2班','2班']*3,
     '科目': ['高数', '线代'] * 6,
     '平均分': [random.randint(60,100) for i in range(12)],
     '及格人数': [random.randint(30,50) for i in range(12)]})
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
      <th>专业</th>
      <th>班级</th>
      <th>科目</th>
      <th>平均分</th>
      <th>及格人数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>数学与应用数学</td>
      <td>1班</td>
      <td>高数</td>
      <td>61</td>
      <td>34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>数学与应用数学</td>
      <td>1班</td>
      <td>线代</td>
      <td>90</td>
      <td>42</td>
    </tr>
    <tr>
      <th>2</th>
      <td>数学与应用数学</td>
      <td>2班</td>
      <td>高数</td>
      <td>84</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>数学与应用数学</td>
      <td>2班</td>
      <td>线代</td>
      <td>80</td>
      <td>43</td>
    </tr>
    <tr>
      <th>4</th>
      <td>计算机</td>
      <td>1班</td>
      <td>高数</td>
      <td>93</td>
      <td>34</td>
    </tr>
    <tr>
      <th>5</th>
      <td>计算机</td>
      <td>1班</td>
      <td>线代</td>
      <td>66</td>
      <td>43</td>
    </tr>
    <tr>
      <th>6</th>
      <td>计算机</td>
      <td>2班</td>
      <td>高数</td>
      <td>88</td>
      <td>45</td>
    </tr>
    <tr>
      <th>7</th>
      <td>计算机</td>
      <td>2班</td>
      <td>线代</td>
      <td>92</td>
      <td>44</td>
    </tr>
    <tr>
      <th>8</th>
      <td>统计学</td>
      <td>1班</td>
      <td>高数</td>
      <td>83</td>
      <td>46</td>
    </tr>
    <tr>
      <th>9</th>
      <td>统计学</td>
      <td>1班</td>
      <td>线代</td>
      <td>83</td>
      <td>41</td>
    </tr>
    <tr>
      <th>10</th>
      <td>统计学</td>
      <td>2班</td>
      <td>高数</td>
      <td>84</td>
      <td>49</td>
    </tr>
    <tr>
      <th>11</th>
      <td>统计学</td>
      <td>2班</td>
      <td>线代</td>
      <td>66</td>
      <td>49</td>
    </tr>
  </tbody>
</table>
</div>



各个专业对应科目的及格人数和平均分


```python
pd.pivot_table(df, index=['专业','科目'],
               values=['及格人数','平均分'],
               aggfunc={'及格人数':np.sum,"平均分":np.mean})
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
      <th>及格人数</th>
      <th>平均分</th>
    </tr>
    <tr>
      <th>专业</th>
      <th>科目</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">数学与应用数学</th>
      <th>线代</th>
      <td>85</td>
      <td>85.0</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>67</td>
      <td>72.5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">统计学</th>
      <th>线代</th>
      <td>90</td>
      <td>74.5</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>95</td>
      <td>83.5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">计算机</th>
      <th>线代</th>
      <td>87</td>
      <td>79.0</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>79</td>
      <td>90.5</td>
    </tr>
  </tbody>
</table>
</div>



补充说明：

`df.pivot_table()`和`df.pivot()`都是Pandas中用于将长表转换为宽表的方法，但它们在使用方式和功能上有一些区别。

1. 使用方式：
   - `df.pivot()`方法接受三个参数：`index`、`columns`和`values`，分别指定新表的索引、列和值。
   - `df.pivot_table()`方法接受多个参数，其中最重要的是`index`、`columns`和`values`，用于指定新表的索引、列和值。此外，还可以使用`aggfunc`参数指定对重复值进行聚合操作的函数，默认为均值。

2. 处理重复值：
   - `df.pivot()`方法在长表中存在重复值时会引发错误。因此，如果长表中存在重复值，就需要先进行去重操作，或者使用其他方法来处理重复值。
   - `df.pivot_table()`方法可以在长表中存在重复值的情况下进行透视操作，并可以使用`aggfunc`参数指定对重复值进行聚合操作的函数，默认为均值。

3. 聚合操作：
   - `df.pivot()`方法不支持对重复值进行聚合操作，它只是简单地将长表中的数据转换为宽表。
   - `df.pivot_table()`方法支持对重复值进行聚合操作。可以使用`aggfunc`参数来指定聚合函数，例如求均值、求和、计数等。

总的来说，`df.pivot()`方法适用于长表中不存在重复值的情况，而`df.pivot_table()`方法适用于长表中存在重复值的情况，并且可以对重复值进行聚合操作。根据具体的数据结构和分析需求，选择合适的方法来进行转换操作。



