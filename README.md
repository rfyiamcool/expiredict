# expiredict

### 介绍

python的一个小模块，支持时间过期及限制key个数的dict,涵盖所有常用的dict方法。

[expiredict 更多介绍](http://xiaorui.cc  "xiaorui.cc")

New Future

1. support len

2. support clear

To Do List

1. logging

.....

### 安装
1. 源码安装

```
git@github.com:rfyiamcool/expiredict.git
python setup.py install
```
2. pip 安装

```
pip install expiredict
```

### 使用方法

```
import time 

from expiredict import ExpireDict
d = ExpireDict(10)
d['a'] = 'abc'
print d.clear()
print "clear data :%s"%d.keys()
d['a'] = 'abc'
print "dict length :%s"%len(d)
print "d.keys() : %s"%d.keys()
d.set_ttl('a',2)
print d.ttl('a')
print "return value : %s"%d['a']
time.sleep(3)
print d['a']
```
