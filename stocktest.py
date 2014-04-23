#!/usr/bin/python
from pandas.io.data import DataReader
from datetime import datetime
import logging

# Setup Argument Parsing
# -sd YYYY MM DD
# -ed YYYY MM DD
# -out file to write out to
# check if both -sd and -ed that -ed > -sd
# if no -sd then set to 2000, 1, 1
# if no -ed then set to currentDay 

#Setup Logging

logging.basicConfig(filename='stocktest.log',level=logging.DEBUG,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
#logging.basicConfig(filename='stocktest.log',level=logging.DEBUG)

startDate = datetime(2000,1,1)
#endDate = datetime(2014,04,22)
endDate = datetime.today()
logging.debug('STOCKTEST: Start run of program')
logging.info(' STOCKTEST: End stock Date is %s', endDate.strftime("%Y-%m-%d"))


# Setup reading stock list
stockSymbolName = "AAPL"
goog = DataReader(stockSymbolName,"yahoo",startDate,endDate)

'''
print "Number of dates = ", len(goog.index)
print "Number of Opens = ", len(goog["Open"])
print "Number of Opens = ", len(goog["High"])
print "Number of Opens = ", len(goog["Low"])
print "Number of Opens = ", len(goog["Close"])
print "Number of Opens = ", len(goog["Volume"])
print "Number of Opens = ", len(goog["Adj Close"])

print "Row of Data... first Record"

print "Date:",goog.index[1].date()
print "Open:",goog["Open"][1]
print "High:",goog["High"][1]
print "Low:",goog["Low"][1]
print "Close:",goog["Close"][1]
print "Volume:",goog["Volume"][1]
print "Adj Close:",goog["Adj Close"][1]
'''
#SPLUNK TRAINING STOCK FORMAT is STOCK-NAME,DATE(%Y-%M-%D),OPEN,HIGH,LOW,CLOSE,ADJCLOSE
logging.info(' Number of stock items for %s is %s',stockSymbolName, len(goog.index))


for stockitem in range(len(goog.index)):
    stockEntryString = stockSymbolName
    stockEntryString += ","
    stockEntryString += goog.index[stockitem].date().strftime("%Y-%m-%d")
    stockEntryString += ","
    stockEntryString += str(goog["Open"][stockitem])
    stockEntryString += ","
    stockEntryString += str(goog["High"][stockitem])
    stockEntryString += ","
    stockEntryString += str(goog["Low"][stockitem])
    stockEntryString += ","
    stockEntryString += str(goog["Close"][stockitem])
    stockEntryString += ","
    stockEntryString += str(goog["Adj Close"][stockitem])
    print stockEntryString




logging.info('END OF RUN...')
