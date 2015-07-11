__author__ = 'Sparwood'
__author__ = 'Muhammad Zubair'
import sys
import time
sys.path.insert(0, '../')
from KnowledgeBase import *
from types import NoneType
##Planner needs to do the following tasks
## 1. Read latest item from the analyzer tables
## 2. Read the policy table
## 3. Calculate the new volume
## 4. Send the new volume to executor
KB = KnowledgeBase()
#[1] = Row number
#[2] = time added
#[3] = Noise
#[4] = volume
#[5] = duration
def checkifExists(rowno):
    plannerdata = KB.readTasks(rowno)
  #  print analyzerdata
    #print plannerdata
    print plannerdata,
    print " already in the table"
    if (type(plannerdata) is not NoneType):
        print plannerdata
        return True #true
    else:
        return False #False
def readData():
    data = KB.readAnalyzerData()
    if (type(data) is NoneType):
        return
    akey = data[0]
    if (checkifExists(akey) is False):
        print "Added new Planning data"
        property = data[3]
        action = data[4]
        volume = data[5]
        newVolume = volume

        if (property=="Volume"):
            #Read Policy
            multiplicity = KB.readPolicy(property,action)

            factor = multiplicity[0][3]
            if (action=="Increase"):
                newVolume += factor
            elif (action=="Decrease"):
                newVolume -= factor
            if (newVolume < 0):
                newVolume = 0
            elif (newVolume >100):
                newVolume = 100

            KB.insertTaskData(akey,newVolume)
            print "New Task added to be read by the Executor To : " + action + " "+property+" by ",
            print factor


while 1:
    readData()
    time.sleep(2)
