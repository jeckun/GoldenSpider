# shGlodPrice

*采用爬虫每天自动获取每天上海黄金交易所各类合约的交易价格*

## 数据来源

数据来自上海黄金交易所[每日行情](https://www.sge.com.cn/sjzx/mrhqsj?p=1)
计划每天早盘和午盘收盘后更新。

## 目录结构

```
shGlodPrice
|__ manager.py           程序入口
```

## 使用方法

修改 manager.py 中的 number 值，这个表示需要爬取的列表页数，默认一页10天的数据。然后执行下面的命令即可。
```
$ python manager.py
```

## 待解决问题

目前还没处理保存数据的问题，计划用sqlite进行存储。

由于上海黄金交易所每日行情的数据格式在不同时期会有所不同，爬取少量数据不会有问题，但爬取大量历史数据时会遇到格式不同的问题。


## Api接口

计划写一个API接口，待上诉问题解决以后就开始。
