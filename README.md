# pyspider_news
### 使用Pyspider框架爬取数据

##### 安装配置：
Anaconda3 5.2.0  ——python3.6
安装命令：
`pip install pyspider`

`pip install pymysql`

终端启动命令：

```
pyspider
```

进入**pyspider dashboard** ：   localhost:5000

官网上面给了很多用法：
http://docs.pyspider.org/en/latest/

我这里简单的结合一个API接口来获取里面的数据
数据接口来自：https://newsapi.org
免费使用里面的接口，只要申请一个apikey。自行申请不介绍了。

现在的任务是：爬取上面`articles`里每一个`author,title,url,publishedAt`并把书存入mysql数据库中.

任务思维：
1.目标的数据是怎样的数据(格式，类型)？
2.如何获取数据？
3.分析完需要获取的设计数据库
4.开始设计程序爬取

**数据库设计**
```
CREATE TABLE `topnews` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `author` varchar(255) DEFAULT NULL COMMENT '作者',
  `title` varchar(2000) DEFAULT NULL COMMENT '标题',
  `url` varchar(2000) DEFAULT NULL COMMENT '链接',
  `publishedAt` varchar(255) DEFAULT NULL COMMENT '发布时间',
  `AddOn` varchar(255) DEFAULT NULL COMMENT '入库时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
```

**newsapi.py**请在  localhost:5000中打开
