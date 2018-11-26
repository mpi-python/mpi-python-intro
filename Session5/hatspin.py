# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')

degree_list = [deg + 1 for deg in range(360)]

hat = visual.ImageStim(win)
hat.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front

# s = start spinning
# d = reverse
# f = fast
# g = slow
# h = pause
# space = stop spinning

while True:
    response = event.getKeys()
    if "s" in response:
        for degree in degree_list:
            hat.setImage(f'C:\\Users\\Marloes Mak\\mpi-python-intro\\Session5\\hats\\hat_{degree}.png')
            hat.draw()
            win.flip()
    if "d" in response:
        for degree in degree_list:
            hat.setImage(f'C:\\Users\\Marloes Mak\\mpi-python-intro\\Session5\\hats\\hat_{361 - degree}.png')
            hat.draw()
            win.flip()
    if "f" in response:
        for degree in degree_list:
            if degree % 2 == 0:
                continue
            hat.setImage(f'C:\\Users\\Marloes Mak\\mpi-python-intro\\Session5\\hats\\hat_{degree}.png')
            hat.draw()
            win.flip()
    if "g" in response:
        for degree in degree_list:
            hat.setImage(f'C:\\Users\\Marloes Mak\\mpi-python-intro\\Session5\\hats\\hat_{degree}.png')
            hat.draw()
            win.flip()
    if "h" in response:
        hat.setImage(f'C:\\Users\\Marloes Mak\\mpi-python-intro\\Session5\\hats\\hat_{degree}.png')
        hat.draw()
        win.flip()
    if "space" in response:
        break

win.close()  # close the window
