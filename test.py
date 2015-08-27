#coding:utf-8
import time 

from expiredict import ExpireDict
d = ExpireDict(10)
d['a'] = 'abc'
d['b'] = 'abc'
print d.pop('b',123)
print d
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
