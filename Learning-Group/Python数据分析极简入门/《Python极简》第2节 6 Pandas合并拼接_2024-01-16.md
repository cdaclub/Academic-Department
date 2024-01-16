# 《Python数据分析极简入门》

## 第2节 6 Pandas合并连接

在pandas中，有多种方法可以合并和拼接数据。常见的方法包括`append()`、`concat()`、`merge()`。

### 追加(Append)

append()函数用于将一个DataFrame或Series对象追加到另一个DataFrame中。




```python
import pandas as pd
df1 = pd.DataFrame({'A': ['a', 'b'],
                   'B': [1, 2]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'B': [2, 3, 4]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.append(df2,ignore_index=True) 
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### 合并(Concat)

concat()函数用于沿指定轴将多个对象（比如Series、DataFrame）堆叠在一起。可以沿行或列方向进行拼接。
![](https://files.mdnice.com/user/33324/f777f25b-9628-44e9-8304-7c1bbe2b0d97.png)
先看一个上下堆叠的例子


```python
df1 = pd.DataFrame({'A': ['a', 'b'],
                   'B': [1, 2]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'B': [2, 3, 4]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1,df2],axis =0) # 上下拼接
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



再看一个左右堆叠的例子


```python
df1 = pd.DataFrame({'A': ['a', 'b']})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({'B': [1, 2],
                    'C': [2, 4]})
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
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.concat([df1,df2],axis =1) # 左右拼接
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
      <td>a</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### 连接（Merge）

`merge()`函数用于根据一个或多个键将两个DataFrame的行连接起来。类似于SQL中的JOIN操作。


![](https://files.mdnice.com/user/33324/10ee7690-bdb6-4db4-89c3-6c1601a4115e.png)


#### 数据连接 1 (pd.merge)

先看一下 `inner` 和 `outer`连接


```python
df1 = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': [1, 2, 3]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'B': [2, 3, 4]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2,how = 'inner')
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2,how = 'outer')
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



#### 数据连接  2 (pd.merge)

再看左右链接的例子：


```python
df1 = pd.DataFrame({'A': ['a', 'b', 'c'],
                   'B': [1, 2, 3]})
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2 = pd.DataFrame({'A': [ 'b', 'c','d'],
                    'C': [2, 3, 4]})
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
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2,how = 'left',on = "A")  # 左连接
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
      <td>a</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2,how = 'right',on = "A") # 右连接
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
      <td>b</td>
      <td>2.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>d</td>
      <td>NaN</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2,how = 'inner',on = "A") # 内连接
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
      <td>b</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>3</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
pd.merge(df1,df2,how = 'outer',on = "A") # 外连接
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
      <td>a</td>
      <td>1.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>d</td>
      <td>NaN</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



补充1个小技巧


```python
df1[df1['A'].isin(df2['A'])] # 返回在df1中列'A'的值在df2中也存在的行
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>b</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>c</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1[~df1['A'].isin(df2['A'])] # 返回在df1中列'A'的值在df2中不存在的行
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>
