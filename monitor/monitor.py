import sys
sys.path.insert(0, '../')
from KnowledgeBase import *
import time

volume = 0
noise = 0
duration = 0
symptom = ""
KB = KnowledgeBase()

while 1:
	f = open('../AlarmClock/data', 'r')
	data = f.readline()

	try:
		if data != "":
			split_data = data.split(" ")

			if volume != split_data[0] or noise != split_data[1] or duration != split_data[2]:
				volume = int(split_data[0])
				noise = int(split_data[1])
				duration = float(split_data[2])

				KB.insertMonitorData(noise, volume, duration)


	except Exception, e:
		raise e
	time.sleep(2)
	
	
	