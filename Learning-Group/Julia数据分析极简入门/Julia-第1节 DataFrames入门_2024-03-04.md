#  Julia数据分析极简入门

![](https://julia.mit.edu/assets/images/julia-lab-logo.svg)

- DataFrames入门
- 使用数据框
- 导入和导出数据 (I/O)
- 数据拼接
- 数据拆分与函数应用
- 数据重塑
- 数据排序
- 分类数据
- 缺失数据
- 数据操作框架
- 与 Python/R/Stata 的比较

<div class="alert alert-info" role="alert">
注：教程所用Julia版本为  Julia 1.5.3 
</div>

## 第1节 DataFrames入门

## `DataFrames` 安装

DataFrames 包可通过 Julia 包系统获得，并且可以使用以下命令进行安装：


```julia
# using Pkg
# Pkg.add("DataFrames")
```

在本教程接下来的部分，我们假设您已安装
DataFrames 包，并且已经输入了 `using DataFrames` 来将所有的相关变量到您当前的命名空间。
  
## `DataFrame` 类型
`DataFrame` 是一个表格型的数据结构，用向量（vectors）组成的序列（series）表示数据表，每个序列对应一列或一组变量。
最简单的`DataFrame`构造方法，是使用关键字参数或传递一对列向量：


```julia
using DataFrames 
# 引入DataFrames包
```


```julia
df = DataFrame(A=1:4, B=["M", "F", "F", "M"]) 
# 创建一个df，A列是1,2,3,4，B列是"M", "F", "F", "M"
```




<div class="data-frame"><p>4 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th title="Int64">Int64</th><th title="String">String</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>M</td></tr><tr><th>2</th><td>2</td><td>F</td></tr><tr><th>3</th><td>3</td><td>F</td></tr><tr><th>4</th><td>4</td><td>M</td></tr></tbody></table></div>



列可以通过 `df.A` 直接访问（即无需复制）、`df."A"`、`df[!, :A]` 或 `df[!, "A"]`。

后两种语法更灵活，因为它们允许传递列名，并且不仅仅是一个名称，还可以是符号（如 `df[!, :A]`、`df[!, :var"A"]` 或 `df[!, Symbol("A")]`）或字符串（如 `df[!, "A"]`）。

也可以使用整数指定其位置的索引`df[[1,3],:A]`来访问列。

由于 `df[!, :col]` 不会复制，因此更改列中元素将会改变`df`的原始值。

要获取列的副本，需要使用 `df[:, :col]`，这种方法更改列中元素不会改变 `df`。


```julia
df.A
```




    4-element Array{Int64,1}:
     1
     2
     3
     4




```julia
df."A"
```




    4-element Array{Int64,1}:
     1
     2
     3
     4




```julia
df.A === df[!, :A]
# df[!, :A]是切片，“===” 判断严格相等是true
```




    true




```julia
df.A === df[!, "A"]
# df[!, :A]是切片，“===” 判断相等是true
```




    true




```julia
df.A === df[!, 1]
# df[!, 1]是切片，“===” 判断严格相等是true
```




    true




```julia
df.A === df[:, :A]
# df[:, :A]是复制，“===” 判断严格相等是false
```




    false




```julia
df.A === df[:, "A"]
# df[:, "A"]是复制，“===” 判断严格相等是false
```




    false




```julia
df.A === df[:, 1]
# df[:, 1]是复制，“===” 判断严格相等是false
```




    false



- 总结：复制严格相等是false,切片严格相等是true


```julia
df.A == df[:, :A]
# df[!, :A]是复制，“==” 判断相等是true
```




    true




```julia
df.A == df[!, "A"]
# df[!, :A]是切片，“==” 判断相等是true
```




    true




```julia
df.A == df[:, 1]
# df[:, 1]是复制，“==” 判断相等是true
```




    true




```julia
df.A == df[!, 1]
# df[!, 1]是切片，“==” 判断相等是true
```




    true



- 总结：复制、切片 只判断相等都是true


```julia
col1 = :A
```




    :A




```julia
df[!, col1] === df.A
# 切片，“===” 判断严格相等是true
```




    true




```julia
df[:, col1] === df.A
# 复制，“===” 判断严格相等是false
```




    false




```julia
df[:, col1] == df.A
# 复制，“==” 判断严格相等是false
```




    true



列名可以使用 `names` 函数获取：


```julia
names(df)
```




    2-element Array{String,1}:
     "A"
     "B"



您还可以通过在第二个参数传递过滤条件来选择列名。
详情可参阅 [`names`](@ref) 文档字符串。
这里我们给出一些精选的例子：


```julia
names(df, r"A")    # 常用列名筛选
```




    1-element Array{String,1}:
     "A"




```julia
names(df, Int)     # 使用元素类型筛选
```




    1-element Array{String,1}:
     "A"




```julia
names(df, Not(:B)) # 除B列外反选
```




    1-element Array{String,1}:
     "A"



使用`propertynames` 函数将列名称作为 `Symbol` ：


```julia
propertynames(df)
```




    2-element Array{Symbol,1}:
     :A
     :B



<div class="alert alert-info" role="alert">
!!! note
    
    
DataFrames.jl 允许使用 `Symbol`（如 `:A`）和字符串（如 `"A"`）操作所有列索引。 
但是，使用 `Symbol`更快一点，如果不声明它们（generating），通常应该是首选通过字符串操作。
</div>




### 通过列构造新的列

也可以从一个空的 `DataFrame` 开始并一一新增列：


```julia
df = DataFrame()
```




<div class="data-frame"><p>0 rows × 0 columns</p><table class="data-frame"><thead><tr><th></th></tr><tr><th></th></tr></thead><tbody></tbody></table></div>




```julia
df.A = 1:8
```




    1:8




```julia
df.B = ["M", "F", "F", "M", "F", "M", "M", "F"]

df
```




<div class="data-frame"><p>8 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th title="Int64">Int64</th><th title="String">String</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>M</td></tr><tr><th>2</th><td>2</td><td>F</td></tr><tr><th>3</th><td>3</td><td>F</td></tr><tr><th>4</th><td>4</td><td>M</td></tr><tr><th>5</th><td>5</td><td>F</td></tr><tr><th>6</th><td>6</td><td>M</td></tr><tr><th>7</th><td>7</td><td>M</td></tr><tr><th>8</th><td>8</td><td>F</td></tr></tbody></table></div>



上面构建的 `DataFrame` 有 8 行 2 列。可以使用 `size` 函数进行查看size：


```julia
size(df, 1) #行数
```




    8




```julia
size(df, 2) #列数
```




    2




```julia
size(df)
```




    (8, 2)



### 通过行构造新的行

也可以逐行填充“DataFrame”。 让我们构造一个空的具有两列的数据框（第一列元素类型是整数，第二个元素类型是字符串）：


```julia
df = DataFrame(A=Int[], B=String[])
df
```




<div class="data-frame"><p>0 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th title="Int64">Int64</th><th title="String">String</th></tr></thead><tbody></tbody></table></div>



可以用元组或向量的形式添加行，其中元素的顺序与列的顺序需要匹配：


```julia
push!(df, (1, "M"))
```




<div class="data-frame"><p>1 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th title="Int64">Int64</th><th title="String">String</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>M</td></tr></tbody></table></div>




```julia
push!(df, [2, "N"])
```




<div class="data-frame"><p>2 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th title="Int64">Int64</th><th title="String">String</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>M</td></tr><tr><th>2</th><td>2</td><td>N</td></tr></tbody></table></div>



也可以用 `Dict`来添加行，其中字典的键与列名需要匹配：


```julia
push!(df, Dict(:B => "F", :A => 3))
```




<div class="data-frame"><p>3 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th title="Int64">Int64</th><th title="String">String</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>M</td></tr><tr><th>2</th><td>2</td><td>N</td></tr><tr><th>3</th><td>3</td><td>F</td></tr></tbody></table></div>



请注意，逐行构造“DataFrame”的性能明显低于一次全部构建，或逐列构建。对于许多用例，这无关紧要，
但对于非常大的 `DataFrame`这可能是一个需要考虑的因素。

### 通过另一个表类型构造

DataFrames 支持 [Tables.jl](https://github.com/JuliaData/Tables.jl) 接口
与表格数据交互。 这意味着“DataFrame”可以用作“源”链接到任何需要 Tables.jl 接口输入的包，（文件格式包，数据操作包等）。 `DataFrame` 也可以是任何 Tables.jl 的接收器接口输入。 一些示例如下：


```julia
df = DataFrame(a=[1, 2, 3], b=[:a, :b, :c])

# 写出 DataFrame 为 CSV 文件
# CSV.write("dataframe.csv", df)

# 存储 DataFrame 在 SQLite database 的 table里
# SQLite.load!(df, db, "dataframe_table")

# 通过 Query.jl 包转换 DataFrame  此处可能有问题，暂时没搞懂
# df = df |> @map({a=_.a + 1, _.b}) |> DataFrame
```




<div class="data-frame"><p>3 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th></tr><tr><th></th><th title="Int64">Int64</th><th title="Symbol">Symbol</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>a</td></tr><tr><th>2</th><td>2</td><td>b</td></tr><tr><th>3</th><td>3</td><td>c</td></tr></tbody></table></div>



支持[Tables.jl](https://github.com/JuliaData/Tables.jl) 类型为
`NamedTuple`的向量：


```julia
v = [(a=1, b=2), (a=3, b=4)]
v
```




    2-element Array{NamedTuple{(:a, :b),Tuple{Int64,Int64}},1}:
     (a = 1, b = 2)
     (a = 3, b = 4)




```julia
df = DataFrame(v)

```




<div class="data-frame"><p>2 rows × 2 columns</p><table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th></tr><tr><th></th><th title="Int64">Int64</th><th title="Int64">Int64</th></tr></thead><tbody><tr><th>1</th><td>1</td><td>2</td></tr><tr><th>2</th><td>3</td><td>4</td></tr></tbody></table></div>



您还可以轻松地将数据框转换回 `NamedTuple` 的向量：


```julia
using Tables

Tables.rowtable(df)
```




    2-element Array{NamedTuple{(:a, :b),Tuple{Int64,Int64}},1}:
     (a = 1, b = 2)
     (a = 3, b = 4)



### 参考链接：
- 1. Julia 的 DataFrame官方教程：https://dataframes.juliadata.org/stable/man/comparisons/
- 2. Julia 中文社区核心成员罗秀哲大佬的分享：https://www.bilibili.com/video/BV1Ms411w7Hh/
