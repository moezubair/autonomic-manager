volume = 0
noise = 0
duration = 0
symptom = ""

while 1:
	f = open('../AlarmClock/data', 'r')
	data = f.readline()

	try:
		if data != "":
			split_data = data.split(" ")

			if str(volume) != split_data[0] or str(noise) != split_data[1] or str(duration) != split_data[2]:
				volume = int(split_data[0])
				noise = int(split_data[1])
				duration = int(split_data[2])

				# Volume too low
				if volume < noise:
					symptom = "increase "
					symptom += str(noise + 1)

				# Volume too high
				elif volume > (noise + 1):
					symptom = "decrease "
					symptom += str(volume - 1)

				# Duration too high
				elif duration > 15000:
					symptom = "increase"
					symptom += str(volume + 5)

				print data
				print symptom

	except Exception, e:
		raise e
	
	
	
	