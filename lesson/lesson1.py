# -*- coding: UTF-8 -*-

def searchMaxWithIndex(listnum):

    maxnum = max(listnum) #先找出最大值
    p = 0   #记录最大值的索引号
    for i in listnum:
        if listnum[p] != maxnum:
            p+=1

    print p

    return


searchMaxWithIndex([1,2,5,4,5])
