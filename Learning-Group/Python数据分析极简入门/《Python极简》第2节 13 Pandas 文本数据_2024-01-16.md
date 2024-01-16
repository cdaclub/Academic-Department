# 《Python数据分析极简入门》

## 第3节 13 Pandas 表格样式

## Pandas 表格样式

Pandas 的样式是一个可视化的方法，像Excel一样对特定数据进行加粗、标红、背景标黄等，为了让数据更加清晰醒目，突出数据的逻辑和特征。

假如我们有这样一个`DataFrame`，我们需要通过表格样式给它做各种标注：


```python
#读取数据
import pandas as pd
import numpy as np
df = df = pd.DataFrame(
    {'A': ['孙云', '郑成', '冯敏', '王忠', '郑花', '孙华', '赵白', '王花', '黄成', '钱明', '孙宇'],
     'B': [79, 70, 39, 84, 87, 26, 29, 47, 32, 22, 99],
     'C': [28, 77, 84, 26, 29, 47, 32, 22, 99, 76, 44],
     'D': [18, 53, 78, 4, 36, 88, 79, 47, 54, 25, 14]})
df
```

![](https://files.mdnice.com/user/33324/fbd8be2a-6971-4c3c-af7d-c03f9bebb9b2.png)

#### 字体颜色

首先来看一个对文字标注颜色的例子：eg.我们想把成绩超过80的分数用红色标注出来

我们需要先定义一个函数，根据条件返回不同的颜色


```python
def color_negative_red(val):
    color = 'red' if val > 80 else 'black'
    return 'color: %s' % color
```

应用这个自定义函数后就可以得到：


```python
df.set_index('A').style.applymap(color_negative_red)
```


![](https://files.mdnice.com/user/33324/c02002f8-9614-4932-8925-9e837e509aff.png)



#### 背景高亮

接着 eg. 我们假设有学生没有去考试，想看看哪些学生没有考试，把这部分进行背景高亮显示

数据如下：


```python
df1 = df.copy()
df1.iloc[1,1] = np.NaN
df1.iloc[2,1] = np.NaN
df1
```

![](https://files.mdnice.com/user/33324/385a681e-510f-4593-81fc-2470d9554664.png)

换句话说，就是用背景高亮标记出空值，应用`.highlight_null() `即可将空值高亮显示,同时用`null_color`参数可以指定该高亮的颜色。

```python
#把空值设置高亮

df1.style.highlight_null(null_color = 'blue'#修改颜色
                       )
```
![](https://files.mdnice.com/user/33324/e4c4a3b4-e3ec-4d0d-9b20-dad85eaae916.png)
  
#### 极值背景高亮

接着我们想看看 eg. 标记出每个科目的最高分数

换句话说，需要查找DataFrame每一列的最大值，通过 highlight_max() 方法用于将最大值高亮显示，并通过color参数修改高亮颜色


```python
#设置极大值高亮
df.set_index('A').style.highlight_max(color = 'red'#修改颜色
                      )
```

![](https://files.mdnice.com/user/33324/666f45cf-41f3-4159-a2d2-c5c2102da4b8.png)

通过 `highlight_min()` 方法可以将最小值高亮显示


```python
df.set_index('A').style.highlight_min(color = 'yellow' #修改颜色
)
```

![](https://files.mdnice.com/user/33324/54979b35-5d54-4c97-898c-a27491b818da.png)

同时显示极大值和极小值，并使用指定颜色：通过 `highlight_min()` 方法和  `highlight_max()` 方法再指定一下颜色即可

```python
df.set_index('A').style.highlight_min(color = 'green').highlight_max(color = 'red')
```

![](https://files.mdnice.com/user/33324/6faeaa7e-d33d-4c28-af2f-234a1d4c05a3.png)

#### 横向对比

再来看看横向对比的例子 eg. 需要标记出每个学生的单科最高分数: 通过参数 axis ，横向对比大小，并把最大值进行高亮显示即可


```python
df.set_index('A').style.highlight_max(axis = 1)
```

![](https://files.mdnice.com/user/33324/5bfd24da-511f-4200-86f5-ae65a626b12e.png)

同样的，也可以通过参数 subset ，选定一列对最大值进行高亮显示

```python
#指定列进行比较
df.set_index('A').style.highlight_max(subset = ['B'])
```

![](https://files.mdnice.com/user/33324/92a028ac-904e-49f6-a580-b7c9b4943c98.png)

#### 背景渐变

eg. 用不同的颜色来标注成绩，背景颜色越深，成绩越高

通过调用 background_gradient() 方法，从而创建一个渐变的背景效果。


```python
df.style.background_gradient()
```

![](https://files.mdnice.com/user/33324/6797e60c-27c7-4a9c-9b1b-2d5c225ca40d.png)

同样地，针对单个列，指定颜色系列如下：


```python
df.style.background_gradient(subset = ['B'],cmap = 'BuGn')
```


![](https://files.mdnice.com/user/33324/c6a855ea-c3a9-438b-8580-c64e4eb27f52.png)

刚才我们是默认颜色渐变的范围了，接着我们来看如何指定颜色渐变的范围，来展现成绩的高低

通过调用 `background_gradient()` 方法，用了两个参数 low=0.5 和 high=0 表示渐变的起始值和结束值


```python
#低百分比和高百分比范围，更换颜色时避免使用所有色域
df.style.background_gradient(low = 0.5,high = 0)
```

![](https://files.mdnice.com/user/33324/ae77f046-4b5f-4912-b5fa-596ffd3c2969.png)

接着我们看看如何对特定范围内的值就行标注

eg. 假如需要把60分以上的分数用颜色标注出来

通过参数 vmin 和参数 vmax 设置渐变的最小值和最大值，就可以展现出来。


```python
df.style.background_gradient(vmin = 60,vmax = 100)
```


![](https://files.mdnice.com/user/33324/332a65b2-8395-42dc-bf33-5f3a4da5ca05.png)

eg. 用此次考试成绩表，添加标题

通过.set_caption() 方法为DataFrame 即可设置标题。


```python
#添加标题
df.style.set_caption("三年级二班学生成绩表")
```

![](https://files.mdnice.com/user/33324/d597c4ae-59e8-4f15-8a42-32f4b3e1295b.png)

通过以上内容的学习，我们快速学习Pandas样式的基本操作，接下来，再用两个案例详细说明一下

案例一：将科目分数小于60的值，用红色进行高亮显示


```python
#将学生没有及格的科目标记为红色
df.style.applymap(lambda x: 'background-color:red' if x<60 else '', subset = pd.IndexSlice[:,['B','C','D']])
```

![](https://files.mdnice.com/user/33324/637d4c12-9714-49de-ab96-220e7638752e.png)

案例二：标记总分低于120分的分数

将每个学生的分数，进行加总和计算平均数，并保留两位小数,把分数低于120的学生，用红色进行标记即可


```python
#通过使用.assign() 来计算学生三门课程的总分和平均值
(df.set_index('A').assign(sum_s = df.set_index('A').sum(axis = 1))
    .style.applymap(lambda x: 'background-color:red' if x<120 else '',subset = pd.IndexSlice[:,['sum_s']])
    .format({'avg':"{:.2f}"}))
```

![](https://files.mdnice.com/user/33324/51e5c337-9e62-4514-ab14-b99732df27bd.png)









