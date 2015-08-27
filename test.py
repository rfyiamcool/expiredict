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
