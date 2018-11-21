# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')

# start the clock
clock = core.Clock()


for deg in range(1,361),10):
        # prepare an image stimulus
    image_file = ('hat' + str(deg) + '.png')
    img = visual.ImageStim(win, image = image_file)
    img.draw()
    win.flip()
    while clock.getTime() > 10:
        break

win.close()