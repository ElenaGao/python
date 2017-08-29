#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""d=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                d.append([i,j,k])

print "total num:",len(d)

print d
"""

from itertools import permutations

for i in permutations([1,2,3,4],3):
    print i