# -*- coding: UTF-8 -*-
import time

def autoCreatFile(filename):
    if filename =='' or filename.isalnum() :
        filename = "untitled_" + str(time.time()) + ".txt"
        print filename

    inputFile = open("inputfile.txt","w")
    inputFile.write("hello world!")

    outputFile = open(filename, "a")

    inputFile = open("inputfile.txt", "r")
    allLines = inputFile.readline()
    outputFile.writelines(allLines)

    inputFile.close()
    outputFile.close()


    return

#autoCreatFile('a.txt')
autoCreatFile(str(123))
autoCreatFile('')