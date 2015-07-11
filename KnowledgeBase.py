import sqlite3
import datetime
class KnowledgeBase:
    def createTables(self):
        global database
        conn = sqlite3.connect(self.database)
        c=conn.cursor()
        #Create table for Monitor to store data to
        c.execute('''Create TABLE if not exists MonitorDataLog
                    (mkey integer primary key,date timestamp, NoiseLevel int,VolumeLevel, Duration real)''')
        #Create table for Analyzer to store data to
        c.execute('''Create TABLE if not exists AnalyzerDataLog
                    (akey integer primary key, mkey integer, date timestamp, property string, action string)''')

        #Create table for Planner to create tasks
        c.execute('''Create TABLE if not exists Tasks
                    (tkey integer primary key, akey integer, date timestamp, volume int)''')
        #Create table for policy
        c.execute('''Create TABLE if not exists Policy
                    (policykey integer primary key, property string, action string, value int)''')
        conn.commit()
        conn.close()
    def insertMonitorData(self,noise, volume, duration):
        #Insert to the monitor data log table. This is used by the monitor component
        global database
        conn = sqlite3.connect(self.database)
        #Insert data into monitordatalog
        c = conn.cursor()
        c.execute('Insert INTO MonitorDataLog VALUES (NULL,?,?,?,?)',(datetime.datetime.now(),noise,volume,duration))
        conn.commit()
        conn.close()
    def readMonitorData(self,quantity="one"):
        #Read monitor data log, this is used by the analyzer to read the latest monitor data value
        global database
        result = ""
        conn = sqlite3.connect(self.database)
        c=conn.cursor()
        c.execute("SELECT * FROM MonitorDataLog ORDER BY date desc")
        if (quantity=="one"):
            result= c.fetchone()
        else:
            result= c.fetchall()
        conn.commit()
        conn.close()
        return result
    #############Analyzer###############

    def insertAnalyzerData(self,monitorkey,property,action ):
    ############Planner#################
    ### Write to Tasks (VOLUME)
    ###
   #Insert to the analyzer data log table. This is used by the anaylzer component
        global database
        conn = sqlite3.connect(self.database)
        #Insert data into monitordatalog
        c = conn.cursor()
        c.execute('Insert INTO AnalyzerDataLog VALUES (NULL,?,?,?,?)',(datetime.datetime.now(),monitorkey,property,action))
        conn.commit()
        conn.close()
    #########EXECUTOR##################
    ### READ From Tasks
    ###
    def readTasks(self):
        global database
        conn = sqlite3.connect(self.database)
        c=conn.cursor()
        c.execute("SELECT * FROM Tasks WHERE executed=0 ORDER BY date desc")
        return c.fetchall()
    def createPolicy(self):
        global database

        conn = sqlite3.connect(self.database)
        c=conn.cursor()
        c.execute ("SELECT COUNT(*) FROM Policy")
        counter = c.fetchone()
       # print counter
        if (counter[0] == 0 ):
            c.execute('INSERT INTO Policy VALUES (NULL,?,?,?)',("Volume","Increase",10))
            c.execute('INSERT INTO Policy VALUES (NULL,?,?,?)',("Volume","Decrease",10))
            c.execute('INSERT INTO Policy VALUES (NULL,?,?,?)',("Duration","None",10000))

        conn.commit()
        conn.close()
    def readPolicy(self,Policy="all"):
        #Read monitor data log, this is used by the analyzer to read the latest monitor data value
        global database
        result = ""
        conn = sqlite3.connect(self.database)
        c=conn.cursor()
        if (Policy=="all"):
            c.execute("SELECT * FROM Policy ORDER BY policykey asc")
            result= c.fetchall()
        else:
            query = "Select * FROM Policy WHERE property = '"+Policy+"'"
            c.execute(query)
            result=c.fetchall()
        conn.commit()
        conn.close()
        return result
    def __init__(self):
       self.database = '../knowledge.db'
       self.createTables()

       self.createPolicy()

#Knowledge = KnowledgeBase()
#Knowledge.createTables()
#Knowledge.insertMonitorData(5,3,5)
#NOISE, VOLUME, DURATION
#print Knowledge.readMonitorData()