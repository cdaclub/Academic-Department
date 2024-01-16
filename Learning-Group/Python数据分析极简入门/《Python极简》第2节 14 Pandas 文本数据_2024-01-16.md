# 《Python数据分析极简入门》


## 第3节 14 Pandas 可视化


> 一图胜千言 A picture is worth a thousand words.

常见的可视化图有如下几种：
- line:折线图
- pie:饼图
- bar:柱状图
- hist:直方图
- box:箱型图
- area:面积图
- scatter：散点图


```python
#用于处理解决中文乱码问题和负号问题。
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #指定显示的字体，解决中文乱码
plt.rcParams['axes.unicode_minus'] = False #显示负号
```

#### line:折线图

折线图一般用于描述数据的**趋势**：


```python
import pandas as pd
import numpy as np
import random
df = pd.DataFrame({'A': ['a', 'b', 'c', 'd','e', 'f','g','h','i'],
                   'B': ['L', 'L', 'M', 'L','M', 'M','M','L','L'],
                   'C': [107, 177, 139, 38, 52, 38,87,38,56],
                   'D': [22, 59, 38, 59, 59, 82,89,48,88]}).set_index('A')
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
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>L</td>
      <td>107</td>
      <td>22</td>
    </tr>
    <tr>
      <th>b</th>
      <td>L</td>
      <td>177</td>
      <td>59</td>
    </tr>
    <tr>
      <th>c</th>
      <td>M</td>
      <td>139</td>
      <td>38</td>
    </tr>
    <tr>
      <th>d</th>
      <td>L</td>
      <td>38</td>
      <td>59</td>
    </tr>
    <tr>
      <th>e</th>
      <td>M</td>
      <td>52</td>
      <td>59</td>
    </tr>
    <tr>
      <th>f</th>
      <td>M</td>
      <td>38</td>
      <td>82</td>
    </tr>
    <tr>
      <th>g</th>
      <td>M</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>h</th>
      <td>L</td>
      <td>38</td>
      <td>48</td>
    </tr>
    <tr>
      <th>i</th>
      <td>L</td>
      <td>56</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
</div>



一组数据的折线图如下：


```python
df['C'].plot.line(
      )
```




    <AxesSubplot:xlabel='A'>



![](https://files.mdnice.com/user/33324/9eaf4084-e0bf-4456-8d52-0be780ff8280.png)


再来看一下两组数据的折线图


```python
df[['C','D']].plot.line()
```




    <AxesSubplot:xlabel='A'>


![](https://files.mdnice.com/user/33324/fc26d218-91d4-4b12-a3ae-6eebae6f4b1f.png)


#### pie:饼图

饼图一般用于展示数据的占比关系


```python
np.random.seed(123)
df1 = pd.Series(3*np.random.rand(4),index = ['a','b','c','d'],name = '占比')
df1
```




    a    0.683925
    b    0.707985
    c    1.646343
    d    1.803777
    Name: 占比, dtype: float64



看看以上四个数据的占比情况


```python
df1.plot.pie()
```




    <AxesSubplot:ylabel='占比'>





![](https://files.mdnice.com/user/33324/c2139d6d-bcb9-4770-88f7-941853da8466.png)


#### bar:柱状图

柱状图一般用于类别型数据的对比分析

一组数据的柱状图


```python
df['C'].plot.bar()
```




    <AxesSubplot:xlabel='A'>





![](https://files.mdnice.com/user/33324/0af538a6-5640-4a23-9f88-f8be522537b9.png)


两组数据的柱状图


```python
df[['C','D']].plot.bar()
```




    <AxesSubplot:xlabel='A'>





![](https://files.mdnice.com/user/33324/fcf5a714-e569-4861-b3e1-d0238c535f19.png)


横向柱状图


```python
df.plot.barh()
```




    <AxesSubplot:ylabel='A'>





![](https://files.mdnice.com/user/33324/3792e0dd-8a6f-45de-829f-33e3865a4a87.png)

其他几种柱状图


```python
df.assign(a = df.C- 70).plot.bar()
```




    <AxesSubplot:xlabel='A'>





![](https://files.mdnice.com/user/33324/7e78f7bf-67b0-4767-80d5-a22a242a034a.png)


```python
df.plot.bar(stacked = True)
```




    <AxesSubplot:xlabel='A'>




![](https://files.mdnice.com/user/33324/d52c6469-c1ee-4df9-8edc-fd3af340db91.png)


```python
df.plot.barh(stacked = True)
```




    <AxesSubplot:ylabel='A'>




![](https://files.mdnice.com/user/33324/6d987666-6962-45b8-a914-01ab7ff9a33e.png)


```python
df.head(5).plot.barh(stacked = True,colormap='cool')
```




    <AxesSubplot:ylabel='A'>




![](https://files.mdnice.com/user/33324/e81451f7-9c28-4441-abd2-ac1335e52737.png)



#### hist:直方图

直方图适合展现连续型数据的分布情况


```python
np.random.seed(123)
df2 = pd.DataFrame({'a':np.random.randn(1000)+1,
                   'b':np.random.randn(1000),
                   'c':np.random.randn(1000)-1},
                  columns = ['a','b','c'])
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
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.085631</td>
      <td>-0.748827</td>
      <td>-2.774224</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.997345</td>
      <td>0.567595</td>
      <td>-2.201377</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.282978</td>
      <td>0.718151</td>
      <td>0.096257</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.506295</td>
      <td>-0.999381</td>
      <td>-0.138963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.421400</td>
      <td>0.474898</td>
      <td>-2.520367</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>995</th>
      <td>1.634763</td>
      <td>0.845701</td>
      <td>-1.075335</td>
    </tr>
    <tr>
      <th>996</th>
      <td>2.069919</td>
      <td>-1.119923</td>
      <td>-1.946199</td>
    </tr>
    <tr>
      <th>997</th>
      <td>0.090673</td>
      <td>-0.359297</td>
      <td>1.040432</td>
    </tr>
    <tr>
      <th>998</th>
      <td>1.470264</td>
      <td>-1.609695</td>
      <td>0.015917</td>
    </tr>
    <tr>
      <th>999</th>
      <td>-0.111430</td>
      <td>0.013570</td>
      <td>-2.633788</td>
    </tr>
  </tbody>
</table>
<p>1000 rows × 3 columns</p>
</div>



先来看下一组数据的直方图


```python
df2['a'].plot.hist()
```




    <AxesSubplot:ylabel='Frequency'>




![](https://files.mdnice.com/user/33324/86bbe626-0941-42ea-a5cc-431637f249f3.png)



多组数据的直方图


```python
df2.plot.hist()
```




    <AxesSubplot:ylabel='Frequency'>



![](https://files.mdnice.com/user/33324/cd60bcac-e39d-4b51-bce5-acb5abb18246.png)



指定分箱数量的直方图


```python
#堆叠，指定分箱数量
df2.plot.hist(stacked = True,bins = 30)
```




    <AxesSubplot:ylabel='Frequency'>




![](https://files.mdnice.com/user/33324/81d0ef82-0b48-42b7-8a3c-ba2faee2e3d7.png)



#### box:箱型图

箱型图用于展示数据的分布、识别异常值以及比较不同组之间的差异。

一组数据的箱型图


```python
df.boxplot('C')
```




    <AxesSubplot:>





![](https://files.mdnice.com/user/33324/d443ceda-bc0a-44b7-85b3-543b9f7ba9ba.png)



再来看看用两列数据来画两个箱型图


```python
import pandas as pd
import numpy as np
import random
df = pd.DataFrame({'A': ['a', 'b', 'c', 'd','e', 'f','g','h','i'],
                   'B': ['L', 'L', 'M', 'L','M', 'M','M','L','L'],
                   'C': [107, 177, 139, 38, 52, 38,87,38,56],
                   'D': [22, 59, 38, 59, 59, 82,89,48,88]}).set_index('A')
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
      <th>B</th>
      <th>C</th>
      <th>D</th>
    </tr>
    <tr>
      <th>A</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>L</td>
      <td>107</td>
      <td>22</td>
    </tr>
    <tr>
      <th>b</th>
      <td>L</td>
      <td>177</td>
      <td>59</td>
    </tr>
    <tr>
      <th>c</th>
      <td>M</td>
      <td>139</td>
      <td>38</td>
    </tr>
    <tr>
      <th>d</th>
      <td>L</td>
      <td>38</td>
      <td>59</td>
    </tr>
    <tr>
      <th>e</th>
      <td>M</td>
      <td>52</td>
      <td>59</td>
    </tr>
    <tr>
      <th>f</th>
      <td>M</td>
      <td>38</td>
      <td>82</td>
    </tr>
    <tr>
      <th>g</th>
      <td>M</td>
      <td>87</td>
      <td>89</td>
    </tr>
    <tr>
      <th>h</th>
      <td>L</td>
      <td>38</td>
      <td>48</td>
    </tr>
    <tr>
      <th>i</th>
      <td>L</td>
      <td>56</td>
      <td>88</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.boxplot(['C','D'])
```




    <AxesSubplot:>





![](https://files.mdnice.com/user/33324/eb530409-c68b-4254-8963-f465d7e433df.png)


横向箱线图


```python
df.boxplot(['C','D'],vert = False)
```




    <AxesSubplot:>


![](https://files.mdnice.com/user/33324/8c0da2d2-c494-483c-a0a8-80bc4ef8d680.png)



#### area:面积图

面积图是一种有效的数据可视化工具，用于展示数据的趋势、比较不同组之间的差异以及理解数据的部分与整体关系。广泛应用于统计学、经济学、市场调研、环境科学等领域，并为数据分析和决策提供了重要的支持。


```python
np.random.seed(123)
df4 = pd.DataFrame(np.random.rand(10,4),columns = ['a','b','c','d'])
df4
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
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.283271</td>
      <td>0.175992</td>
      <td>0.058558</td>
      <td>0.667383</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.765492</td>
      <td>0.707079</td>
      <td>0.894216</td>
      <td>0.984987</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.244719</td>
      <td>0.447263</td>
      <td>0.150672</td>
      <td>0.093241</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.814119</td>
      <td>0.034705</td>
      <td>0.740344</td>
      <td>0.944930</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.017390</td>
      <td>0.058722</td>
      <td>0.015387</td>
      <td>0.174923</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.305805</td>
      <td>0.053481</td>
      <td>0.509208</td>
      <td>0.897541</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.530119</td>
      <td>0.324150</td>
      <td>0.789586</td>
      <td>0.569459</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.365288</td>
      <td>0.148475</td>
      <td>0.503314</td>
      <td>0.829087</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.033251</td>
      <td>0.045697</td>
      <td>0.851344</td>
      <td>0.054292</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.470415</td>
      <td>0.480322</td>
      <td>0.959995</td>
      <td>0.960315</td>
    </tr>
  </tbody>
</table>
</div>



一组数据的面积图


```python
df4['a'].plot.area()
```




    <AxesSubplot:>





![](https://files.mdnice.com/user/33324/8084ea95-0c29-4fc3-8103-50ea857c6dbb.png)



多组数据的面积图


```python
df4[['a','b','c','d']].plot.area()
```




    <AxesSubplot:>





![](https://files.mdnice.com/user/33324/775325e8-a4f6-4109-a50b-9646b63bba21.png)



#### scatter：散点图

散点图显示两个连续型变量之间的关系和探索离群值。对于相关性，散点图有助于显示两个变量之间线性关系的强度。对于回归，散点图常常会添加拟合线。

```python
np.random.seed(123)
df = pd.DataFrame(np.random.randn(10,2),columns = ['B','C']).cumsum()
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
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.085631</td>
      <td>0.997345</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.802652</td>
      <td>-0.508949</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-1.381252</td>
      <td>1.142487</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-3.807932</td>
      <td>0.713575</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-2.541995</td>
      <td>-0.153166</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-3.220881</td>
      <td>-0.247875</td>
    </tr>
    <tr>
      <th>6</th>
      <td>-1.729492</td>
      <td>-0.886777</td>
    </tr>
    <tr>
      <th>7</th>
      <td>-2.173474</td>
      <td>-1.321128</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.032456</td>
      <td>0.865658</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1.036510</td>
      <td>1.251844</td>
    </tr>
  </tbody>
</table>
</div>


看一下这两列数据的散点图


```python
df['A'] = pd.Series(list(range(len(df))))
df.assign(avg = df.mean(1)).plot.scatter(x='C',
                                         y = 'B')
```




    <AxesSubplot:xlabel='C', ylabel='B'>



![](https://files.mdnice.com/user/33324/33f55506-cc1d-4f1f-b7e8-65c86f61f5e1.png)


至此，Python基础部分pandas常用的内容就告一段落了。

**致谢**

《Python数据分析极简入门》图文系列教程的写作过程中参考了诸多经典书籍，包括:

Wes McKinney 的《利用Python做数据分析》;

小甲鱼老师的《零基础入门学习Python》；

李庆辉老师的 《深入浅出Pandas》;

在此一并感谢以上内容的作者！

> 怕什么真理无穷,进一寸有一寸的欢喜。你每每往前进一寸，你的天空，便有一片新的明朗。你便会有一片新的开阔。诸位加油，我们下个系列见！
