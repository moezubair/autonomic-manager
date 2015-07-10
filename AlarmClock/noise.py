from random import randint

class Noise(object):

	def senseNoise(self):
		self.value = randint(0,100)

	def __init__(self):
		self.value = randint(0,100)
		