import sys
import os
import datetime
import argparse

stocklist = list()
stockline = list()
fo = open(sys.argv[1],'r')
#Cheat Read first line
header = fo.readline()
for line in fo:
    stockline =line.split(',')
    print stockline[0]
    stocklist.append(stockline[0])
    
print "Number of items in list: %s",len(stocklist)
print "100th item in list: %s", stocklist[100]
fo.close()
