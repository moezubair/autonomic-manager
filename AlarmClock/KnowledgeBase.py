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
        c.execute('''Create TABLE if not exists Symptoms
                    (skey integer primary key, mkey integer, date timestamp, property string, symptom string)''')

        #Create table for Planner to create tasks
        c.execute('''Create TABLE if not exists Tasks
                    (tkey integer primary key, skey integer, date timestamp, volume int)''')
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
    def readData(self,quantity="one",condition="",order="",table):
        #Read monitor data log, this is used by the analyzer to read the latest monitor data value
        global database
        result = ""
        conn = sqlite3.connect(self.database)
        c=conn.cursor()
        query = "SELECT * FROM "+table
        query += ("" if condition=="" else " WHERE "+condition)
        query += ("" if order=="" else " ORDER BY "+order)
        print query
        #c.execute("SELECT * FROM MonitorDataLog ORDER BY date desc")
        c.execute(query)
        if (quantity=="one"):
            result= c.fetchone()
        else:
            result= c.fetchall()
        conn.commit()
        conn.close()
        return result
    #############Analyzer###############


    ############Planner#################
    ### Write to Tasks (VOLUME)
    ###

    #########EXECUTOR##################
    ### READ From Tasks
    ###
    def readTasks(self):
        global database
        conn = sqllite3.connect(self.database)
        c=conn.cursor()
        c.execute("SELECT * FROM Tasks WHERE executed=0 ORDER BY date desc")
        return c.fetchall()
    def __init__(self):
       self.database = 'knowledge.db'

Knowledge = KnowledgeBase()
Knowledge.createTables()
Knowledge.insertMonitorData(5,3,5)
print Knowledge.readData("one",,"date desc")