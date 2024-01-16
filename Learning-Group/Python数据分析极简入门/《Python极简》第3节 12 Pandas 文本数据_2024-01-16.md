# 《Python数据分析极简入门》
## 第3节 12 Pandas 数据读写

## Pandas 数据读写

Pandas提供了多种读取数据的方法，包括读取CSV、Excel、SQL数据库等。

#### CSV

写出`csv`文件


```python
import pandas as pd
import numpy as np

data = np.random.rand(10, 10)  # 生成一个10行10列的随机数矩阵
columns = ['col' + str(i) for i in range(10)]  # 列名为col0, col1, ..., col9

df = pd.DataFrame(data, columns=columns)
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
      <th>col0</th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
      <th>col4</th>
      <th>col5</th>
      <th>col6</th>
      <th>col7</th>
      <th>col8</th>
      <th>col9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.466616</td>
      <td>0.728356</td>
      <td>0.611705</td>
      <td>0.798693</td>
      <td>0.595354</td>
      <td>0.985732</td>
      <td>0.586150</td>
      <td>0.320381</td>
      <td>0.335783</td>
      <td>0.660817</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.712571</td>
      <td>0.335545</td>
      <td>0.523658</td>
      <td>0.528449</td>
      <td>0.666035</td>
      <td>0.021001</td>
      <td>0.947240</td>
      <td>0.399122</td>
      <td>0.281759</td>
      <td>0.110816</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.175048</td>
      <td>0.513420</td>
      <td>0.067066</td>
      <td>0.666860</td>
      <td>0.377052</td>
      <td>0.213377</td>
      <td>0.175968</td>
      <td>0.877383</td>
      <td>0.587943</td>
      <td>0.531723</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.034618</td>
      <td>0.910112</td>
      <td>0.131991</td>
      <td>0.482421</td>
      <td>0.579907</td>
      <td>0.569939</td>
      <td>0.641757</td>
      <td>0.459544</td>
      <td>0.546252</td>
      <td>0.438100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.112847</td>
      <td>0.117470</td>
      <td>0.360243</td>
      <td>0.598008</td>
      <td>0.210927</td>
      <td>0.262409</td>
      <td>0.540579</td>
      <td>0.397511</td>
      <td>0.142911</td>
      <td>0.360057</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.228802</td>
      <td>0.065476</td>
      <td>0.327229</td>
      <td>0.377131</td>
      <td>0.021064</td>
      <td>0.429451</td>
      <td>0.366117</td>
      <td>0.420715</td>
      <td>0.977730</td>
      <td>0.812894</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.134770</td>
      <td>0.725406</td>
      <td>0.159081</td>
      <td>0.696428</td>
      <td>0.525755</td>
      <td>0.240271</td>
      <td>0.959835</td>
      <td>0.836452</td>
      <td>0.189946</td>
      <td>0.998590</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.176187</td>
      <td>0.216828</td>
      <td>0.444304</td>
      <td>0.726939</td>
      <td>0.334520</td>
      <td>0.922983</td>
      <td>0.668025</td>
      <td>0.207854</td>
      <td>0.870736</td>
      <td>0.822457</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.506092</td>
      <td>0.697873</td>
      <td>0.296946</td>
      <td>0.443291</td>
      <td>0.671899</td>
      <td>0.344138</td>
      <td>0.502330</td>
      <td>0.562803</td>
      <td>0.304063</td>
      <td>0.118550</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.991827</td>
      <td>0.631362</td>
      <td>0.552241</td>
      <td>0.640401</td>
      <td>0.156152</td>
      <td>0.548396</td>
      <td>0.831292</td>
      <td>0.563461</td>
      <td>0.221882</td>
      <td>0.891689</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.to_csv('./output/foo.csv')  # 请注意需要在你的代码文件夹目录下建一个\output 文件夹才能写入
```

读入刚刚写出的文件


```python
pd.read_csv('./output/foo.csv')
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
      <th>Unnamed: 0</th>
      <th>col0</th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
      <th>col4</th>
      <th>col5</th>
      <th>col6</th>
      <th>col7</th>
      <th>col8</th>
      <th>col9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>0.466616</td>
      <td>0.728356</td>
      <td>0.611705</td>
      <td>0.798693</td>
      <td>0.595354</td>
      <td>0.985732</td>
      <td>0.586150</td>
      <td>0.320381</td>
      <td>0.335783</td>
      <td>0.660817</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0.712571</td>
      <td>0.335545</td>
      <td>0.523658</td>
      <td>0.528449</td>
      <td>0.666035</td>
      <td>0.021001</td>
      <td>0.947240</td>
      <td>0.399122</td>
      <td>0.281759</td>
      <td>0.110816</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>0.175048</td>
      <td>0.513420</td>
      <td>0.067066</td>
      <td>0.666860</td>
      <td>0.377052</td>
      <td>0.213377</td>
      <td>0.175968</td>
      <td>0.877383</td>
      <td>0.587943</td>
      <td>0.531723</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>0.034618</td>
      <td>0.910112</td>
      <td>0.131991</td>
      <td>0.482421</td>
      <td>0.579907</td>
      <td>0.569939</td>
      <td>0.641757</td>
      <td>0.459544</td>
      <td>0.546252</td>
      <td>0.438100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>0.112847</td>
      <td>0.117470</td>
      <td>0.360243</td>
      <td>0.598008</td>
      <td>0.210927</td>
      <td>0.262409</td>
      <td>0.540579</td>
      <td>0.397511</td>
      <td>0.142911</td>
      <td>0.360057</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>0.228802</td>
      <td>0.065476</td>
      <td>0.327229</td>
      <td>0.377131</td>
      <td>0.021064</td>
      <td>0.429451</td>
      <td>0.366117</td>
      <td>0.420715</td>
      <td>0.977730</td>
      <td>0.812894</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>0.134770</td>
      <td>0.725406</td>
      <td>0.159081</td>
      <td>0.696428</td>
      <td>0.525755</td>
      <td>0.240271</td>
      <td>0.959835</td>
      <td>0.836452</td>
      <td>0.189946</td>
      <td>0.998590</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>0.176187</td>
      <td>0.216828</td>
      <td>0.444304</td>
      <td>0.726939</td>
      <td>0.334520</td>
      <td>0.922983</td>
      <td>0.668025</td>
      <td>0.207854</td>
      <td>0.870736</td>
      <td>0.822457</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>0.506092</td>
      <td>0.697873</td>
      <td>0.296946</td>
      <td>0.443291</td>
      <td>0.671899</td>
      <td>0.344138</td>
      <td>0.502330</td>
      <td>0.562803</td>
      <td>0.304063</td>
      <td>0.118550</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>0.991827</td>
      <td>0.631362</td>
      <td>0.552241</td>
      <td>0.640401</td>
      <td>0.156152</td>
      <td>0.548396</td>
      <td>0.831292</td>
      <td>0.563461</td>
      <td>0.221882</td>
      <td>0.891689</td>
    </tr>
  </tbody>
</table>
</div>



### EXCEL

写出`excel`文件


```python
df.to_excel('./output/foo.xlsx', sheet_name='Sheet1',index = None)
```

读取`excel`文件


```python
pd.read_excel('./output/foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
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
      <th>col0</th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
      <th>col4</th>
      <th>col5</th>
      <th>col6</th>
      <th>col7</th>
      <th>col8</th>
      <th>col9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.466616</td>
      <td>0.728356</td>
      <td>0.611705</td>
      <td>0.798693</td>
      <td>0.595354</td>
      <td>0.985732</td>
      <td>0.586150</td>
      <td>0.320381</td>
      <td>0.335783</td>
      <td>0.660817</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.712571</td>
      <td>0.335545</td>
      <td>0.523658</td>
      <td>0.528449</td>
      <td>0.666035</td>
      <td>0.021001</td>
      <td>0.947240</td>
      <td>0.399122</td>
      <td>0.281759</td>
      <td>0.110816</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.175048</td>
      <td>0.513420</td>
      <td>0.067066</td>
      <td>0.666860</td>
      <td>0.377052</td>
      <td>0.213377</td>
      <td>0.175968</td>
      <td>0.877383</td>
      <td>0.587943</td>
      <td>0.531723</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.034618</td>
      <td>0.910112</td>
      <td>0.131991</td>
      <td>0.482421</td>
      <td>0.579907</td>
      <td>0.569939</td>
      <td>0.641757</td>
      <td>0.459544</td>
      <td>0.546252</td>
      <td>0.438100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.112847</td>
      <td>0.117470</td>
      <td>0.360243</td>
      <td>0.598008</td>
      <td>0.210927</td>
      <td>0.262409</td>
      <td>0.540579</td>
      <td>0.397511</td>
      <td>0.142911</td>
      <td>0.360057</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.228802</td>
      <td>0.065476</td>
      <td>0.327229</td>
      <td>0.377131</td>
      <td>0.021064</td>
      <td>0.429451</td>
      <td>0.366117</td>
      <td>0.420715</td>
      <td>0.977730</td>
      <td>0.812894</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.134770</td>
      <td>0.725406</td>
      <td>0.159081</td>
      <td>0.696428</td>
      <td>0.525755</td>
      <td>0.240271</td>
      <td>0.959835</td>
      <td>0.836452</td>
      <td>0.189946</td>
      <td>0.998590</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.176187</td>
      <td>0.216828</td>
      <td>0.444304</td>
      <td>0.726939</td>
      <td>0.334520</td>
      <td>0.922983</td>
      <td>0.668025</td>
      <td>0.207854</td>
      <td>0.870736</td>
      <td>0.822457</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.506092</td>
      <td>0.697873</td>
      <td>0.296946</td>
      <td>0.443291</td>
      <td>0.671899</td>
      <td>0.344138</td>
      <td>0.502330</td>
      <td>0.562803</td>
      <td>0.304063</td>
      <td>0.118550</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.991827</td>
      <td>0.631362</td>
      <td>0.552241</td>
      <td>0.640401</td>
      <td>0.156152</td>
      <td>0.548396</td>
      <td>0.831292</td>
      <td>0.563461</td>
      <td>0.221882</td>
      <td>0.891689</td>
    </tr>
  </tbody>
</table>
</div>



#### HDF

写出`hdf`文件


```python
df.to_hdf('./output/foo.h5','df')
```

读入刚刚写出的文件


```python
pd.read_hdf('./output/foo.h5','df').head()
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
      <th>col0</th>
      <th>col1</th>
      <th>col2</th>
      <th>col3</th>
      <th>col4</th>
      <th>col5</th>
      <th>col6</th>
      <th>col7</th>
      <th>col8</th>
      <th>col9</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.466616</td>
      <td>0.728356</td>
      <td>0.611705</td>
      <td>0.798693</td>
      <td>0.595354</td>
      <td>0.985732</td>
      <td>0.586150</td>
      <td>0.320381</td>
      <td>0.335783</td>
      <td>0.660817</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.712571</td>
      <td>0.335545</td>
      <td>0.523658</td>
      <td>0.528449</td>
      <td>0.666035</td>
      <td>0.021001</td>
      <td>0.947240</td>
      <td>0.399122</td>
      <td>0.281759</td>
      <td>0.110816</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.175048</td>
      <td>0.513420</td>
      <td>0.067066</td>
      <td>0.666860</td>
      <td>0.377052</td>
      <td>0.213377</td>
      <td>0.175968</td>
      <td>0.877383</td>
      <td>0.587943</td>
      <td>0.531723</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.034618</td>
      <td>0.910112</td>
      <td>0.131991</td>
      <td>0.482421</td>
      <td>0.579907</td>
      <td>0.569939</td>
      <td>0.641757</td>
      <td>0.459544</td>
      <td>0.546252</td>
      <td>0.438100</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.112847</td>
      <td>0.117470</td>
      <td>0.360243</td>
      <td>0.598008</td>
      <td>0.210927</td>
      <td>0.262409</td>
      <td>0.540579</td>
      <td>0.397511</td>
      <td>0.142911</td>
      <td>0.360057</td>
    </tr>
  </tbody>
</table>
</div>



#### MySQL

写出到mysql里


```python
from sqlalchemy import create_engine
import pandas as pd
```


```python
mysql_engine=create_engine("mysql+pymysql://root:password@localhost/test")
df.to_sql(pust_table_name,mysql_engine,if_exists='replace',index =  False) #  注意 mysql_engine一定要正确配置
```

读入刚刚写出的文件


```python
df = pd.read_sql("""
select a,b
from pust_table_name;
""",mysql_engine) # 再次强调，mysql_engine一定要正确配置，实在有问题可以私信 aiu_cda
df
```
