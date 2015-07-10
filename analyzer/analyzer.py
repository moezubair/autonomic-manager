__author__ = 'Muhammad Zubair'
import sys
sys.path.insert(0, '../')
from KnowledgeBase import *

##Analyzer needs to do the following tasks
## 1. Read latest item from the monitor tables
## 2.
KB = KnowledgeBase()
#[1] = Row number
#[2] = time added
#[3] = Noise
#[4] = volume
#[5] = duration
data = KB.readMonitorData()
noise = data[2]
rowid = data[0]
time = data[1]
volume = data[3]
duration = data[4]
action =""
property = ""
#Read policy
duration-poicy = KB.readPolicy("Duration")
if (noise > volume):
    #increase volume
    action ="Increase"
    property ="Volume"
if (duration > )

print data
