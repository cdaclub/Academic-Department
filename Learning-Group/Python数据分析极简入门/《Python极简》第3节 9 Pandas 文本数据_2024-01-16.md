# 《Python数据分析极简入门》

## 第3节 9 Pandas 文本数据

```python
import pandas as pd
```

#### 1、cat() 拼接字符串 


```python
d = pd.DataFrame(['a', 'b', 'c'],columns = ['A'])
d
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
    <tr>
      <th>2</th>
      <td>c</td>
    </tr>
  </tbody>
</table>
</div>



将某列元素拼接一列特定字符串


```python
d['A'].str.cat(['A', 'B', 'C'], sep=',')
```




    0    a,A
    1    b,B
    2    c,C
    Name: A, dtype: object



将某列的元素合并为一个字符串


```python
d['A'].str.cat(sep=',')
```




    'a,b,c'



#### 2、split() 切分字符串 


```python
import numpy as np
import pandas as pd
d = pd.DataFrame(['a_b_c', 'c_d_e', np.nan, 'f_g_h'],columns = ['A'])
d
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
      <td>a_b_c</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c_d_e</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f_g_h</td>
    </tr>
  </tbody>
</table>
</div>



将某列的字符串元素进行切分


```python
d['A'].str.split('_')
```




    0    [a, b, c]
    1    [c, d, e]
    2          NaN
    3    [f, g, h]
    Name: A, dtype: object



#### 3、get() 获取指定位置的字符串 


```python
d = pd.DataFrame(['a_b_c', 'c_d_e', np.nan, 'f_g_h'],columns = ['A'])
d['A']
```




    0    a_b_c
    1    c_d_e
    2      NaN
    3    f_g_h
    Name: A, dtype: object




```python
d['A'].str.get(2)
```




    0      b
    1      d
    2    NaN
    3      g
    Name: A, dtype: object



#### 4、join() 对每个字符都用给定的字符串拼接起来（不常用） 


```python
d = pd.DataFrame(['a_b_c', 'c_d_e', np.nan, 'f_g_h'],columns = ['A'])
d['A']
```




    0    a_b_c
    1    c_d_e
    2      NaN
    3    f_g_h
    Name: A, dtype: object




```python
d['A'].str.join("!")
```




    0    a!_!b!_!c
    1    c!_!d!_!e
    2          NaN
    3    f!_!g!_!h
    Name: A, dtype: object



#### 5、contains() 是否包含表达式 （很常用）


```python
d['A'].str.contains('d')
```




    0    False
    1     True
    2      NaN
    3    False
    Name: A, dtype: object




```python
d.fillna('0')[d.fillna('0')['A'].str.contains('d')]
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
      <th>1</th>
      <td>c_d_e</td>
    </tr>
  </tbody>
</table>
</div>




```python
d.fillna('0')[d['A'].fillna('0').str.contains('d|e')]

#表示或的关系用"A|B"，表示且用'A.*B|B.*A'
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
      <th>1</th>
      <td>c_d_e</td>
    </tr>
  </tbody>
</table>
</div>



#### 6、replace() 替换 


```python
d['A'].str.replace("_", ".")
```




    0    a.b.c
    1    c.d.e
    2      NaN
    3    f.g.h
    Name: A, dtype: object



#### 7、repeat() 重复 


```python
d['A'].str.repeat(3)
```




    0    a_b_ca_b_ca_b_c
    1    c_d_ec_d_ec_d_e
    2                NaN
    3    f_g_hf_g_hf_g_h
    Name: A, dtype: object



#### 8、pad() 左右补齐 


```python
d['A'].str.pad(10, fillchar="0")
```




    0    00000a_b_c
    1    00000c_d_e
    2           NaN
    3    00000f_g_h
    Name: A, dtype: object




```python
d['A'].str.pad(10, side="right", fillchar="?")
```




    0    a_b_c?????
    1    c_d_e?????
    2           NaN
    3    f_g_h?????
    Name: A, dtype: object



#### 9、center() 中间补齐


```python
d['A'].str.center(10, fillchar="?")
```




    0    ??a_b_c???
    1    ??c_d_e???
    2           NaN
    3    ??f_g_h???
    Name: A, dtype: object



#### 10、ljust() 右边补齐


```python
d['A'].str.ljust(10, fillchar="?")
```




    0    a_b_c?????
    1    c_d_e?????
    2           NaN
    3    f_g_h?????
    Name: A, dtype: object



#### 11、rjust() 左边补齐


```python
d['A'].str.rjust(10, fillchar="?")
```




    0    ?????a_b_c
    1    ?????c_d_e
    2           NaN
    3    ?????f_g_h
    Name: A, dtype: object



#### 12、zfill() 左边补0 


```python
d['A'].str.zfill(10)
```




    0    00000a_b_c
    1    00000c_d_e
    2           NaN
    3    00000f_g_h
    Name: A, dtype: object



#### 13、wrap() 在指定的位置加回车符号 


```python
d['A'].str.wrap(3)
```




    0    a_b\n_c
    1    c_d\n_e
    2        NaN
    3    f_g\n_h
    Name: A, dtype: object



#### 14、slice() 按给定点的开始结束位置切割字符串 


```python
d['A'].str.slice(1,3)
```




    0     _b
    1     _d
    2    NaN
    3     _g
    Name: A, dtype: object



#### 15、slice_replace() 使用给定的字符串，替换指定的位置的字符 


```python
d['A'].str.slice_replace(1, 3, "?")
```




    0    a?_c
    1    c?_e
    2     NaN
    3    f?_h
    Name: A, dtype: object



#### 16、count() 计算给定单词出现的次数 


```python
d['A'].str.count("b")
```




    0    1.0
    1    0.0
    2    NaN
    3    0.0
    Name: A, dtype: float64



#### 17、startswith() 判断是否以给定的字符串开头 


```python
d['A'].str.startswith("a")
```




    0     True
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 18、endswith() 判断是否以给定的字符串结束


```python
d['A'].str.endswith("e")
```




    0    False
    1     True
    2      NaN
    3    False
    Name: A, dtype: object



#### 19、findall() 查找所有符合正则表达式的字符，以数组形式返回 


```python
d['A'].str.findall("[a-z]")
```




    0    [a, b, c]
    1    [c, d, e]
    2          NaN
    3    [f, g, h]
    Name: A, dtype: object



#### 20、match() 检测是否全部匹配给点的字符串或者表达式 


```python
d['A'].str.match("[d-z]")
```




    0    False
    1    False
    2      NaN
    3     True
    Name: A, dtype: object



#### 21、extract() 抽取匹配的字符串出来，注意要加上括号，把你需要抽取的东西标注上 


```python
d['A'].str.extract("([d-z])")
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
      <th>0</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>d</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f</td>
    </tr>
  </tbody>
</table>
</div>



#### 22、len() 计算字符串的长度 


```python
d['A'].str.len()
```




    0    5.0
    1    5.0
    2    NaN
    3    5.0
    Name: A, dtype: float64



#### 23、strip() 去除前后的空白字符 


```python
df = pd.DataFrame(['a_b  ', '  d_e  ', np.nan, 'f_g  '],columns = ['B'])
df['B']
```




    0      a_b  
    1      d_e  
    2        NaN
    3      f_g  
    Name: B, dtype: object




```python
df['B'].str.strip()
```




    0    a_b
    1    d_e
    2    NaN
    3    f_g
    Name: B, dtype: object



#### 24、rstrip() 去除后面的空白字符 


```python
df['B'].str.rstrip()
```




    0      a_b
    1      d_e
    2      NaN
    3      f_g
    Name: B, dtype: object



#### 25、lstrip() 去除前面的空白字符 


```python
df['B'].str.lstrip()
```




    0    a_b  
    1    d_e  
    2      NaN
    3    f_g  
    Name: B, dtype: object



#### 26、partition() 把字符串数组切割称为DataFrame，注意切割只是切割称为三部分，分隔符前，分隔符，分隔符后 


```python
d['A'] .str.partition('_')
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a</td>
      <td>_</td>
      <td>b_c</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c</td>
      <td>_</td>
      <td>d_e</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f</td>
      <td>_</td>
      <td>g_h</td>
    </tr>
  </tbody>
</table>
</div>



#### 27、rpartition() 从右切起 


```python
d['A'].str.rpartition('_')
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>a_b</td>
      <td>_</td>
      <td>c</td>
    </tr>
    <tr>
      <th>1</th>
      <td>c_d</td>
      <td>_</td>
      <td>e</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f_g</td>
      <td>_</td>
      <td>h</td>
    </tr>
  </tbody>
</table>
</div>



#### 28、lower() 全部小写 


```python
d['A'].str.lower() 
```




    0    a_b_c
    1    c_d_e
    2      NaN
    3    f_g_h
    Name: A, dtype: object



#### 29、upper() 全部大写 


```python
d['A'].str.upper() 
```




    0    A_B_C
    1    C_D_E
    2      NaN
    3    F_G_H
    Name: A, dtype: object



#### 30、find() 从左边开始，查找给定字符串的所在位置 


```python
d['A'].str.find('d')
```




    0   -1.0
    1    2.0
    2    NaN
    3   -1.0
    Name: A, dtype: float64



#### 31、rfind() 从右边开始，查找给定字符串的所在位置 


```python
d['A'].str.rfind('d')
```




    0   -1.0
    1    2.0
    2    NaN
    3   -1.0
    Name: A, dtype: float64



#### 32、index() 查找给定字符串的位置，注意，如果不存在这个字符串，那么会报错！ 


```python
d['A'].str.index('_')
```




    0    1.0
    1    1.0
    2    NaN
    3    1.0
    Name: A, dtype: float64



#### 33、rindex() 从右边开始查找，给定字符串的位置 


```python
d['A'].str.rindex('_')
```




    0    3.0
    1    3.0
    2    NaN
    3    3.0
    Name: A, dtype: float64



#### 34、capitalize() 首字符大写 


```python
d['A'].str.capitalize()
```




    0    A_b_c
    1    C_d_e
    2      NaN
    3    F_g_h
    Name: A, dtype: object



#### 35、swapcase() 大小写互换 


```python
d['A'].str.capitalize()
```




    0    A_b_c
    1    C_d_e
    2      NaN
    3    F_g_h
    Name: A, dtype: object



#### 36、isalnum() 是否全部是数字和字母组成 


```python
d['A'].str.isalnum()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 37、isalpha() 是否全部是字母 


```python
d['A'].str.isalpha()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 38、isdigit() 是否全部都是数字 


```python
d['A'].str.isdigit()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 39、isspace() 是否空格 


```python
d['A'].str.isspace()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 40、islower() 是否全部小写 


```python
d['A'].str.islower()
```




    0    True
    1    True
    2     NaN
    3    True
    Name: A, dtype: object



#### 41、isupper() 是否全部大写 


```python
d['A'].str.isupper()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 42、istitle() 是否只有首字母为大写，其他字母为小写 


```python
d['A'].str.istitle()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 43、isnumeric() 是否是数字 


```python
d['A'].str.isnumeric()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object



#### 44、isdecimal() 是否全是数字 


```python
d['A'].str.isdecimal()
```




    0    False
    1    False
    2      NaN
    3    False
    Name: A, dtype: object