class State(object):
	
	def update(self, volume, noise, duration):
		f = open('data', 'w')
		self.volume = volume
		self.noise = noise
		self.duration = duration
		string = str(self.volume)
		string += " "
		string += str(self.noise)
		string += " "
		string += str(self.duration)
		f.write(string)
		f.close()


	def __init__(self, volume, noise, duration):
		self.volume = volume
		self.noise = noise
		self.duration = duration
		