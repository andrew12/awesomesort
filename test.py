import heapq
import random


class mine(list):
    def __getitem__(self, key):
        print("%r[%r]" % (self, key))
        return super(mine, self).__getitem__(key)

    def __setitem__(self, key, value):
        print("%r[%r] = %r" % (self, key, value))
        super(mine, self).__setitem__(key, value)

    def __getattr__(self, name):
        print("%r.%s" % (self, name))
        super(mine, self).__getattr__(name)


lst = mine(range(32))
print("shuffle")
random.shuffle(lst)
print("heapify")
heapq.heapify(lst)
print("%r" % (lst))
