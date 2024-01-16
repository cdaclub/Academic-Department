# 《Python数据分析极简入门》

## 第2节 8-3 Pandas 数据重塑 - 数据交叉表

### 数据交叉表

交叉表显示了每个变量的不同类别组合中观察到的频率或计数。通俗地说，就是根据不同列的数据统计了频数

```
df = pd.DataFrame(
    { 'High':  ["高", "高", "高", "中", "中", "中", "低", "低", "低", "高", "低"],
     'Weight': ["重", "轻", "中", "中", "轻", "重", "重", "轻", "中", "重", "轻"]
    })
df
```

```python
pd.crosstab(df['High'], df['Weight']) 
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
      <th>Weight</th>
      <th>中</th>
      <th>轻</th>
      <th>重</th>
    </tr>
    <tr>
      <th>High</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>中</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>低</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>高</th>
      <td>1</td>
      <td>1</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



双层`crosstab`


```python
df = pd.DataFrame(
    { 'High':  ["高", "高", "高", "中", "中", "中", "低", "低", "低", "高", "低"],
     'Weight': ["重", "轻", "中", "中", "轻", "重", "重", "轻", "中", "重", "轻"],
     'Size':   ["大", "中", "小", "中", "中", "大", "中", "小", "小", "大", "小"]})
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
      <th>High</th>
      <th>Weight</th>
      <th>Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>高</td>
      <td>重</td>
      <td>大</td>
    </tr>
    <tr>
      <th>1</th>
      <td>高</td>
      <td>轻</td>
      <td>中</td>
    </tr>
    <tr>
      <th>2</th>
      <td>高</td>
      <td>中</td>
      <td>小</td>
    </tr>
    <tr>
      <th>3</th>
      <td>中</td>
      <td>中</td>
      <td>中</td>
    </tr>
    <tr>
      <th>4</th>
      <td>中</td>
      <td>轻</td>
      <td>中</td>
    </tr>
    <tr>
      <th>5</th>
      <td>中</td>
      <td>重</td>
      <td>大</td>
    </tr>
    <tr>
      <th>6</th>
      <td>低</td>
      <td>重</td>
      <td>中</td>
    </tr>
    <tr>
      <th>7</th>
      <td>低</td>
      <td>轻</td>
      <td>小</td>
    </tr>
    <tr>
      <th>8</th>
      <td>低</td>
      <td>中</td>
      <td>小</td>
    </tr>
    <tr>
      <th>9</th>
      <td>高</td>
      <td>重</td>
      <td>大</td>
    </tr>
    <tr>
      <th>10</th>
      <td>低</td>
      <td>轻</td>
      <td>小</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.crosstab(df['High'], [df['Weight'], df['Size']], rownames=['High'], colnames=['Weight', 'Size']) 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th>Weight</th>
      <th colspan="2" halign="left">中</th>
      <th colspan="2" halign="left">轻</th>
      <th colspan="2" halign="left">重</th>
    </tr>
    <tr>
      <th>Size</th>
      <th>中</th>
      <th>小</th>
      <th>中</th>
      <th>小</th>
      <th>中</th>
      <th>大</th>
    </tr>
    <tr>
      <th>High</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>中</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>低</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>高</th>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



另一种 宽表转长表 pd.wide_to_long() 


```python
np.random.seed(123)
df = pd.DataFrame({"A1970" : {0 : "a", 1 : "b", 2 : "c"},
                   "A1980" : {0 : "d", 1 : "e", 2 : "f"},
                   "B1970" : {0 : 2.5, 1 : 1.2, 2 : .7},
                   "B1980" : {0 : 3.2, 1 : 1.3, 2 : .1},
                   "X"     : dict(zip(range(3), np.random.randn(3)))
                  })
df["id"] = df.index
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
      <th>A1970</th>
      <th>A1980</th>
      <th>B1970</th>
      <th>B1980</th>
      <th>X</th>
      <th>id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>d</td>
      <td>2.5</td>
      <td>3.2</td>
      <td>-1.085631</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>e</td>
      <td>1.2</td>
      <td>1.3</td>
      <td>0.997345</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>f</td>
      <td>0.7</td>
      <td>0.1</td>
      <td>0.282978</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



把`id` 列用作标识列


```python
pd.wide_to_long(df, ["A", "B"], i="id", j="year")
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
      <th>X</th>
      <th>A</th>
      <th>B</th>
    </tr>
    <tr>
      <th>id</th>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>1970</th>
      <td>-1.085631</td>
      <td>a</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>1</th>
      <th>1970</th>
      <td>0.997345</td>
      <td>b</td>
      <td>1.2</td>
    </tr>
    <tr>
      <th>2</th>
      <th>1970</th>
      <td>0.282978</td>
      <td>c</td>
      <td>0.7</td>
    </tr>
    <tr>
      <th>0</th>
      <th>1980</th>
      <td>-1.085631</td>
      <td>d</td>
      <td>3.2</td>
    </tr>
    <tr>
      <th>1</th>
      <th>1980</th>
      <td>0.997345</td>
      <td>e</td>
      <td>1.3</td>
    </tr>
    <tr>
      <th>2</th>
      <th>1980</th>
      <td>0.282978</td>
      <td>f</td>
      <td>0.1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame({
    'famid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'birth': [1, 2, 3, 1, 2, 3, 1, 2, 3],
    'ht1': [2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1],
    'ht2': [3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9]
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
      <th>famid</th>
      <th>birth</th>
      <th>ht1</th>
      <th>ht2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>2.8</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>2</td>
      <td>2.9</td>
      <td>3.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>2.2</td>
      <td>2.9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>1</td>
      <td>2.0</td>
      <td>3.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>2</td>
      <td>1.8</td>
      <td>2.8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>3</td>
      <td>1.9</td>
      <td>2.4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>1</td>
      <td>2.2</td>
      <td>3.3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>2</td>
      <td>2.3</td>
      <td>3.4</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>3</td>
      <td>2.1</td>
      <td>2.9</td>
    </tr>
  </tbody>
</table>
</div>



把`famid`, `birth` 两列用作标识列


```python
l = pd.wide_to_long(df, stubnames='ht', i=['famid', 'birth'], j='age')
l
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
      <th></th>
      <th>ht</th>
    </tr>
    <tr>
      <th>famid</th>
      <th>birth</th>
      <th>age</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="6" valign="top">1</th>
      <th rowspan="2" valign="top">1</th>
      <th>1</th>
      <td>2.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.4</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>1</th>
      <td>2.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>1</th>
      <td>2.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.9</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">2</th>
      <th rowspan="2" valign="top">1</th>
      <th>1</th>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.2</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>1</th>
      <td>1.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>1</th>
      <td>1.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.4</td>
    </tr>
    <tr>
      <th rowspan="6" valign="top">3</th>
      <th rowspan="2" valign="top">1</th>
      <th>1</th>
      <td>2.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.3</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">2</th>
      <th>1</th>
      <td>2.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3.4</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">3</th>
      <th>1</th>
      <td>2.1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.9</td>
    </tr>
  </tbody>
</table>
</div>