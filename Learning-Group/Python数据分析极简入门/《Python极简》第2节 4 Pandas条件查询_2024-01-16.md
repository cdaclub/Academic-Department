# 《Python数据分析极简入门》

## 第2节 4 Pandas条件查询

在pandas中，可以使用条件筛选来选择满足特定条件的数据

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




```python
# 单一条件
df[df['a']>60]
df.loc[df['a']>60]
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




```python
# 单一条件&多列
df.loc[(df['a']>60) ,['a','b','d']]
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
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>81</td>
      <td>28</td>
      <td>25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70</td>
      <td>54</td>
      <td>48</td>
    </tr>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>80</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 多条件
df[(df['a']>60) & (df['b']>60)]
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




```python
# 多条件 筛选行 & 指定列筛选列
df.loc[(df['a']>60) & (df['b']>60) ,['a','b','d']]
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
      <th>d</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>63</td>
      <td>80</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>



以上是使用条件筛选来选取数据 ，接下来我们来看如何对数据进行数学计算

---
