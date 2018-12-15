from psychopy import core, visual, event

win = visual.Window((800, 600), color = 'blue') # open a window of 800 by 600 pixels 
core.wait(1) 

# prepare a text stimulus
text = visual.TextStim(win, text='Welcome!', color='white')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
core.wait(2)  # wait for 2 seconds

text.setText('For the next few minutes, you will see pictures and words. Your goal is to match the picture to the word as fast as you can. Click "A" if the picture matches the word, and "K" if it does not match.')  # replace our text with instructions
text.draw()  # draw to back buffer again
win.flip()
core.wait(5)  # wait for 3 seconds so we can read the instructions

win.flip()  # flip an empty back buffer onto the screen
core.wait(1)  # wait on blank screen again
