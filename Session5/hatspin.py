import subprocess as sp
from PIL import Image
from psychopy import core, visual,event

im = Image.open('hat.png')
# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')
core.wait(3)

im = visual.imageStim(win=win,image='hat.png',units='pix')
im.draw()
win.flip()

# for i in range(36):
clock = core.Clock()

while True:
    if clock.getTime() == 1:
    rotated = im.rotate(10)
    im = visual.ImageStim(win=win,image=rotated,units='pix')
    im.draw()
    win.flip()
    