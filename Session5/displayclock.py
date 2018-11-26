# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')

# prepare a text stimulus
text = visual.TextStim(win, text='0', color='white')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front

# start the clock
clock = core.Clock()

# use a while loop to quit when t reaches 30 seconds
while clock.getTime() < 30:
    text.setText(f't = {clock.getTime():.2f}')  # the clock returns a float, so we format it nicely using an f-string (.2 means two decimals)
    text.draw()
    win.flip()

win.close()  # close the window
