# -*- coding: UTF-8 -*-

i =1
while ((i+1)*(i+1)-i*i)<=168:
    i+=1
    print i

for j in range(1,i):
    for k in range(1,i):
        if(k*k-j*j)==168:
            print k*k-268
