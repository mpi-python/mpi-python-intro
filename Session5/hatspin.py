# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event
import os 
os.chdir("./Rotated")

win = visual.Window((800, 600), color = 'orange') # open a window of 800 by 600 pixels 
core.wait(3) #show window for n seconds

image = visual.ImageStim(win, None)
image.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front

count = 1
counter = 1

while True:
    keys = event.getKeys(keyList=['space', 'escape', 'up', 'down', 'right', 'left'])
    
    if 'escape' in keys:
        break
        
    elif 'space' in keys:
        event.waitKeys(keyList=['space'])
        
    elif 'up' in keys:
        counter += 1
                              
    
    image.setImage(f'Hat{count}.png')
    image.draw()
    win.flip()
    
    count += counter
    
    if count > 360:
        count = 1
    if count < 1:
        count = 360
    
win.close()  # close the window
