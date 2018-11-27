# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event
from PIL import Image

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')


# prepare a text stimulus
text = visual.TextStim(win, text='+', color='white')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
core.wait(1)  # wait for 1 second so we can look at the window with our fixation cross

text.setText('Clockwise (a) or counterclockwise (b):')  # replace our text
text.draw()  # draw to back buffer again
win.flip()
direction = event.waitKeys(keyList = ['a', 'b'])  # wait for 2 seconds so we can look at the window with our text
win.flip()

text.setText('Speed (1-9):')  # replace our text
text.draw()  # draw to back buffer again
win.flip()
speed = event.waitKeys(keyList = ['1','2','3','4','5','6','7','8','9'])  # wait for 2 seconds so we can look at the window with our text
win.flip()

# prepare an image stimulus
hat = visual.ImageStim(win)
hat.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
im = Image.open('hat.png')

speed_n = int(speed[0])
n = 0
while True:
    key_press = event.getKeys(keyList = ['space', 'a', 'b', 'u', 'd', 'p'])
    hat.setImage(im.rotate(n))
    hat.draw()
    win.flip()
    
    if 'space' in key_press:
        break
    elif 'p' in key_press:
        speed_n = 0
    elif 'u' in key_press:
        speed_n = speed_n + 1
    elif 'd' in key_press:
        speed_n = speed_n - 1
    elif 'a' in key_press:
        direction = 'a'
    elif 'b' in key_press:
        direction = 'b'
        
    if direction == 'a':
        n = n + speed_n
    else:
        n = n - speed_n
        
win.close() 