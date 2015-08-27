# expiredict

### 介绍

python的一个小模块，支持时间过期的dict

### 使用方法

```
import time

from expiredict import ExpireDict
d = ExpireDict(10)
d['a'] = 'abc'
print "d.keys() : %s"%d.keys()
d.set_ttl('a',2)
print d.ttl('a')
print "return value : %s"%d['a']
time.sleep(3)
print d['a']

```
