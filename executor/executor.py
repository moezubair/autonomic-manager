__author__ = 'Muhammad Zubair'
import sys
import time
import os
import os.path
sys.path.insert(0, '../')
from KnowledgeBase import *
from types import NoneType

#Read from the tasks table

KB = KnowledgeBase()
def executor():
    todo = KB.readTasks()
    #check if task is done
    if (type(todo) is not NoneType):
        tkey = todo[0]
        akey = todo[1]
        date = todo[2]
        volume = todo[3]
        completed = todo[4]
        if (completed ==0):
            print "A task needs to be completed : ",
            print todo
            #task needs to be completed
            while (os.path.isfile('../AlarmClock/volume')):
                time.sleep(3)
            with open('../AlarmClock/volume', 'w') as f :
                f.write(str(volume))
                print "File Created with new Volume of " + str(volume)
            KB.taskCompleted(tkey)
        else:
            print "No new Task yet - the last task was : ",
            print todo

while 1:
    executor()
    time.sleep(2)