import sys
import os
import datetime
import argparse

stocklist = list()
stockline = list()


parser = argparse.ArgumentParser()
parser.add_argument("-if","--inputfile",help="Input File")
parser.add_argument("-sd","--startdate", type=int,nargs=3,help="Start Date: Year[YYYY] Month[MM] Day [DD]")
parser.add_argument("-of","--outputfile",help="Output File")
parser.add_argument("-ed","--enddate", type=int,nargs=3,help="End Date: Year[YYYY] Month[MM] Day [DD]")

args = parser.parse_args()

infilename = args.inputfile
startyear= args.startdate[0]
startmonth = args.startdate[1]
startday = args.startdate[2]


print "Year: ", startyear
print "Month: ", startmonth
print "Day: ", startday

stockStartDate = datetime.datetime(startyear,startmonth,startday)

print stockStartDate
'''


fo = open(infilename,'r')
#Cheat Read first line
header = fo.readline()
for line in fo:
    stockline =line.split(',')
    print stockline[0]
    stocklist.append(stockline[0])
    
print "Number of items in list: %s",len(stocklist)
print "100th item in list: %s", stocklist[100]
fo.close()
'''