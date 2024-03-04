#  Julia数据分析极简入门

## 第2节 DataFrames基础

## 数据查看
`DataFrame`  默认输出部分行和列：


```julia
using Pkg
```


```julia
# Pkg.add("DataFrames")
# # Pkg.rm("DataFrames")
```


```julia
# using Pkg
# Pkg.status("DataFrames")
```


```julia
using DataFrames;
using CSV;
using SQLite
```


```julia
df = DataFrame(A=1:2:1000, B=repeat(1:10, inner=50), C=1:500)
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>500 rows × 3 columns</p><tr><th>1</th><td>1</td><td>1</td><td>1</td></tr><tr><th>2</th><td>3</td><td>1</td><td>2</td></tr><tr><th>3</th><td>5</td><td>1</td><td>3</td></tr><tr><th>4</th><td>7</td><td>1</td><td>4</td></tr><tr><th>5</th><td>9</td><td>1</td><td>5</td></tr><tr><th>6</th><td>11</td><td>1</td><td>6</td></tr><tr><th>7</th><td>13</td><td>1</td><td>7</td></tr><tr><th>8</th><td>15</td><td>1</td><td>8</td></tr><tr><th>9</th><td>17</td><td>1</td><td>9</td></tr><tr><th>10</th><td>19</td><td>1</td><td>10</td></tr><tr><th>11</th><td>21</td><td>1</td><td>11</td></tr><tr><th>12</th><td>23</td><td>1</td><td>12</td></tr><tr><th>13</th><td>25</td><td>1</td><td>13</td></tr><tr><th>14</th><td>27</td><td>1</td><td>14</td></tr><tr><th>15</th><td>29</td><td>1</td><td>15</td></tr><tr><th>16</th><td>31</td><td>1</td><td>16</td></tr><tr><th>17</th><td>33</td><td>1</td><td>17</td></tr><tr><th>18</th><td>35</td><td>1</td><td>18</td></tr><tr><th>19</th><td>37</td><td>1</td><td>19</td></tr><tr><th>20</th><td>39</td><td>1</td><td>20</td></tr><tr><th>21</th><td>41</td><td>1</td><td>21</td></tr><tr><th>22</th><td>43</td><td>1</td><td>22</td></tr><tr><th>23</th><td>45</td><td>1</td><td>23</td></tr><tr><th>24</th><td>47</td><td>1</td><td>24</td></tr><tr><th>25</th><td>49</td><td>1</td><td>25</td></tr><tr><th>26</th><td>51</td><td>1</td><td>26</td></tr><tr><th>27</th><td>53</td><td>1</td><td>27</td></tr><tr><th>28</th><td>55</td><td>1</td><td>28</td></tr><tr><th>29</th><td>57</td><td>1</td><td>29</td></tr><tr><th>30</th><td>59</td><td>1</td><td>30</td></tr><tr><th>&vellip;</th><td>&vellip;</td><td>&vellip;</td><td>&vellip;</td></tr></tbody></table>



可以通过`show` 函数手动调整打印选项：
  - `show(df, allrows=true)` 打印所有行
  - `show(df, allcols=true)` 打印所有列

`first` 和 `last` 函数可用于查看第一行和最后一行数据框的（分别）：


```julia
first(df, 6)
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>6 rows × 3 columns</p><tr><th>1</th><td>1</td><td>1</td><td>1</td></tr><tr><th>2</th><td>3</td><td>1</td><td>2</td></tr><tr><th>3</th><td>5</td><td>1</td><td>3</td></tr><tr><th>4</th><td>7</td><td>1</td><td>4</td></tr><tr><th>5</th><td>9</td><td>1</td><td>5</td></tr><tr><th>6</th><td>11</td><td>1</td><td>6</td></tr></tbody></table>




```julia
last(df, 6)
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>6 rows × 3 columns</p><tr><th>1</th><td>989</td><td>10</td><td>495</td></tr><tr><th>2</th><td>991</td><td>10</td><td>496</td></tr><tr><th>3</th><td>993</td><td>10</td><td>497</td></tr><tr><th>4</th><td>995</td><td>10</td><td>498</td></tr><tr><th>5</th><td>997</td><td>10</td><td>499</td></tr><tr><th>6</th><td>999</td><td>10</td><td>500</td></tr></tbody></table>



另请注意，当`DataFrame` 被print到控制台或以HTML呈现时（例如在Jupyter Notebook中），您可以获得有关其列中元素类型的信息。例如


```julia
using CategoricalArrays
```


```julia
DataFrame(a=1:2, b=[1.0, missing],
                 c=categorical('a':'b'), d=[1//2, missing])
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>Int64</th><th>Float64?</th><th>Cat…</th><th>Rationa…?</th></tr></thead><tbody><p>2 rows × 4 columns</p><tr><th>1</th><td>1</td><td>1.0</td><td>'a'</td><td>1//2</td></tr><tr><th>2</th><td>2</td><td><em>missing</em></td><td>'b'</td><td><em>missing</em></td></tr></tbody></table>



我们可以观察到：

* 第一列 `:a` 中元素类型为 `Int64`;
* 第二列 `:b` 中元素类型为 `Float64` or `Missing`,`?`类型的名称会在print后显示;
* 第三列 `:c` 中元素类型为 categorical data; 这里我们注意到 `…`, 这表明由于该类型的实际名称太长而被截断了;
* 第四列 `:d` 中名称被截断并且该类型允许`Missing`.

## 获取子集（subset子集）

### 通过索引方式

使用索引取数据框的子集类似于矩阵。在手册的索引部分[Indexing](@ref) 中，您可以找到有关可用选项的所有详细信息。在这里，我们重点介绍基本选项。

 `:`表示应保留所有项（行或列，具体取决于其位置）:


```julia
df[1:3, :]
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>3 rows × 3 columns</p><tr><th>1</th><td>1</td><td>1</td><td>1</td></tr><tr><th>2</th><td>3</td><td>1</td><td>2</td></tr><tr><th>3</th><td>5</td><td>1</td><td>3</td></tr></tbody></table>




```julia
df[[1, 5, 10], :]
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>3 rows × 3 columns</p><tr><th>1</th><td>1</td><td>1</td><td>1</td></tr><tr><th>2</th><td>9</td><td>1</td><td>5</td></tr><tr><th>3</th><td>19</td><td>1</td><td>10</td></tr></tbody></table>




```julia
df[:, [:A, :B]]
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>500 rows × 2 columns</p><tr><th>1</th><td>1</td><td>1</td></tr><tr><th>2</th><td>3</td><td>1</td></tr><tr><th>3</th><td>5</td><td>1</td></tr><tr><th>4</th><td>7</td><td>1</td></tr><tr><th>5</th><td>9</td><td>1</td></tr><tr><th>6</th><td>11</td><td>1</td></tr><tr><th>7</th><td>13</td><td>1</td></tr><tr><th>8</th><td>15</td><td>1</td></tr><tr><th>9</th><td>17</td><td>1</td></tr><tr><th>10</th><td>19</td><td>1</td></tr><tr><th>11</th><td>21</td><td>1</td></tr><tr><th>12</th><td>23</td><td>1</td></tr><tr><th>13</th><td>25</td><td>1</td></tr><tr><th>14</th><td>27</td><td>1</td></tr><tr><th>15</th><td>29</td><td>1</td></tr><tr><th>16</th><td>31</td><td>1</td></tr><tr><th>17</th><td>33</td><td>1</td></tr><tr><th>18</th><td>35</td><td>1</td></tr><tr><th>19</th><td>37</td><td>1</td></tr><tr><th>20</th><td>39</td><td>1</td></tr><tr><th>21</th><td>41</td><td>1</td></tr><tr><th>22</th><td>43</td><td>1</td></tr><tr><th>23</th><td>45</td><td>1</td></tr><tr><th>24</th><td>47</td><td>1</td></tr><tr><th>25</th><td>49</td><td>1</td></tr><tr><th>26</th><td>51</td><td>1</td></tr><tr><th>27</th><td>53</td><td>1</td></tr><tr><th>28</th><td>55</td><td>1</td></tr><tr><th>29</th><td>57</td><td>1</td></tr><tr><th>30</th><td>59</td><td>1</td></tr><tr><th>&vellip;</th><td>&vellip;</td><td>&vellip;</td></tr></tbody></table>




```julia
df[1:3, [:B, :A]]
```




<table class="data-frame"><thead><tr><th></th><th>B</th><th>A</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>3 rows × 2 columns</p><tr><th>1</th><td>1</td><td>1</td></tr><tr><th>2</th><td>1</td><td>3</td></tr><tr><th>3</th><td>1</td><td>5</td></tr></tbody></table>




```julia
df[[3, 1], [:C]]
```




<table class="data-frame"><thead><tr><th></th><th>C</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>2 rows × 1 columns</p><tr><th>1</th><td>3</td></tr><tr><th>2</th><td>1</td></tr></tbody></table>



请注意 `df[!, [:A]]` and `df[:, [:A]]` 会返回一个 `DataFrame` 对象, 而`df[!, :A]` and `df[:, :A]` 会返回一个向量:


```julia
df[!, [:A]]
```




<table class="data-frame"><thead><tr><th></th><th>A</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>500 rows × 1 columns</p><tr><th>1</th><td>1</td></tr><tr><th>2</th><td>3</td></tr><tr><th>3</th><td>5</td></tr><tr><th>4</th><td>7</td></tr><tr><th>5</th><td>9</td></tr><tr><th>6</th><td>11</td></tr><tr><th>7</th><td>13</td></tr><tr><th>8</th><td>15</td></tr><tr><th>9</th><td>17</td></tr><tr><th>10</th><td>19</td></tr><tr><th>11</th><td>21</td></tr><tr><th>12</th><td>23</td></tr><tr><th>13</th><td>25</td></tr><tr><th>14</th><td>27</td></tr><tr><th>15</th><td>29</td></tr><tr><th>16</th><td>31</td></tr><tr><th>17</th><td>33</td></tr><tr><th>18</th><td>35</td></tr><tr><th>19</th><td>37</td></tr><tr><th>20</th><td>39</td></tr><tr><th>21</th><td>41</td></tr><tr><th>22</th><td>43</td></tr><tr><th>23</th><td>45</td></tr><tr><th>24</th><td>47</td></tr><tr><th>25</th><td>49</td></tr><tr><th>26</th><td>51</td></tr><tr><th>27</th><td>53</td></tr><tr><th>28</th><td>55</td></tr><tr><th>29</th><td>57</td></tr><tr><th>30</th><td>59</td></tr><tr><th>&vellip;</th><td>&vellip;</td></tr></tbody></table>




```julia
df[!, [:A]] == df[:, [:A]]
```




    true




```julia
df[!, :A]
```




    500-element Array{Int64,1}:
       1
       3
       5
       7
       9
      11
      13
      15
      17
      19
      21
      23
      25
       ⋮
     977
     979
     981
     983
     985
     987
     989
     991
     993
     995
     997
     999




```julia
df[!, :A] == df[:, :A]
```




    true



在第一种情况下，列索引`[:A]` 是一个向量，所以生成的对象应该是一个  `DataFrame`。

在第二种情况下，列索引  `:A`是单个符号，表示应提取单列向量。

请注意，在第一种情况下，需要传递一个向量（而不仅仅是任何可迭代的对象），因此，例如`df[:, (:x1,:x2)]`是不允许的，但是`df[:, [:x1, :x2]]` 是可以的。


也可以使用正则表达式作选择器：


```julia
df = DataFrame(x1=1, x2=2, y=3)
```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>1 rows × 3 columns</p><tr><th>1</th><td>1</td><td>2</td><td>3</td></tr></tbody></table>




```julia
df[!, r"x"]
```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>1 rows × 2 columns</p><tr><th>1</th><td>1</td><td>2</td></tr></tbody></table>



`Not` 选择器 (来自索引倒排包
[InvertedIndices](https://github.com/mbauman/InvertedIndices.jl) )可用于选择除特定子集之外的所有列:


```julia
df[!, Not(:x1)]
```




<table class="data-frame"><thead><tr><th></th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>1 rows × 2 columns</p><tr><th>1</th><td>2</td><td>3</td></tr></tbody></table>



最后，可以在更复杂的列选择方案中使用`Not`, `Between`, `Cols` 和 `All`选择器。（请注意，如果编写泛型代码， `All()`会选择所有列，而`Cols()`不选择任何列，因此是首选选择器）。以下示例：


```julia
df = DataFrame(r=1, x1=2, x2=3, y=4)
```




<table class="data-frame"><thead><tr><th></th><th>r</th><th>x1</th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>1 rows × 4 columns</p><tr><th>1</th><td>1</td><td>2</td><td>3</td><td>4</td></tr></tbody></table>




```julia
df[:, Not(:r)] # 删除 :r 列
```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>1 rows × 3 columns</p><tr><th>1</th><td>2</td><td>3</td><td>4</td></tr></tbody></table>




```julia
df[:, All()] # keep all columns
```




<table class="data-frame"><thead><tr><th></th><th>r</th><th>x1</th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>1 rows × 4 columns</p><tr><th>1</th><td>1</td><td>2</td><td>3</td><td>4</td></tr></tbody></table>



索引方式还可以根据条件表达式选择行：


```julia
df = DataFrame(A=1:2:1000, B=repeat(1:10, inner=50), C=1:500)
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>500 rows × 3 columns</p><tr><th>1</th><td>1</td><td>1</td><td>1</td></tr><tr><th>2</th><td>3</td><td>1</td><td>2</td></tr><tr><th>3</th><td>5</td><td>1</td><td>3</td></tr><tr><th>4</th><td>7</td><td>1</td><td>4</td></tr><tr><th>5</th><td>9</td><td>1</td><td>5</td></tr><tr><th>6</th><td>11</td><td>1</td><td>6</td></tr><tr><th>7</th><td>13</td><td>1</td><td>7</td></tr><tr><th>8</th><td>15</td><td>1</td><td>8</td></tr><tr><th>9</th><td>17</td><td>1</td><td>9</td></tr><tr><th>10</th><td>19</td><td>1</td><td>10</td></tr><tr><th>11</th><td>21</td><td>1</td><td>11</td></tr><tr><th>12</th><td>23</td><td>1</td><td>12</td></tr><tr><th>13</th><td>25</td><td>1</td><td>13</td></tr><tr><th>14</th><td>27</td><td>1</td><td>14</td></tr><tr><th>15</th><td>29</td><td>1</td><td>15</td></tr><tr><th>16</th><td>31</td><td>1</td><td>16</td></tr><tr><th>17</th><td>33</td><td>1</td><td>17</td></tr><tr><th>18</th><td>35</td><td>1</td><td>18</td></tr><tr><th>19</th><td>37</td><td>1</td><td>19</td></tr><tr><th>20</th><td>39</td><td>1</td><td>20</td></tr><tr><th>21</th><td>41</td><td>1</td><td>21</td></tr><tr><th>22</th><td>43</td><td>1</td><td>22</td></tr><tr><th>23</th><td>45</td><td>1</td><td>23</td></tr><tr><th>24</th><td>47</td><td>1</td><td>24</td></tr><tr><th>25</th><td>49</td><td>1</td><td>25</td></tr><tr><th>26</th><td>51</td><td>1</td><td>26</td></tr><tr><th>27</th><td>53</td><td>1</td><td>27</td></tr><tr><th>28</th><td>55</td><td>1</td><td>28</td></tr><tr><th>29</th><td>57</td><td>1</td><td>29</td></tr><tr><th>30</th><td>59</td><td>1</td><td>30</td></tr><tr><th>&vellip;</th><td>&vellip;</td><td>&vellip;</td><td>&vellip;</td></tr></tbody></table>




```julia
df[df.A .> 500, :]
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>250 rows × 3 columns</p><tr><th>1</th><td>501</td><td>6</td><td>251</td></tr><tr><th>2</th><td>503</td><td>6</td><td>252</td></tr><tr><th>3</th><td>505</td><td>6</td><td>253</td></tr><tr><th>4</th><td>507</td><td>6</td><td>254</td></tr><tr><th>5</th><td>509</td><td>6</td><td>255</td></tr><tr><th>6</th><td>511</td><td>6</td><td>256</td></tr><tr><th>7</th><td>513</td><td>6</td><td>257</td></tr><tr><th>8</th><td>515</td><td>6</td><td>258</td></tr><tr><th>9</th><td>517</td><td>6</td><td>259</td></tr><tr><th>10</th><td>519</td><td>6</td><td>260</td></tr><tr><th>11</th><td>521</td><td>6</td><td>261</td></tr><tr><th>12</th><td>523</td><td>6</td><td>262</td></tr><tr><th>13</th><td>525</td><td>6</td><td>263</td></tr><tr><th>14</th><td>527</td><td>6</td><td>264</td></tr><tr><th>15</th><td>529</td><td>6</td><td>265</td></tr><tr><th>16</th><td>531</td><td>6</td><td>266</td></tr><tr><th>17</th><td>533</td><td>6</td><td>267</td></tr><tr><th>18</th><td>535</td><td>6</td><td>268</td></tr><tr><th>19</th><td>537</td><td>6</td><td>269</td></tr><tr><th>20</th><td>539</td><td>6</td><td>270</td></tr><tr><th>21</th><td>541</td><td>6</td><td>271</td></tr><tr><th>22</th><td>543</td><td>6</td><td>272</td></tr><tr><th>23</th><td>545</td><td>6</td><td>273</td></tr><tr><th>24</th><td>547</td><td>6</td><td>274</td></tr><tr><th>25</th><td>549</td><td>6</td><td>275</td></tr><tr><th>26</th><td>551</td><td>6</td><td>276</td></tr><tr><th>27</th><td>553</td><td>6</td><td>277</td></tr><tr><th>28</th><td>555</td><td>6</td><td>278</td></tr><tr><th>29</th><td>557</td><td>6</td><td>279</td></tr><tr><th>30</th><td>559</td><td>6</td><td>280</td></tr><tr><th>&vellip;</th><td>&vellip;</td><td>&vellip;</td><td>&vellip;</td></tr></tbody></table>




```julia
df[(df.A .> 500) .& (300 .< df.C .< 400), :]
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>99 rows × 3 columns</p><tr><th>1</th><td>601</td><td>7</td><td>301</td></tr><tr><th>2</th><td>603</td><td>7</td><td>302</td></tr><tr><th>3</th><td>605</td><td>7</td><td>303</td></tr><tr><th>4</th><td>607</td><td>7</td><td>304</td></tr><tr><th>5</th><td>609</td><td>7</td><td>305</td></tr><tr><th>6</th><td>611</td><td>7</td><td>306</td></tr><tr><th>7</th><td>613</td><td>7</td><td>307</td></tr><tr><th>8</th><td>615</td><td>7</td><td>308</td></tr><tr><th>9</th><td>617</td><td>7</td><td>309</td></tr><tr><th>10</th><td>619</td><td>7</td><td>310</td></tr><tr><th>11</th><td>621</td><td>7</td><td>311</td></tr><tr><th>12</th><td>623</td><td>7</td><td>312</td></tr><tr><th>13</th><td>625</td><td>7</td><td>313</td></tr><tr><th>14</th><td>627</td><td>7</td><td>314</td></tr><tr><th>15</th><td>629</td><td>7</td><td>315</td></tr><tr><th>16</th><td>631</td><td>7</td><td>316</td></tr><tr><th>17</th><td>633</td><td>7</td><td>317</td></tr><tr><th>18</th><td>635</td><td>7</td><td>318</td></tr><tr><th>19</th><td>637</td><td>7</td><td>319</td></tr><tr><th>20</th><td>639</td><td>7</td><td>320</td></tr><tr><th>21</th><td>641</td><td>7</td><td>321</td></tr><tr><th>22</th><td>643</td><td>7</td><td>322</td></tr><tr><th>23</th><td>645</td><td>7</td><td>323</td></tr><tr><th>24</th><td>647</td><td>7</td><td>324</td></tr><tr><th>25</th><td>649</td><td>7</td><td>325</td></tr><tr><th>26</th><td>651</td><td>7</td><td>326</td></tr><tr><th>27</th><td>653</td><td>7</td><td>327</td></tr><tr><th>28</th><td>655</td><td>7</td><td>328</td></tr><tr><th>29</th><td>657</td><td>7</td><td>329</td></tr><tr><th>30</th><td>659</td><td>7</td><td>330</td></tr><tr><th>&vellip;</th><td>&vellip;</td><td>&vellip;</td><td>&vellip;</td></tr></tbody></table>



如果需要匹配特定值的子集，则可以用`in()`函数:


```julia
df[in.(df.A, Ref([1, 5, 601])), :]
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th><th>C</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>3 rows × 3 columns</p><tr><th>1</th><td>1</td><td>1</td><td>1</td></tr><tr><th>2</th><td>5</td><td>1</td><td>3</td></tr><tr><th>3</th><td>601</td><td>7</td><td>301</td></tr></tbody></table>



等效地，可以使用单个参数调用 `in` 创建的函数对象，该对象测试每个值是否属于子集（`in`的部分应用）：。`df[in([1, 5, 601]).(df.A), :]`


!!! 注意

与矩阵一样，数据框的子集通常返回列的副本，而不是视图或直接引用。

数据框**不会**返回副本的唯一索引情况是:

- 当 `!` 在第一个索引位置(`df[!, :A]`, 或 `df[!, [:A, :B]]`),
- 当使用`.` (`getpropery`) 标记 (`df.A`),
- 当使用整数 (`df[1, [:A, :B]]`)
- 当使用`view` or `@view`  (e.g. `@view df[1:3, :A]`).

有关副本、视图和引用的更多详细信息，请参阅 [`getindex` and `view`](@ref) 部分.

### 选择和转换列
Selecting and transforming columns


您还可以使用[`select`](@ref)/[`select!`](@ref) 和 [`transform`](@ref)/[`transform!`](@ref) 函数来选择、重命名和转换数据框中的列。

 `select` 函数将创建一个新的数据框:


```julia
df = DataFrame(x1=[1, 2], x2=[3, 4], y=[5, 6])
```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 3 columns</p><tr><th>1</th><td>1</td><td>3</td><td>5</td></tr><tr><th>2</th><td>2</td><td>4</td><td>6</td></tr></tbody></table>




```julia
select(df, Not(:x1)) # drop column :x1 in a new data frame
```




<table class="data-frame"><thead><tr><th></th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 2 columns</p><tr><th>1</th><td>3</td><td>5</td></tr><tr><th>2</th><td>4</td><td>6</td></tr></tbody></table>




```julia
select(df, r"x") # select columns containing 'x' character
```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 2 columns</p><tr><th>1</th><td>1</td><td>3</td></tr><tr><th>2</th><td>2</td><td>4</td></tr></tbody></table>




```julia
select(df, :x1 => :a1, :x2 => :a2) # rename columns
```




<table class="data-frame"><thead><tr><th></th><th>a1</th><th>a2</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 2 columns</p><tr><th>1</th><td>1</td><td>3</td></tr><tr><th>2</th><td>2</td><td>4</td></tr></tbody></table>




```julia
select(df, :x1, :x2 => (x -> x .- minimum(x)) => :x2) # transform columns
```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 2 columns</p><tr><th>1</th><td>1</td><td>0</td></tr><tr><th>2</th><td>2</td><td>1</td></tr></tbody></table>




```julia
select(df, :x2, :x2 => ByRow(sqrt)) # transform columns by row
```




<table class="data-frame"><thead><tr><th></th><th>x2</th><th>x2_sqrt</th></tr><tr><th></th><th>Int64</th><th>Float64</th></tr></thead><tbody><p>2 rows × 2 columns</p><tr><th>1</th><td>3</td><td>1.73205</td></tr><tr><th>2</th><td>4</td><td>2.0</td></tr></tbody></table>



请务必注意，`select` 即使选择了单个列（与索引语法相反），也始终返回数据框。


```julia
select(df, :x1)
```




<table class="data-frame"><thead><tr><th></th><th>x1</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>2 rows × 1 columns</p><tr><th>1</th><td>1</td></tr><tr><th>2</th><td>2</td></tr></tbody></table>




```julia
df[:, :x1]
```




    2-element Array{Int64,1}:
     1
     2



`select`默认会复制源数据框的列。为避免复制，请通过： `copycols=false`:


```julia
df2 = select(df, :x1)
```




<table class="data-frame"><thead><tr><th></th><th>x1</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>2 rows × 1 columns</p><tr><th>1</th><td>1</td></tr><tr><th>2</th><td>2</td></tr></tbody></table>




```julia
df2.x1 === df.x1
```




    false




```julia
df2 = select(df, :x1, copycols=false)
```




<table class="data-frame"><thead><tr><th></th><th>x1</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>2 rows × 1 columns</p><tr><th>1</th><td>1</td></tr><tr><th>2</th><td>2</td></tr></tbody></table>




```julia
df2.x1 === df.x1
```




    true



要直接执行选择操作in-place，请使用：`select!`


```julia
select!(df, Not(:x1));

df
```




<table class="data-frame"><thead><tr><th></th><th>x2</th><th>y</th></tr><tr><th></th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 2 columns</p><tr><th>1</th><td>3</td><td>5</td></tr><tr><th>2</th><td>4</td><td>6</td></tr></tbody></table>



`transform`和`transform!`函数的工作方式与`select`和`select!`相同，唯一的区别是它们保留源数据框中存在的所有列。下面是一些更高级的示例。

首先，我们展示如何使用 `All()`选择器生成一个列，该列是数据框中所有其他列的总和：


```julia
df = DataFrame(x1=[1, 2], x2=[3, 4], y=[5, 6])


transform(df, All() => +)

```




<table class="data-frame"><thead><tr><th></th><th>x1</th><th>x2</th><th>y</th><th>x1_x2_y_+</th></tr><tr><th></th><th>Int64</th><th>Int64</th><th>Int64</th><th>Int64</th></tr></thead><tbody><p>2 rows × 4 columns</p><tr><th>1</th><td>1</td><td>3</td><td>5</td><td>9</td></tr><tr><th>2</th><td>2</td><td>4</td><td>6</td><td>12</td></tr></tbody></table>



使用`ByRow`包装器，我们可以很容易地获取每行中得分最高的列的名称


```julia
using Random

Random.seed!(1);
```


```julia
df = DataFrame(rand(10, 3), [:a, :b, :c])
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th></tr><tr><th></th><th>Float64</th><th>Float64</th><th>Float64</th></tr></thead><tbody><p>10 rows × 3 columns</p><tr><th>1</th><td>0.236033</td><td>0.555751</td><td>0.0769509</td></tr><tr><th>2</th><td>0.346517</td><td>0.437108</td><td>0.640396</td></tr><tr><th>3</th><td>0.312707</td><td>0.424718</td><td>0.873544</td></tr><tr><th>4</th><td>0.00790928</td><td>0.773223</td><td>0.278582</td></tr><tr><th>5</th><td>0.488613</td><td>0.28119</td><td>0.751313</td></tr><tr><th>6</th><td>0.210968</td><td>0.209472</td><td>0.644883</td></tr><tr><th>7</th><td>0.951916</td><td>0.251379</td><td>0.0778264</td></tr><tr><th>8</th><td>0.999905</td><td>0.0203749</td><td>0.848185</td></tr><tr><th>9</th><td>0.251662</td><td>0.287702</td><td>0.0856352</td></tr><tr><th>10</th><td>0.986666</td><td>0.859512</td><td>0.553206</td></tr></tbody></table>




```julia
transform(df, AsTable(:) => ByRow(argmax) => :prediction)

```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>prediction</th></tr><tr><th></th><th>Float64</th><th>Float64</th><th>Float64</th><th>Symbol</th></tr></thead><tbody><p>10 rows × 4 columns</p><tr><th>1</th><td>0.236033</td><td>0.555751</td><td>0.0769509</td><td>b</td></tr><tr><th>2</th><td>0.346517</td><td>0.437108</td><td>0.640396</td><td>c</td></tr><tr><th>3</th><td>0.312707</td><td>0.424718</td><td>0.873544</td><td>c</td></tr><tr><th>4</th><td>0.00790928</td><td>0.773223</td><td>0.278582</td><td>b</td></tr><tr><th>5</th><td>0.488613</td><td>0.28119</td><td>0.751313</td><td>c</td></tr><tr><th>6</th><td>0.210968</td><td>0.209472</td><td>0.644883</td><td>c</td></tr><tr><th>7</th><td>0.951916</td><td>0.251379</td><td>0.0778264</td><td>a</td></tr><tr><th>8</th><td>0.999905</td><td>0.0203749</td><td>0.848185</td><td>a</td></tr><tr><th>9</th><td>0.251662</td><td>0.287702</td><td>0.0856352</td><td>b</td></tr><tr><th>10</th><td>0.986666</td><td>0.859512</td><td>0.553206</td><td>a</td></tr></tbody></table>



在下面这个复杂的示例中，我们计算按行求和、元素个数和平均值，同时忽略缺失值。


```julia
using Statistics

df = DataFrame(x=[1, 2, missing], y=[1, missing, missing])
```




<table class="data-frame"><thead><tr><th></th><th>x</th><th>y</th></tr><tr><th></th><th>Int64?</th><th>Int64?</th></tr></thead><tbody><p>3 rows × 2 columns</p><tr><th>1</th><td>1</td><td>1</td></tr><tr><th>2</th><td>2</td><td><em>missing</em></td></tr><tr><th>3</th><td><em>missing</em></td><td><em>missing</em></td></tr></tbody></table>




```julia
transform(df, AsTable(:) .=>
                     ByRow.([sum∘skipmissing,
                             x -> count(!ismissing, x),
                             mean∘skipmissing]) .=>
                     [:sum, :n, :mean])
```




<table class="data-frame"><thead><tr><th></th><th>x</th><th>y</th><th>sum</th><th>n</th><th>mean</th></tr><tr><th></th><th>Int64?</th><th>Int64?</th><th>Int64</th><th>Int64</th><th>Float64</th></tr></thead><tbody><p>3 rows × 5 columns</p><tr><th>1</th><td>1</td><td>1</td><td>2</td><td>2</td><td>1.0</td></tr><tr><th>2</th><td>2</td><td><em>missing</em></td><td>2</td><td>1</td><td>2.0</td></tr><tr><th>3</th><td><em>missing</em></td><td><em>missing</em></td><td>0</td><td>0</td><td>NaN</td></tr></tbody></table>



虽然 DataFrames.jl 包提供了基本的数据操作功能，但鼓励用户使用查询框架实现更方便、更强大的操作：

-  [Query.jl](https://github.com/davidanthoff/Query.jl)包为大量数据源提供了类似[LINQ](https://en.wikipedia.org/wiki/Language_Integrated_Query)的接口
- [DataFramesMeta.jl](https://github.com/JuliaStats/DataFramesMeta.jl)包提供了类似于 LINQ 和 [dplyr](https://dplyr.tidyverse.org)的接口。
有关详细信息，请参阅[Data manipulation frameworks](@ref)部分。

## 汇总数据
Summarizing Data


`describe` 函数返回一个数据框，汇总有关每列的基本统计信息：


```julia
df = DataFrame(A=1:4, B=["M", "F", "F", "M"])
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th>Int64</th><th>String</th></tr></thead><tbody><p>4 rows × 2 columns</p><tr><th>1</th><td>1</td><td>M</td></tr><tr><th>2</th><td>2</td><td>F</td></tr><tr><th>3</th><td>3</td><td>F</td></tr><tr><th>4</th><td>4</td><td>M</td></tr></tbody></table>




```julia
describe(df)
```




<table class="data-frame"><thead><tr><th></th><th>variable</th><th>mean</th><th>min</th><th>median</th><th>max</th><th>nunique</th><th>nmissing</th><th>eltype</th></tr><tr><th></th><th>Symbol</th><th>Union…</th><th>Any</th><th>Union…</th><th>Any</th><th>Union…</th><th>Nothing</th><th>DataType</th></tr></thead><tbody><p>2 rows × 8 columns</p><tr><th>1</th><td>A</td><td>2.5</td><td>1</td><td>2.5</td><td>4</td><td></td><td></td><td>Int64</td></tr><tr><th>2</th><td>B</td><td></td><td>F</td><td></td><td>M</td><td>2</td><td></td><td>String</td></tr></tbody></table>



如果您只想描述列的子集，那么最简单的方法是将原始数据框的子集传递给 `describe`， 如下：


```julia
describe(df[!, [:A]])
```




<table class="data-frame"><thead><tr><th></th><th>variable</th><th>mean</th><th>min</th><th>median</th><th>max</th><th>nunique</th><th>nmissing</th><th>eltype</th></tr><tr><th></th><th>Symbol</th><th>Float64</th><th>Int64</th><th>Float64</th><th>Int64</th><th>Nothing</th><th>Nothing</th><th>DataType</th></tr></thead><tbody><p>1 rows × 8 columns</p><tr><th>1</th><td>A</td><td>2.5</td><td>1</td><td>2.5</td><td>4</td><td></td><td></td><td>Int64</td></tr></tbody></table>



当然，也可以直接在各个列上计算描述性统计量：


```julia
using Statistics

```


```julia
mean(df.A)
```




    2.5



我们还可以通过`combine`对`DataFrame` 的列应用函数。例如：


```julia
df = DataFrame(A=1:4, B=4.0:-1.0:1.0)
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th>Int64</th><th>Float64</th></tr></thead><tbody><p>4 rows × 2 columns</p><tr><th>1</th><td>1</td><td>4.0</td></tr><tr><th>2</th><td>2</td><td>3.0</td></tr><tr><th>3</th><td>3</td><td>2.0</td></tr><tr><th>4</th><td>4</td><td>1.0</td></tr></tbody></table>




```julia
combine(df, names(df) .=> sum)
```




<table class="data-frame"><thead><tr><th></th><th>A_sum</th><th>B_sum</th></tr><tr><th></th><th>Int64</th><th>Float64</th></tr></thead><tbody><p>1 rows × 2 columns</p><tr><th>1</th><td>10</td><td>10.0</td></tr></tbody></table>




```julia
combine(df, names(df) .=> sum, names(df) .=> prod)
```




<table class="data-frame"><thead><tr><th></th><th>A_sum</th><th>B_sum</th><th>A_prod</th><th>B_prod</th></tr><tr><th></th><th>Int64</th><th>Float64</th><th>Int64</th><th>Float64</th></tr></thead><tbody><p>1 rows × 4 columns</p><tr><th>1</th><td>10</td><td>10.0</td><td>24</td><td>24.0</td></tr></tbody></table>



如果希望结果具有与源数据框相同的行数，请使用`select` 代替 `combine` 。

## 处理存储在数据帧中的列
（Handling of Columns Stored in a `DataFrame`）

默认情况下，转换生成新的 `DataFrame` 会生成列的副本，例如：


```julia
df = DataFrame(A=1:4, B=4.0:-1.0:1.0)
```




<table class="data-frame"><thead><tr><th></th><th>A</th><th>B</th></tr><tr><th></th><th>Int64</th><th>Float64</th></tr></thead><tbody><p>4 rows × 2 columns</p><tr><th>1</th><td>1</td><td>4.0</td></tr><tr><th>2</th><td>2</td><td>3.0</td></tr><tr><th>3</th><td>3</td><td>2.0</td></tr><tr><th>4</th><td>4</td><td>1.0</td></tr></tbody></table>




```julia
df2 = copy(df);
```


```julia
df2.A === df.A
```




    false



另一方面，名称以`!`结尾的`in-place`类函数可能会改变它们作为参数的 `DataFrame` 的列向量。-例如：


```julia
x = [3, 1, 2];
```


```julia
df = DataFrame(x=x)
```




<table class="data-frame"><thead><tr><th></th><th>x</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>3 rows × 1 columns</p><tr><th>1</th><td>3</td></tr><tr><th>2</th><td>1</td></tr><tr><th>3</th><td>2</td></tr></tbody></table>




```julia
sort!(df)
```




<table class="data-frame"><thead><tr><th></th><th>x</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>3 rows × 1 columns</p><tr><th>1</th><td>1</td></tr><tr><th>2</th><td>2</td></tr><tr><th>3</th><td>3</td></tr></tbody></table>




```julia
x
```




    3-element Array{Int64,1}:
     3
     1
     2




```julia
df.x[1] = 100
```




    100




```julia
df
```




<table class="data-frame"><thead><tr><th></th><th>x</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>3 rows × 1 columns</p><tr><th>1</th><td>100</td></tr><tr><th>2</th><td>2</td></tr><tr><th>3</th><td>3</td></tr></tbody></table>




```julia
x
```




    3-element Array{Int64,1}:
     3
     1
     2



请注意，在上面的示例中，`x` 原始向量在程序执行中不会发生改变，因为 `DataFrame(x=x)` 构造函数默认进行复制。

In-place 函数可以安全调用，除非通过 `view``@view`或[`groupby`](@ref)）创建`DataFrame` 视图  或  使用`copycols=false` 中创建的`DataFrame` 视图。

可以使用`df.col`、 `df[!, :col]` 直接访问`DataFrame`、 `df`的`col` ，通过[`eachcol`](@ref)函数，访问`DataFrame`的一列的`view` 的 `parent`，或者在`DataFrame`通过`copycols=false`创建之前，通过调用对列向量的引用。


```julia
x = [3, 1, 2];
```


```julia
df = DataFrame(x=x)
```




<table class="data-frame"><thead><tr><th></th><th>x</th></tr><tr><th></th><th>Int64</th></tr></thead><tbody><p>3 rows × 1 columns</p><tr><th>1</th><td>3</td></tr><tr><th>2</th><td>1</td></tr><tr><th>3</th><td>2</td></tr></tbody></table>




```julia
df.x == x
```




    true




```julia
df[!, 1] !== x
```




    true




```julia
eachcol(df)[1] === df.x
```




    true



请注意，不随意地从使用这些方法之一的对`DataFrame`的列进行更改。


处理`DataFrame`的列的确切规则在手册的[The design of handling of columns of a DataFrame](@ref-man-columnhandling)部分中进行了说明。


## 替换数据
Replacing Data


可以使用多种方法将数据框中的某些值替换为其他值。有些将替换应用于数据框中的所有值，有些则应用于单个列或列的子集。

请注意，in-place要求替换值可以转换为列的元素类型。特别是，这意味着将值替换为`missing`需要调用`allowmissing!`（如果列不允许缺少值）。


可以使用以下`replace!`命令执行对单个列的替换操作：


```julia
using DataFrames
```


```julia
df = DataFrame(a=["a", "None", "b", "None"], b=1:4,
                      c=["None", "j", "k", "h"], d=["x", "y", "None", "z"])
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String</th><th>Int64</th><th>String</th><th>String</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td>None</td><td>x</td></tr><tr><th>2</th><td>None</td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td>None</td></tr><tr><th>4</th><td>None</td><td>4</td><td>h</td><td>z</td></tr></tbody></table>




```julia
replace!(df.a, "None" => "c")
```




    4-element Array{String,1}:
     "a"
     "c"
     "b"
     "c"




```julia
df
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String</th><th>Int64</th><th>String</th><th>String</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td>None</td><td>x</td></tr><tr><th>2</th><td>c</td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td>None</td></tr><tr><th>4</th><td>c</td><td>4</td><td>h</td><td>z</td></tr></tbody></table>



这等效于`df.a = replace(df.a, "None" => "c")` ，但就in-place不创建新的列向量


可以使用广播语法就地执行对多个列或整个数据框的替换操作：


```julia
# replacement on a subset of columns [:c, :d]
df[:, [:c, :d]] .= ifelse.(df[!, [:c, :d]] .== "None", "c", df[!, [:c, :d]])
df
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String</th><th>Int64</th><th>String</th><th>String</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td>c</td><td>x</td></tr><tr><th>2</th><td>c</td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td>c</td></tr><tr><th>4</th><td>c</td><td>4</td><td>h</td><td>z</td></tr></tbody></table>




```julia
df .= ifelse.(df .== "c", "None", df) # replacement on entire data frame
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String</th><th>Int64</th><th>String</th><th>String</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td>None</td><td>x</td></tr><tr><th>2</th><td>None</td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td>None</td></tr><tr><th>4</th><td>None</td><td>4</td><td>h</td><td>z</td></tr></tbody></table>



请注意，在上面的示例中，更改 `.=` 为 `=` 将分配新的列向量，而不是就地应用操作。

将值替换为 `missing`时，如果列尚不允许缺少值，则必须避免就地操作并使用`=` 代替`.=`，或者事先调用`allowmissing!` ：


```julia
df2 = ifelse.(df .== "None", missing, df) # do not operate in-place (`df = ` would also work)
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String?</th><th>Int64</th><th>String?</th><th>String?</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td><em>missing</em></td><td>x</td></tr><tr><th>2</th><td><em>missing</em></td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td><em>missing</em></td></tr><tr><th>4</th><td><em>missing</em></td><td>4</td><td>h</td><td>z</td></tr></tbody></table>




```julia
allowmissing!(df) # operate in-place after allowing for missing
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String?</th><th>Int64?</th><th>String?</th><th>String?</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td>None</td><td>x</td></tr><tr><th>2</th><td>None</td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td>None</td></tr><tr><th>4</th><td>None</td><td>4</td><td>h</td><td>z</td></tr></tbody></table>




```julia
df .= ifelse.(df .== "None", missing, df)
```




<table class="data-frame"><thead><tr><th></th><th>a</th><th>b</th><th>c</th><th>d</th></tr><tr><th></th><th>String?</th><th>Int64?</th><th>String?</th><th>String?</th></tr></thead><tbody><p>4 rows × 4 columns</p><tr><th>1</th><td>a</td><td>1</td><td><em>missing</em></td><td>x</td></tr><tr><th>2</th><td><em>missing</em></td><td>2</td><td>j</td><td>y</td></tr><tr><th>3</th><td>b</td><td>3</td><td>k</td><td><em>missing</em></td></tr><tr><th>4</th><td><em>missing</em></td><td>4</td><td>h</td><td>z</td></tr></tbody></table>



参考原文：[2、working_with_dataframes](https://github.com/JuliaData/DataFrames.jl/blob/main/docs/src/man/working_with_dataframes.md)

