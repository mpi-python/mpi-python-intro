# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')

core.wait(1)  # wait for 1 second on a blank window

# prepare a text stimulus
text = visual.TextStim(win, text='+', color='white')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
core.wait(1)  # wait for 1 second so we can look at the window with our fixation cross

text.setText('Hi!')  # replace our text
text.draw()  # draw to back buffer again
win.flip()
core.wait(2)  # wait for 2 seconds so we can look at the window with our text

win.flip()  # flip an empty back buffer onto the screen
core.wait(1)  # wait on blank screen again

win.close()  # close the window
