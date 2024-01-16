# 《Python数据分析极简入门》
## 第3节 11 Pandas 窗口数据


Pandas提供了窗口函数（Window Functions）用于在数据上执行滑动窗口操作，可以对数据进行滚动计算、滑动统计等操作。下面是一些常用的窗口函数：

滚动计算函数：
移动平均值（Moving Average）：


```python
import pandas as pd
data = {'column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)
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
      <th>column</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['MA'] = df['column'].rolling(window=3).mean()
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
      <th>column</th>
      <th>MA</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>



其中，window=3表示窗口大小为3，即计算每3个数据的平均值。

滚动求和（Rolling Sum）：


```python
import pandas as pd
df['Sum'] = df['column'].rolling(window=5).sum()
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
      <th>column</th>
      <th>MA</th>
      <th>Sum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.0</td>
      <td>15.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5.0</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>6.0</td>
      <td>25.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>8.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>9.0</td>
      <td>40.0</td>
    </tr>
  </tbody>
</table>
</div>



其中，window=5表示窗口大小为5，即计算每5个数据的和。

滑动统计函数：
滑动最大值（Rolling Maximum）：


```python
import pandas as pd
df['Max'] = df['column'].rolling(window=7).max()
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
      <th>column</th>
      <th>MA</th>
      <th>Sum</th>
      <th>Max</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.0</td>
      <td>15.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>6.0</td>
      <td>25.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7.0</td>
      <td>30.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>8.0</td>
      <td>35.0</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>9.0</td>
      <td>40.0</td>
      <td>10.0</td>
    </tr>
  </tbody>
</table>
</div>



其中，window=7表示窗口大小为7，即计算每7个数据的最大值。

滑动最小值（Rolling Minimum）：


```python
import pandas as pd
df['Min'] = df['column'].rolling(window=7).min()
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
      <th>column</th>
      <th>MA</th>
      <th>Sum</th>
      <th>Max</th>
      <th>Min</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.0</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>6.0</td>
      <td>25.0</td>
      <td>7.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7.0</td>
      <td>30.0</td>
      <td>8.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>8.0</td>
      <td>35.0</td>
      <td>9.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>9.0</td>
      <td>40.0</td>
      <td>10.0</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>



其中，window=7表示窗口大小为7，即计算每7个数据的最小值。

滑动标准差（Rolling Standard Deviation）：


```python
import pandas as pd
df['Std'] = df['column'].rolling(window=5).std()
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
      <th>column</th>
      <th>MA</th>
      <th>Sum</th>
      <th>Max</th>
      <th>Min</th>
      <th>Std</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.0</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.581139</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.581139</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>6.0</td>
      <td>25.0</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>1.581139</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7.0</td>
      <td>30.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>1.581139</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>8.0</td>
      <td>35.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>1.581139</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>9.0</td>
      <td>40.0</td>
      <td>10.0</td>
      <td>4.0</td>
      <td>1.581139</td>
    </tr>
  </tbody>
</table>
</div>



其中，window=5表示窗口大小为5，即计算每5个数据的标准差。

自定义窗口函数：
可以使用rolling().apply()方法来应用自定义的窗口函数：


```python
import pandas as pd

def custom_function(data):
    # 自定义的窗口函数逻辑
    return max(data) - min(data)

df['Result'] =df['column'].rolling(window=3).apply(custom_function)
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
      <th>column</th>
      <th>MA</th>
      <th>Sum</th>
      <th>Max</th>
      <th>Min</th>
      <th>Std</th>
      <th>Result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>2.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>3.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4.0</td>
      <td>15.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.581139</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.581139</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>7</td>
      <td>6.0</td>
      <td>25.0</td>
      <td>7.0</td>
      <td>1.0</td>
      <td>1.581139</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>7.0</td>
      <td>30.0</td>
      <td>8.0</td>
      <td>2.0</td>
      <td>1.581139</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>9</td>
      <td>8.0</td>
      <td>35.0</td>
      <td>9.0</td>
      <td>3.0</td>
      <td>1.581139</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>9</th>
      <td>10</td>
      <td>9.0</td>
      <td>40.0</td>
      <td>10.0</td>
      <td>4.0</td>
      <td>1.581139</td>
      <td>2.0</td>
    </tr>
  </tbody>
</table>
</div>



其中，custom_function是自定义的窗口函数，data是窗口中的数据，result是窗口函数的计算结果。
以上是Pandas窗口函数的一些常用操作和示例代码。需要注意的是，在使用窗口函数时，需要根据实际需求选择合适的窗口大小和窗口函数，并确保数据的顺序和窗口大小的一致性。
