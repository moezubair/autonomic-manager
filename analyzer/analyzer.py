__author__ = 'Muhammad Zubair'
import sys
import time
sys.path.insert(0, '../')
from KnowledgeBase import *
from types import NoneType
##Analyzer needs to do the following tasks
## 1. Read latest item from the monitor tables
## 2.
KB = KnowledgeBase()
#[1] = Row number
#[2] = time added
#[3] = Noise
#[4] = volume
#[5] = duration
def checkifExists(rowno):
    analyzerdata = KB.readAnalyzerData(rowno)
  #  print analyzerdata
    if (type(analyzerdata) is not NoneType):
        return True #true
    else:
        return False #False
def readData():
    data = KB.readMonitorData()
    if (type(data) is not NoneType):
        noise = data[2]
        rowid = data[0]
        time = data[1]
        volume = data[3]
        duration = data[4]
        action =""
        property = ""
        print data
        if (checkifExists(rowid) == False):
            print "Added data"
        #Read policy
            duration = KB.readPolicy("Duration")
            #print duration
            duration_limit = duration[0][3]
            if (noise > volume):
                #increase volume
                action ="Increase"
                property ="Volume"
            elif (duration > duration_limit):
                action = "Increase"
                property = "Volume"
            KB.insertAnalyzerData(rowid,property,action,volume)

while 1:
    readData()
    time.sleep(2)
