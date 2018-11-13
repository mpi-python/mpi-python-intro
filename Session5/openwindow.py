# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600))
core.wait(10)  # wait for 5 seconds so we can look at the window
win.close()  # close the window
