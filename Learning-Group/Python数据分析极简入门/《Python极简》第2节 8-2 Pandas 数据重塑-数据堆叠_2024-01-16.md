# 《Python数据分析极简入门》

## 第2节 8-2 Pandas 数据重塑 - 数据堆叠


### 数据堆叠

```python
df = pd.DataFrame({'专业': np.repeat(['数学与应用数学', '计算机', '统计学','物理学'], 6),
                   '班级': ['1班','2班','3班']*8,
                   '科目': ['高数', '线代'] * 12,
                   '平均分': [random.randint(60,100) for i in range(24)],
                   '及格人数': [random.randint(30,50) for i in range(24)]})

df2 = pd.pivot_table(df, index=['专业','科目'],  values=['及格人数','平均分'],
               aggfunc={'及格人数':np.sum,"平均分":np.mean})
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
      <td>107</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>107</td>
      <td>65.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">物理学</th>
      <th>线代</th>
      <td>111</td>
      <td>82.333333</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>115</td>
      <td>78.666667</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">统计学</th>
      <th>线代</th>
      <td>107</td>
      <td>71.000000</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>122</td>
      <td>74.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">计算机</th>
      <th>线代</th>
      <td>122</td>
      <td>78.333333</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>137</td>
      <td>74.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
stacked = df2.stack()
```

“压缩”后的DataFrame或Series(具有MultiIndex作为索引)， [stack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack) 的逆操作是[unstack()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack)，默认情况下取消最后压缩的那个级别：

堆叠`stack()`，顾名思义就是把透视结果堆到一起。接下来我们把透视后堆叠的数据一步步展开`unstack()`：


```python
stacked.unstack()
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
      <td>107.0</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>107.0</td>
      <td>65.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">物理学</th>
      <th>线代</th>
      <td>111.0</td>
      <td>82.333333</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>115.0</td>
      <td>78.666667</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">统计学</th>
      <th>线代</th>
      <td>107.0</td>
      <td>71.000000</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>122.0</td>
      <td>74.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">计算机</th>
      <th>线代</th>
      <td>122.0</td>
      <td>78.333333</td>
    </tr>
    <tr>
      <th>高数</th>
      <td>137.0</td>
      <td>74.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
stacked.unstack(level=1)
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
      <th>线代</th>
      <th>高数</th>
    </tr>
    <tr>
      <th>专业</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">数学与应用数学</th>
      <th>及格人数</th>
      <td>107.000000</td>
      <td>107.000000</td>
    </tr>
    <tr>
      <th>平均分</th>
      <td>76.000000</td>
      <td>65.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">物理学</th>
      <th>及格人数</th>
      <td>111.000000</td>
      <td>115.000000</td>
    </tr>
    <tr>
      <th>平均分</th>
      <td>82.333333</td>
      <td>78.666667</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">统计学</th>
      <th>及格人数</th>
      <td>107.000000</td>
      <td>122.000000</td>
    </tr>
    <tr>
      <th>平均分</th>
      <td>71.000000</td>
      <td>74.000000</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">计算机</th>
      <th>及格人数</th>
      <td>122.000000</td>
      <td>137.000000</td>
    </tr>
    <tr>
      <th>平均分</th>
      <td>78.333333</td>
      <td>74.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
stacked.unstack(level=0)
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
      <th>数学与应用数学</th>
      <th>物理学</th>
      <th>统计学</th>
      <th>计算机</th>
    </tr>
    <tr>
      <th>科目</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">线代</th>
      <th>及格人数</th>
      <td>107.0</td>
      <td>111.000000</td>
      <td>107.0</td>
      <td>122.000000</td>
    </tr>
    <tr>
      <th>平均分</th>
      <td>76.0</td>
      <td>82.333333</td>
      <td>71.0</td>
      <td>78.333333</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">高数</th>
      <th>及格人数</th>
      <td>107.0</td>
      <td>115.000000</td>
      <td>122.0</td>
      <td>137.000000</td>
    </tr>
    <tr>
      <th>平均分</th>
      <td>65.0</td>
      <td>78.666667</td>
      <td>74.0</td>
      <td>74.000000</td>
    </tr>
  </tbody>
</table>
</div>



