volume = 0
noise = 0
duration = 0

while 1:
	f = open('../AlarmClock/data', 'r')
	data = f.readline()

	try:
		if data != "":
			split_data = data.split(" ")

			if volume != split_data[0] or noise != split_data[1] or duration != split_data[2]:
				volume = split_data[0]
				noise = split_data[1]
				duration = split_data[2]
				print data

	except Exception, e:
		raise e
	
	
	
	