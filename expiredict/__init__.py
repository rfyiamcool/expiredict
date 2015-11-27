#coding:utf-8
'''
>>> d = ExpireDict(100)

map1: OrderedDict()
The values stored in the following way:
{
    key1: value1,
}
map2 : key_time_map
{
    key1: {"expire_time":created_time1},
}

'''

import time
from threading import RLock

try:
    from collections import OrderedDict
except ImportError:
    # Python < 2.7
    from ordereddict import OrderedDict


class ExpireDict(OrderedDict):
    def __init__(self, max_len=0):
        assert max_len >= 1

        OrderedDict.__init__(self)
        self.max_len = max_len
        self.key_time_map = {}
        self.lock = RLock()

    def __contains__(self, key):
        """ Return True if the dict has a key, else return False. """
        try:
            with self.lock:
                item = OrderedDict.__getitem__(self, key)
                expire_time = self.key_time_map[key].get('expire_time',None)
                if expire_time and expire_time >0:
                    return True
                else:
                    del self[key]
        except KeyError:
            pass
        return False

    def __getitem__(self, key, with_age=False):
        """ Return the item of the dict.

        Raises a KeyError if key is not in the map.
        """
        with self.lock:
            try:
                item = OrderedDict.__getitem__(self, key)
            except KeyError: 
                raise KeyError(key)

            if not self.key_time_map.get(key,None):
                return item
            item_age = (self.key_time_map[key].get('expire_time',0)) - time.time() 
            if item_age > 0:
            #    if with_age:
            #    return item[0], item_age
            #else:
                return item
            else:
                del self[key]
                raise KeyError(key)

    def __setitem__(self, key, value):
        """ Set d[key] to value. """
        with self.lock:
            if len(self) == self.max_len:
                self.popitem(last=False)
            OrderedDict.__setitem__(self, key,value)
            self.key_time_map[key] = {}

    def __llen__(self, key):
        return len(OrderedDict.__setitem__(self, key,value))

    def pop(self, key, default=None):
        """ Get item from the dict and remove it.

        Return default if expired or does not exist. Never raise KeyError.
        """
        with self.lock:
            try:
                item = OrderedDict.__getitem__(self, key)
                expire_time = self.key_time_map.get(key,{}).get('expire_time',None)
                if not expire_time:
                    del self[key]
                    del self.key_time_map[key]
                    return item
                
                if expire_time - time.time() >0:
                    del self[key]
                    return item
                return default
                        
            except KeyError:
                return default

    def clear(self):
        """ 
            clear all keys and keys in key_time_map
        """
        with self.lock:
            try:
                OrderedDict.clear(self)
                self.key_time_map.clear()
                return True
            except KeyError:
                return False

    def ttl(self, key):
        """ Return TTL of the `key` (in seconds).

        Returns None for non-existent or expired keys.
        """
        expire_time = self.key_time_map.get(key,{}).get('expire_time',None)
        if expire_time:
            key_ttl = expire_time - time.time()
            if key_ttl > 0:
                return key_ttl
        return None

    def set_ttl(self, key, seconds):
        is_have = OrderedDict.__getitem__(self,key)
        if is_have:
            expire_time = time.time() + seconds
            self.key_time_map[key] = {"time":time.time(),"max_age":0,"expire_time":expire_time}
            key_ttl = expire_time - time.time()
            #self.__setitem__(key,is_have)
            #OrderedDict.__setitem__(self, key,is_have)
            if key_ttl > 0:
                return key_ttl
        return None

    def get(self, key, default=None, with_age=False):
        " Return the value for key if key is in the dictionary, else default. "
        try:
            return self.__getitem__(key, with_age)
        except KeyError:
            if with_age:
                return default, None
            else:
                return default

    def items(self):
        """ Return a copy of the dictionary's list of (key, value) pairs. """
        r = []
        for key in self:
            try:
                r.append((key, self[key]))
            except KeyError:
                pass
        return r

    def values(self):
        """ Return a copy of the dictionary's list of values.
        See the note for dict.items(). """
        r = []
        for key in self:
            try:
                r.append(self[key])
            except KeyError:
                pass
        return r

    def keys(self):
        return OrderedDict.keys(self)

    def fromkeys(self):
        return OrderedDict.keys(self)

    def iteritems(self):
        """ support iteritems"""
        return OrderedDict.keys(self)

    def itervalues(self):
        return OrderedDict.keys(self)

    def viewitems(self):
        raise NotImplementedError()

    def viewkeys(self):
        raise NotImplementedError()

    def viewvalues(self):
        """ Return a new view of the dictionary's values. """
        raise NotImplementedError()
