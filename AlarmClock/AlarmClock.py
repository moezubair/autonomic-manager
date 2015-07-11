from Tkinter import *
from sound import *
from noise import *
from state import *
import time
import os
import os.path
class AlarmClock(Frame):

    def createWidgets(self):

        self.clock = Label(font=('courier', 20, 'bold'), bg='black', fg='green')
        self.clock.pack()

        self.alarm = StringVar()
        self.alarm.set("HH:MM")

        self.alarm_entry = Entry()
        self.alarm_entry.pack({"side": "bottom"})  
        self.alarm_entry["textvariable"] = self.alarm

        self.stop_alarm = Button(self)
        self.stop_alarm["text"] = "Stop Alarm"
        self.stop_alarm["command"] = self.stopAlarm
        self.stop_alarm.pack({"side":"bottom"})

        self.set_alarm = Button(self)
        self.set_alarm["text"] = "Set Alarm"
        self.set_alarm["command"] = self.setAlarm
        self.set_alarm.pack({"side": "bottom"})    
        
        self.volume_slider = Scale(length=140, label='Volume', from_=100, to=0)
        self.volume_slider.pack({"side":"right"})
        self.volume_slider.set(self.volume)

        self.sensor_data = Scale(length=140, label='Noise', from_=100, to=0)
        self.sensor_data.pack({"side":"left"})
        self.sensor_data.set(self.noise_generator.value)

        self.alarm_sound = Sound('boom.wav')


    def setAlarm(self):
        self.alarm_set = True
        print (self.alarm.get())

    def stopAlarm(self):
        self.alarm_sound.stopSound()
        self.alarm_set = False
        self.alarm_playing = False
        print ("Stop alarm")

    def tick(self):
        self.volume = self.volume_slider.get()
        self.time2 = time.strftime('%H:%M:%S')
        if (os.path.isfile('volume')):
            with open('volume', 'r') as f :
                self.setVolume(int (f.readline()))
            os.remove('volume')
        if self.time2 != self.time1:
            self.time1 = self.time2
            self.clock.config(text=self.time2)

        if self.alarm.get() == time.strftime('%H:%M') and self.alarm_set and not self.alarm_playing:
            self.alarm_sound.playSound()
            self.alarm_playing = True

        if self.alarm_playing:
            duration += 200

        if self.state.volume != self.volume or self.state.duration != self.duration:
            self.state.update(self.volume, self.noise, self.duration)
        

        # calls itself every 200 milliseconds
        # to update the time display as needed
        self.clock.after(200, self.tick)

    def updateNoise(self):
        self.noise_generator.senseNoise()
        self.noise = self.noise_generator.value
        self.sensor_data.set(self.noise)
        self.sensor_data.after(20000, self.updateNoise)
        self.state.update(self.volume, self.noise, self.duration)

    def increaseVolume(self, n):
        if self.volume < 100:
            self.volume += n
            self.volume_slider.set(self.volume)
            self.alarm_sound.soundVolume(self.volume/100)
            self.state.update(self.volume, self.noise, self.duration)
    def setVolume(self, n):

        self.volume = n
        self.volume_slider.set(self.volume)
        self.alarm_sound.soundVolume(self.volume/100)
        self.state.update(self.volume, self.noise, self.duration)


    def decreaseVolume(self, n):
        if self.volume > 0:
            self.volume -= n
            self.volume_slider.set(self.volume)
            self.alarm_sound.soundVolume(self.volume/100)
            self.state.update(self.volume, self.noise, self.duration)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack({"side": "bottom"})
        self.volume = 50.0
        self.noise_generator = Noise()
        self.noise = self.noise_generator.senseNoise()
        self.duration = 0

        self.state = State(self.volume, self.noise, self.duration)

        self.time1 = ''
        self.alarm_set = False
        self.alarm_playing = False
        self.createWidgets()
        self.tick()
        self.updateNoise()
        

root = Tk()
root.title ("Simple Alarm Program")
root.geometry("350x350+300+300")
app = AlarmClock(master=root)
app.mainloop()
root.destroy()


