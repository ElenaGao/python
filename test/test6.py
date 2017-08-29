# -*- coding: UTF-8 -*-
"""
try:
    fh = open("testfile", "r")
    fh.write("这是一个测试文件,用于测试异常!!")
except IOError:
    print "Error:没有找到文件或读取文件失败"
else:
    print "内容写入成功"
    fh.close()
"""

try:
    fh = open("testfile", 'r')
    try:
        fh.write("this is the test file")
    finally:
        print "close the file"
        fh.close()
except IOError:
    print "Error"