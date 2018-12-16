import subprocess as sp
from PIL import Image
from psychopy import core, visual,event
import os,fnmatch,random

## open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800,600),color = 'teal')
text = visual.TextStim(win, text='0', color='white',pos = (0.5,-0.5))
text1 = visual.TextStim(win, text='0', color='white',pos = (0,0.5))
im = Image.open('hat.png')

## display the clock and the image
clock = core.Clock()
i = 0

## 5.x.1 display image every second, and rotate 60 degree
while clock.getTime() < 5:    
    text.setText(f't = {clock.getTime():.2f}')  # the clock returns a float, so we format it nicely using an f-string
    text.draw()
    text1.setText('display image every second, and rotate 60 degree')
    text1.draw()
    i += 1
    imm = visual.ImageStim(win = win, image = im.rotate(60*i),units='pix') # rotate the image 60 degree each time and display every second
    imm.draw()
    win.flip()
    core.wait(1)

## 5.x.2 speech up by skipping a image    
while clock.getTime() < 10:    
    text.setText(f't = {clock.getTime():.2f}')  # the clock returns a float, so we format it nicely using an f-string
    text.draw()
    text1.setText('speed up by skipping a image')
    text1.draw()
    i += 1
    imm = visual.ImageStim(win = win, image = im.rotate(120*i),units='pix') # rotate the image 60 degree each time and display every second
    imm.draw()
    win.flip()
    core.wait(1)
    
## 5.x.3 press space bar to stop
while clock.getTime() < 15:
    press = event.getKeys(keyList = ['space'])
    if 'space' in press:
        break
    text.setText(f't = {clock.getTime():.2f}')  # the clock returns a float, so we format it nicely using an f-string
    text.draw()
    text1.setText('press spacebar to stop')
    text1.draw()
    i += 1
    imm = visual.ImageStim(win = win, image = im.rotate(120*i),units='pix') # rotate the image 60 degree each time and display every second
    imm.draw()
    win.flip()
    core.wait(1)

## 5.x.4 Handing over control to the participant
i = 1
speed = 6
while clock.getTime() < 30:
    keypress = event.getKeys(keyList = ['escape','space','up','down'])
    if 'escape' in keypress:
        break
    elif 'space' in keypress:
        event.waitKeys(keyList = 'space')
    elif 'up' in keypress:
        speed += 1
    elif 'down' in keypress:
        speed -= 1
    text.setText(f't = {clock.getTime():.2f}')  # the clock returns a float, so we format it nicely using an f-string
    text.draw()
    text1.setText('press spacebar to stop/start, press excape to break, press up/down arrow to speed up/down')
    text1.draw()
    i += 1
    imm = visual.ImageStim(win = win, image = im.rotate(10*i*speed),units='pix') # rotate the image 60 degree each time and display every second
    imm.draw()
    win.flip()
    core.wait(1)    

    