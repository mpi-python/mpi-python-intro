from psychopy import core, visual, event
import os 

# set the stims directory
os.chdir("./RotatedPic")

win = visual.Window((800, 600), color = 'orange') # open a window of 800 by 600 pixels 
core.wait(3) #show window for n seconds

image = visual.ImageStim(win, None)
image.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front


# X1 - show all stims 

n = 0
while n < 360:
    image.setImage(f'Hat{n}.png')
    image.draw()
    win.flip()
    core.wait(0.1)
    n += 1   
win.close()  # close the window

# X2 - skip to show every second stim

n = 0
while n < 360:
    image.setImage(f'Hat{n}.png')
    image.draw()
    win.flip()
    core.wait(0.1)
    n += 2
win.close()  # close the window


# X3 - spress pace bar to stop

n = 0
while n < 360:
    press = event.getKeys(keyList=['space'])
    if 'space' in press:
        break        
    image.setImage(f'Hat{n}.png')
    image.draw()
    win.flip()
    core.wait(0.1)
    n += 2
win.close()  # close the window


# X4 - Participant in control

n = 0
t = 0.2
while n < 360:
    press = event.getKeys(keyList=['escape', 'space', 'up', 'down', 'right', 'left'])
    if 'escape' in press:
        break 
    elif 'space' in press:
        event.waitKeys(keyList = 'space')
    elif 'up' in press: 
        t -= 1
    elif 'down' in press: 
        t += 1
    elif 'right' in press: 
        n += 1
    elif 'left' in press: 
        n -= 1
        
    image.setImage(f'Hat{n}.png')
    image.draw()
    win.flip()
    core.wait(t)
    n += 1
    
win.close()  # close the window

