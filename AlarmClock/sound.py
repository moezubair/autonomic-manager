import pyglet

class Sound():

	def playSound(self):
		self.player.play()

	def stopSound(self):
		self.player.pause()

	def __init__(self, filename):
		self.player = pyglet.media.Player()
		self.sound = pyglet.media.load(filename)
		self.player.queue(self.sound)
		self.player.eos_action = pyglet.media.Player.EOS_LOOP