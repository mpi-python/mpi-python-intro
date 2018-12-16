from psychopy import core, visual
import os, fnmatch
import random

## list all .png in dir
lis=[]
listOfFiles = os.listdir('.')  
pattern = "*.png"
for file in listOfFiles:  
    if fnmatch.fnmatch(file, pattern):
            lis.append(file)
# print(lis)

## create a blank canvas
win = visual.Window((800, 600), color='teal')
core.wait(3)

## loop over a folder of images, paste all of the images into a canvas at random locations
for i in range(len(lis)):
    locx = random.uniform(0.0,1.0) - 0.5
    locy = random.uniform(0.0,1.0) - 0.5
    im = visual.ImageStim(win=win, image = lis[i],pos=(locx,locy))
    im.draw()
    win.flip()
    core.wait(1)
    
core.wait(3)
win.close()