# Practical_project_bikeshare
## 自行车共享数据  
在过去十年内，自行车共享系统的数量不断增多，并且在全球多个城市内越来越受欢迎。自行车共享系统使用户能够按照一定的金额在短时间内租赁自行车。用户可以在 A 处借自行车，并在 B 处还车，或者他们只是想骑一下，也可以在同一地点还车。每辆自行车每天可以供多位用户使用。  

由于信息技术的迅猛发展，共享系统的用户可以轻松地访问系统中的基座并解锁或还回自行车。这些技术还提供了大量数据，使我们能够探索这些自行车共享系统的使用情况。  

在此项目中，你将使用[ Motivate  ](https://www.motivateco.com/)提供的数据探索自行车共享使用模式，Motivate 是一家入驻美国很多大型城市的自行车共享系统。你将比较以下三座城市的系统使用情况：芝加哥、纽约市和华盛顿特区。  
## 数据集  
我们提供了三座城市 2017 年上半年的数据。三个数据文件都包含相同的核心六 (6) 列：    
  
* 起始时间 Start Time（例如 2017-01-01 00:07:57）  
* 结束时间 End Time（例如 2017-01-01 00:20:53）  
* 骑行时长 Trip Duration（例如 776 秒）  
* 起始车站 Start Station（例如百老汇街和巴里大道）  
* 结束车站 End Station（例如塞奇威克街和北大道）  
* 用户类型 User Type（订阅者 Subscriber/Registered 或客户Customer/Casual）  
  
芝加哥和纽约市文件还包含以下两列：  
   
* 性别 Gender  
* 出生年份 Birth Year  
原始文件（访问地址：([芝加哥](https://www.divvybikes.com/system-data)、[纽约市](https://www.citibikenyc.com/system-data)、[华盛顿特区](https://www.capitalbikeshare.com/system-data)）有很多列，并且在很多方面格式不一样。我们执行了一些[数据整理](https://en.wikipedia.org/wiki/Data_wrangling)操作，使这些文件压缩成上述核心六大列，以便于更直接地使用 Python 技能进行评估和分析。  
## 问题
将编写代码并回答以下关于自行车共享数据的问题：  

* 起始时间（Start Time 列）中哪个月份最常见？  
* 起始时间中，一周的哪一天（比如 Monday, Tuesday）最常见？  
* 起始时间中，一天当中哪个小时最常见？  
* 总骑行时长（Trip Duration）是多久，平均骑行时长是多久？  
* 哪个起始车站（Start Station）最热门，哪个结束车站（End Station）最热门？  
* 哪一趟行程最热门（即，哪一个起始站点与结束站点的组合最热门）？  
* 每种用户类型有多少人？  
* 每种性别有多少人？  
* 出生年份最早的是哪一年、最晚的是哪一年，最常见的是哪一年？  
## 互动式体验  
该文件是一个脚本，它接受原始输入在终端中创建交互式体验，来回答有关数据集的问题。这种体验之所以是交互式的，是因为根据用户输入的内容，上一页面中的数据结果也会随之改变。有以下三个问题会对结果产生影响：  
  
  1.你想分析哪个城市的数据？输入：芝加哥，纽约，华盛顿 ( Would you like to see data for Chicago, New York, or Washington?)  
  2.你想分析几月的数据？输入：全部，一月，二月…六月 ( Which month? all, january, february, ... , june?)  
  3.你想分析星期几的数据？输入：全部，星期一，星期二…星期日 (Which day? all, monday, tuesday, ... sunday?)  
    
这几个问题的答案将用来确定进行数据分析的城市，同时选择过滤某个月份或星期的数据。在相应的数据集过滤和加载完毕后，用户会看到数据的统计结果，并选择重新开始或退出。输入的信息应当大小写不敏感，比如"Chicago", "CHICAGO", "chicago", “chiCago”都是有效输入。  
  
