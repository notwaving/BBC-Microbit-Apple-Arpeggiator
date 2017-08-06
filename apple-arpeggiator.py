from microbit import *


import music
pitch = 440
music.pitch(pitch)

while True:
    if pin1.is_touched():
        if pitch >= 1100:
            pitch = 440
        else: 
            pitch += 110
        music.pitch(pitch)
        sleep(100) 
   
        
    