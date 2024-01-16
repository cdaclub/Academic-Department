## 《SQL数据分析极简入门》第1节 SQL简介与基础知识


> 做数据分析的，为什么要写SQL？
> 
> 没有数据的情况下，我们分析数据就像是巧妇难为无米之炊。因此，为了进行数据分析，我们必须获取数据。而大多数情况下，数据都存放在数据库中，这时候我们就必须要学会SQL取数了。
>
> 除了一部分公司专人专岗，有人帮你查好数据发你做分析,大部分情况还是需要你自己取数的。

本次我们沿用之前[《极简统计学入门》](https://edu.cda.cn/goods/show/3386?targetId=5647&preview=0)的“MVP”思路，用三节的内容梳理一下SQL（基于MySQL8.0），整个系列框架如下

- 第1节 SQL简介与基础知识
    - SQL简介
    - SQL查询基础之DDL、DML、DQL
    - SQL数据类型
    - SQL查询的执行顺序
- 第2节 窗口分析函数
    - 窗口函数
    - 分析函数
- 第3节 SQL近N日登录与连续登录N日问题
    - 连续登录N天的用户数量
- 第4节 近N日留存的用户数及留存率
    - 近N日留存的用户数及留存率
    
### 1. SQL简介

我们知道，**SQL**（结构化查询语言）是一种数据库语言，按照功能分类，有**DDL、DQL、DML、DCL、TCL** 五大类型，简单了解一下它们分别是做什么用的：



（1）**DDL**（Data Definition Language）
DDL是数据**定义**语言，主要用来定义或者改变表的结构。例如：`create、alter、drop、truncate`等语句。




（2）**DQL**（Data Query Language）
DQL是数据**查询**语言，主要用来从表中检索数据。例如：`select`语句。









（3）**DML**（Data Manipulation Language）
DML是数据**操作**语言，主要用来对数据库里表中的数据进行操作。例如：`insert、delete、update`等语句。





（4）**DCL**（Data Control Language）
DCL是数据**控制**语言，主要用来设置或更改数据库用户或角色对数据的访问权限。例如：`grant、revoke`等语句。




（5）**TCL**（Transaction Control Language）
TCL是事务**控制**语言，主要用来控制事务。例如：`COMMIT、ROLLBACK`等语句。

了解了以上分类，我们简单回顾一下其中DDL、DML、DQL的基础语法（有基础的可直接跳过看SQL查询与执行顺序）


### 2. SQL基础之DDL、DML、DQL

#### ① 数据定义语言 (DDL)
定义数据库当中的对象 (库、表) 关键字: `create`、`delete`、`alter`、`show`


##### 创建数据库
- 创建数据库 `create database 数据库名`
- 创建指定字符集的数据库 `create database 数据库名 charset set 字符集编码`
- 创建一个数据库（先判断数据库是否已存在，如果不存在则进行创建）`create database if not exist数据库名`




##### 查看数据库
- 查询所有数据库名称

`show database;`
- 查询指定数据库的字符集 并显示创建语句 

`show create database 数据库名;`




##### 删除数据库
- 删除指定数据库 

`drop database 数据库名;`
- 删除指定数据库，如果不存在则不删除 

`drop database 数据库名 if exist;`








##### 进入指定数据库
`use 数据库名;`










##### 创建表
`create table 表名(字段名 字段类型)`
```sql
create table table_name
(
	column_1 int null,
	column_2 int null
);
```

##### 复制表

- 只复制结构 

`create table 新表名 like 被复制的表名;`

执行上述语句后，将创建一个名为table2的新表，其结构与table1完全相同，但不会复制table1中的任何数据。

- 复制结构和数据 

`create table 新表名 as select * from 被复制的表名;`

上述语句将创建一个名为table2的新表，其结构和数据与table1完全相同。






##### 查询表
- 查询库里面有哪些表 

`show tables;`
- 查询表的结构 

`describe 表名;`
- 查询指定表的创建语句 

`show create table 表名;`








##### 修改表
- 给表添加 (多个) 字段 

`alter table 表名 add column (字段名 字段类型,字段名 字段类型);`
- 修改表字段的数据类型 

`alter table 表名 modify column 字段名 字段类型;`

- 修改表字段的字段名 

`alter table 表名 change column 旧字段名 新字段名 字段类型;`

- 删除一个字段 

`alter table 表名 drop column 字段名;`

- 修改表名 

`alter table 表名 rename 新表名;`



#### ② 数据操作语言 (DML)
操作数据 (增、删、改) 关键字: `insert`、`delete`、`update`





##### 添加数据
- 指定列名添加 

`insert into 表名 (字段名1,字段名2) values(数值1,数值2);`

- 全部列的添加 

`insert into 表名 values (数值1,···,最后一个数值);`

- 一次性插入多条数据

```sql
insert into 表名 values
(数值1_1,数值2_1···,最后一个数值n_1),
(数值1_2,数值2_2···,最后一个数值n_2),
(数值1_n,数值2_n···,最后一个数值n_n);
```

##### 删除数据

- 删除表的指定数据 

`delete from 表名 where 字段名 = 字段值;`

- truncate 删除全表的数据 

`truncate table 表名;`

- drop 删除全表（包括定义和数据。）

`drop table 表名;`


##### drop、truncate、delete 三者的区别

- `drop`用于删除数据库对象，包括定义和数据。
- `truncate`用于删除表中的所有数据，但保留表的定义。
- `delete`用于删除表中的行，可以根据条件删除特定的数据，并且可以回滚。



##### 修改数据
- 修改指定字段数据 

`update 表名 set 字段名 = 数据值 where 字段名 = 数据值;`

- 同时修改多个字段 

`update 表名 set 字段名1=数据值1,字段名2=数据值2 where 字段名 = 数据值;`

- 在基础数据上进行修改（某列的值减去3）

`update 表名 set 字段名1 = 字段名1 -3;`


#### ③ 数据库查询语言 (DQL)
##### 查询数据
- 查询表中所有数据 

`
select * from 表名;
`


- 查询表的指定列

`
select 字段名1, 字段名2 from 表名;
`
- 指定别名查询 

`
select 字段名 as 别名 from 表名;
`

- 常量列查询 

`
select 字段名 as 自定义名字,临时常量 as 别名 from 表名;
`
- 合并列查询 

`
select 字段名 as 自定义名字，(字段 1 + 字段2) as 别名 from 表名;
`








##### 条件查询 (跟在 where 后面的关键字) 条件运算符
```sql
<             # 小于
>             # 大于
<=            # 小于等于 
>=            # 大于等于
<>            # 不等于
!=            # 不等于
between…and…  # 在……范围内
in            # 包括
like          # 模糊查询
is null       # 是否为空
and           # 且
or            # 或
not           # 非
```

##### 模糊查询

`select * from 表名 where 字段名 like "关键词";`

`select * from 表名 where 字段名 like "%hello%";`

`select * from 表名 where 字段名 like "%_大学%";`


##### 聚合查询

- max():获取查询后结果的最大值 

`select max(字段名) from 表名;`

- min():获取查询后结果的最小值 

`select min(字段名) from 表名;`

- avg():获取查询后结果的平均值 

`select avg(字段名) from 表名;`


- sum():获取查询后结果的总和 

`select sum(字段名) from 表名;`

- count():获取查询后结果的总记录数

`select count (字段名) from 表名;`



##### 排序查询关键字: order by 默认是升序 asc，降序 desc

```sql
select *
from table_class
order by id desc;
```


##### 分组查询关键字:group by
- 统计每个班级有多少人 
```sql
select class_name,count(*) 
from table_class
group by class_name;
```

- 统计班级人数大于2个人的班级
```sql
select class_name,count(*)
from table_class
group by class_name
having count (*)>=2;
```

##### 内连接查询
两张表交叉后并且过滤后的数据查询 (交集)关键字: **inner join**

```sql
select * 
from table_a a 
inner join table_b b 
on a.aid = b.bid;
```

##### 左 (外) 连接查询
左表 (table_a) 的记录将会全部表示出来，而右表 (table_b) 只会显示符合搜索条件的记录，右表记录不足的地方均为 NULL 关键字: **left join**。

```sql
select * 
from table_a  a 
left join  table_b b
on a.a_id = b.b_id;
```

##### 右 (外) 连接查询
左表 (a_table) 只会显示符合搜索条件的记录，而右表 (b_table) 的记录将会全部表示出来，左表记录不足的地方均为 null 关键字: **right join**

```sql
select * 
from  table_a a 
right join table_b b 
on a.a_id = b.b_id;
```


##### 结果合并
```sql
(select colum_1,colum_2,...,colum_n 
from table_a)
union
(select colum_1,colum_2,...,colum_n
from table_b)
```

- 两个select语句具有相同的列数和相似的数据类型。如果列数不匹配，可以使用null或者空字符串填充缺失的列

- 使用 union 时，数据完全相同的记录，将会被合并，由于合并比较耗时，一般不直接使用 union 进行合并，而是采用 union all进行合并。


```sql
(select id,name from table_a
order by id) 
union all
(select id,name from table_b
order by id);
#没有排序效果
```


```sql
(select id,name from table_a ) 
union all 
(select id,name from table_b ) 
order by id;
#有排序效果
```

##### 子查询
将一个 SQL 语句的查询结果 (单列数据) 作为另一个 SQL 语句的查询条件。


```sql
select *
from table_a
where id_a in 
    (select id_b
    from table_a);
```
好了，以上内容，我们简单回顾了一下SQL的基本函数，下面我们开始正式内容：

如果你接触过不同编程语言就会发现，任何编程语言的学习，都离不开3个最基本的核心要素，**数据类型、流程控制、函数**

**数据类型**是用来描述数据的性质和特征的，它决定了数据在计算和处理过程中的行为和规则。常见的数据类型包括整数、浮点数、字符串、日期等。简而言之，数据类型就是**你将要操作的东西具有什么样的特点**。

**流程控制**是指通过条件判断和循环等方式，控制程序按照一定的顺序执行不同的操作步骤。它决定了数据的处理流程，包括判断条件、循环次数、分支选择等。简而言之，流程控制解决的问题就是**你要操作这个东西的基本流程是什么**。

**函数**是一段预先定义好的代码，用于执行特定的操作或计算。它接受输入参数，并返回一个结果。函数可以用来对数据进行各种计算、转换、筛选等操作，以满足特定的需求。简而言之，函数解决的问题就是**你要怎么样才能可复用地操作这一类东西**。

SQL极简教程系列我们重点讨论数据类型与函数，下面我们先来看第一个核心要素：

### 3. 数据类型

##### ① 整数类型
| 整数类型 | 用途 | 范围 |
| --- | --- | --- |
| tinyint | 用于存储小整数值 | -128到127，即($-2^7$)到($2^7-1$)  |
| smallint | 用于存储较小的整数值 | -32768到32767 ，即($-2^{15}$)到($2^{15}-1$) |
| mediumint | 用于存储中等大小的整数值 |   -8388608到 8388607 ，即($-2^{23}$)到($2^{23}-1$) |
| int | 用于存储普通大小的整数值 | -2147483648到2147483647，即 ($-2^{31}$)到($2^{31}-1$)|
| bigint | 用于存储大整数值 | -9223372036854775808到9223372036854775807，即 ($-2^{63}$) 到 ($(2^{63})-1$)|


##### ② 浮点类型

| 浮点类型 | 用途 | 范围 |
| --- | --- | --- |
| float | 用于存储单精度浮点数值 | -3.402823466E+38到-1.175494351E-38，0，1.175494351E-38到3.402823466E+38 |
| double | 用于存储双精度浮点数值 | -1.7976931348623157E+308到-2.2250738585072014E-308，0，2.2250738585072014E-308到1.7976931348623157E+308 |

##### ③ 字符串类型

| 数据类型 | 用途 | 特点 |
| --- | --- | --- |
| char | 用于存储固定长度的字符串 | 存储的字符串长度固定，最多可以存储255个字符 |
| varchar | 用于存储可变长度的字符串 | 存储的字符串长度可变，最多可以存储65535个字符 |
| binary | 用于存储二进制数据 | 存储的数据以二进制形式存储，最多可以存储255个字节 |
| varbinary| 用于存储可变长度的二进制数据 | 存储的数据以二进制形式存储，长度可变，最多可以存储65535个字节 |
| text | 用于存储较长的文本数据 | 存储的文本数据长度可变，最多可以存储65535个字符 |
| blob | 用于存储较大的二进制数据 | 存储的二进制数据长度可变，最多可以存储65535个字节 |


##### ④ 日期类型

| 数据类型 | 用途 | 范围 |
| --- | --- | --- |
| date | 用于存储日期值 | '1000-01-01'到'9999-12-31' |
| time | 用于存储时间值 | '-838:59:59'到'838:59:59' |
| datetime | 用于存储日期和时间值 | '1000-01-01 00:00:00'到'9999-12-31 23:59:59' |
|timestamp | 用于存储日期和时间值，自动更新 | '1970-01-01 00:00:01' UTC到'2038-01-19 03:14:07' UTC |
| year | 用于存储年份值 | 1901到2155 |




如果上面内容看明白了，恭喜你已经学会了**如何描述你要操作的对象的特点了**，接着我们看第二个核心问题：函数。一般无外乎针对字符串的函数、针对日期的函数、针对数值运算的函数、以及操作数据转化的函数：


### 5、函数
#### ① 字符串函数

**字符串函数：**返回字符串的长度 

```sql
select length('learn_mysql_and_find_a_data_analysis_job') str_len;
```



**字符串连接函数：**返回输入字符串连接后的结果，支持任意个输入字符串

```sql
select concat('Certified','Data','Analyst') as str_concat;
```

**带分隔符字符串连接函数：** 返回输入字符串连接后的结果，SEP表示各个字符串间的分隔符

```sql
select concat_ws('_','Certified','Data','Analyst') as str_concat_ws; 
```


**字符串截取函数:** 返回字符串从start位置到结尾的字符串

```
select substr('Certified_Data_Analyst',11);

select substr('Certified_Data_Analyst',-12);

```

**字符串截取函数:** 返回字符串从start位置开始，长度为len的字符串 

```sql
select substr('Certified_Data_Analyst',11,4);
select substring('Certified_Data_Analyst',-7,7);

```

**字符串转大写函数：upper,ucase** 返回字符串A的大写格式

```sql
select upper('certified_data_analyst');  
select ucase('certified_data_analyst');
```



**字符串转小写函数：lower,lcase** 返回字符串A的小写格式

```sql
select lower('CERTIFIED_DATA_ANALYST'); 
select lcase('CERTIFIED_DATA_ANALYST');
```

**字符串反转函数：**返回字符串的反转结果 

```sql
select reverse('learn_mysql')  as str_rev;
```


**去空格函数：trim** 去除字符串两边的空格  

```sql
select trim(' Data ');  
```

**左边去空格函数：ltrim**去除字符串左边的空格

```sql
select ltrim(' Data '); 
```

**右边去空格函数：rtrim** 去除字符串右边的空格

```sql
select rtrim(' Data ');  `
```

**空格字符串函数：space** 返回长度为n的字符串  
```sql
select space(10);  
select length(space(10));
```

**重复字符串函数：repeat** 返回重复n次后的str字符串  
```sql
select repeat('SQL',5);
```

**左补足函数：lpad** 将str进行用pad进行左补足到len位  

```sql
select lpad('MySQL',11,'go');
```

**右补足函数：rpad** 将str进行用pad进行右补足到len位  
```sql
select rpad('MySQL',11,'go');
```

**分割字符串函数: mysql里面没有直接做字符串分割的函数，substring_index** 按照pat字符串分割str，会返回分割后的字符串数组  
```sql
select substring_index('Certified_Data_Analyst', '_', 1) AS part1,
       substring_index(substring_index('Certified_Data_Analyst', '_', 2), '_', -1) AS part2,
       substring_index(substring_index('Certified_Data_Analyst', '_', 3), '_', -1) AS part3;
```

**集合查找函数: find_in_set** 返回str在strlist第一次出现的位置，strlist是用逗号分割的字符串。如果没有找该str字符，则返回0  
```sql
select find_in_set('data', 'certified,data,analyst');
select find_in_set('mysql','certified,data,analyst');
```

**正则表达式替换函数：regexp_replace**将字符串A中的符合java正则表达式B的部分替换为C。注意，在有些情况下要使用转义字符
```sql
select regexp_replace('learn_mysql_and_python', 'mysal|python', 'programming');
```
**正则表达式提取函数：regexp_extract** 返回第一个匹配的子字符串

```sql
select regexp_substr('mysql8', '[0-9]+')  extracted_number;
```

#### ② 数学函数

**四舍五入:round** 
```sql
select round(3.14159);   # round(a) 返回a的值，并对a四舍五入
select round(3.14159,3); # round(a, n) 返回保留n小数位和四舍五入后的a的值
```
**向上取整:ceil**
```sql
select ceil(3.14);
select ceiling(3.14);
select ceil(-3.14);
```
**向下取整:floor**
```sql
select floor(3.14);
select floor(-3.14);
```
**求取随机数:rand**
```sql
select rand();    # 每行返回一个double型随机数
select rand(100); # 每行返回一个double型随机数，整数seed是随机因子的种子；
```
---
**其他数学运算函数**
```sql
# exp(d)           #返回e的 d幂次方，返回double型；
select exp(1); # e的1次方
# 2.718281828459045

# ln(d)	        #以自然数为底d的对数，返回double型；
select ln(exp(1)); # 以e为底e的对数
# 1

# log2(d)          #以2为底d的对数，返回double型；
select log2(8);
# 3

# log10(d)         #以10为底d的对数，返回double型；
select log10(100);
# 2

# log(a, b) #以a为底b的对数，返回double型；
select log(3,9);
# 2


# pow(x, n) # x 的n次幂，返回double型；
select pow(10,2);
# 100

# sqrt(DOUBLE d) 	        #d的平方根，返回double型；
select sqrt(16);
# 4

# abs(DOUBLE d)		    #返回d的绝对值，结果为double型；
select abs(-3.14);
# 3.14

# sin()		    #返回d的正弦值，结果为double型；
select sin(radians(30));
# 0.49999999999999994

# cos()		    #返回d 的余弦值，结果为double型；
select tan(radians(60));
# 0.5000000000000001

# tan()		    #返回d的正切值，结果为double型；
select tan(radians(45));
# 0.9999999999999999

# asin()		    #返回d的反正弦值，结果为double型；
select degrees(asin(0.5));
# 30.000000000000004

# acos()		    #返回d的反余弦值，结果为double型；
select degrees(acos(0.5));
# 60.00000000000001

# atan()		    #返回d的反正切值，结果为double型；
select degrees(atan(1));
# 45

# PI()				    #数学常数Pi，圆周率；
select PI();
# 3.141593
```
#### ③ 日期函数
**获取日期** date() 返回时间字符串的日期部分

```sql
select date('2023-09-21 15:06:51');
```

**获取年月日** 

year()、month()、day() 从一个日期中取出相应的年、月、日
```sql
select 
year('2023-09-21 15:06:51'),
month('2023-09-21 15:06:51'),
day('2023-09-21 15:06:51');
```

**获取第几周** 

weekofyear()  返回输入日期在该年中是第几个星期

```sql
select weekofyear('2023-09-21 15:06:51');
```

**获取指定间隔的日期**

- date_add()  在一个日期基础上增加天数   
- date_sub() 在一个日期基础上减去天数
```sql
#请问，2023-09-21起，7天以后的日期是？7天前的日期是？
select date_add('2023-09-21',interval 7 day) as seven_days_after,
date_sub('2023-09-21',interval 7 day ) as seven_days_before;

# 当前日期，7天以后的日期是？7天前的日期是？
select date_add(current_date(),interval 7 day) as seven_days_after, date_sub(current_date(),interval 7 day) as seven_days_before;
```

**获取两个日期之差** 

返回的是数字 
- datediff() 计算开始时间startdate到结束时间enddate相差的天数
```sql
select datediff('2023-09-21 15:06:51','2003-09-21 15:06:51');
# 7305
```

- current_date() 返回当前日期
```sql
select current_date();
# 2023-09-21
```

**日期时间格式化**
- date_format() 按指定格式返回时间（对日期时间格式化）

```
#将“2023-09-21 15:06:51”转化如下格式
select date_format('2023-09-21 15:06:51', '%Y-%m-%d');
select date_format('2023-09-21 15:06:51', '%Y-%M-%D');
select date_format('2023-09-21 15:06:51', '%M-%d-%y');

select date_format('2023-09-21 15:06:51', '%m/%d/%y');
select date_format('2023-09-21 15:06:51', '%m/%d/%Y %H:%i:%s');
select date_format('2023-09-21 15:06:51', '%Y年%m月%d日 %H点%i分%s秒');
```

附：MySql查询当天、本周、本月、本季度、本年

```sql

# 1.今天
select  to_days(now());

# 2.昨天
select  to_days(now()) - 1 ;

# 3.本周
select  yearweek(now());

# 4.上周
select yearweek(now()) -1;

# 5.往回推，7天前的时间
select date_sub(current_date(), interval 7 day);

# 6.往回推，30天前的时间
select date_sub(current_date(), interval 30 day);

# 7.本月
select  date_format(current_date(),'%Y%m');

# 8.上月
select  date_format(date_sub(current_date(),interval 1 month),'%Y%m') ;


# 9.近6个月
select date_sub(current_date(),interval 6 month);

# 10.本季度
select quarter(current_date());

# 11.上季度
select quarter(date_sub(current_date(),interval 1 quarter));

# 12.今年
select  year(now());

13.去年
select year(date_sub(now(),interval 1 year));
```


#### ④ 类型转换函数
**类型转换函数 double、date、char**



```sql
# 将字符'3.14'转换为double数值类型
select cast('3.14' as double);
```




```sql
# 将字符串'2023-09-21'转换为date类型
select cast('2023-09-21' as date);
```


#### interval函数

```sql
interval(a,n1,n2,n3,...);
```
其中，a是要判断的数值，n1,n2,n3,...是分段的间隔。这个函数的返回值是段的位置：如果比n1还小，则返回0，如果在n1和n2中间，则返回1，如果n2<=a<n3，则返回2。

```sql
select interval(1, 3, 7, 10);
# 0
select interval(5, 3, 7, 10);
# 1
select interval(9, 3, 7, 10);
# 2
```

**interval关键词**

```
select now()-interval '2' hour;
```




#### ⑤ 条件函数


**函数if**
```sql
select if(80 > 60,'及格','未及格'); 条件表达式为真返回1，为假返回2

```

**非空查找 coalesce**

coalesce(v1,v2,…)  返回参数中的第一个非空值；如果所有值都为null，那么返回 null

```sql
select coalesce('Certified',null, 'Analyst');
select coalesce(null, 'Data','Analyst');
```

**判断是否为null**

isnull()  判断是否为null
-   语法：isnull(a)    如果a为null就返回1，否则返回0

```sql
select isnull(null);
select isnull('');
```


**条件判断 case...when...** 

```sql
select name,
      case
           when score >= 80 then '优秀'
           when score >= 70 and score < 80 then '良好'
           when score >= 60 and score < 70 then '及格'
           else '未及格'
      end as score_label
from cda_exam;
```

看完了数据类型与函数，我们来了解一下SQL的执行顺序。了解SQL的执行顺序，不仅有助于深入理解SQL的执行过程，还能在处理异常时快速确定问题所在。

### 4. SQL查询的执行顺序
下面看一个包含常用SQL关键词的语句模板：

```sql
select distinct column_name,
agg_func(column_name_or_expression)
from table_a a
join table_b b
on a.column_name = b.column_name
where constraint_expression
group by column_name
having constraint_expression
order by column_name asc/desc
limit count offset count;
```

##### ① from 和 join
从指定的表中选择数据


##### ② where

从数据进行过滤。 注意：as 列别名还不能在这个阶段使用，因为这时候select还没执行，别名是一个还没执行的表达式

##### ③ group by

按指定的列对数据进行分组。

##### ④ having
对group by 子句中分组后的数据进行过滤。as 列别名也不能在这个阶段使用。


##### ⑤ select
选择要返回的列，决定输出什么数据。

##### ⑥ distinct
如果数据行有重复 distinct 将负责排重


##### ⑦ order by
对结果做排序。此时可以用 as 别名了，select 中的表达式已经执行完了。


##### ⑧ limit / offset
限制结果集的数量。 `limmit a,b  等价于 limit b offset a`



> 日拱一卒，功不唐捐。你所有的奋斗都不会白费！

下期将为大家带来《SQL数据分析极简入门》第2节 窗口分析函数

