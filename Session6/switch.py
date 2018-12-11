#This is the code for the switch experiment 

from psychopy import core, visual, event 

win = visual.Window(color = 'white', fullscr = True) #Open a window with a white background, full screen instead of pixels 

core.wait(2)  # Wait two seconds

# prepare a text stimulus
text = visual.TextStim(win, text='Welcome to this experiment', color='Black', font = 'arial')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
core.wait(5)  # wait

image = visual.ImageStim(win, None)
image.draw()  # draw the stimulus to the back buffer
win.flip() 

#class psychopy.voicekey.OffsetVoiceKey(sec=10, file_out='', file_in='', delay=0.3, **kwargs)

while True:
    keys = event.getKeys(keyList=['space', 'escape'])
    
    if 'escape' in keys:
        break
                                     
    text.setText('In this experiment, you will get to see pictures. Your task is to name the pictures as quickly as possible.')
    text.draw()  # draw to back buffer again
    win.flip()
    core.wait(2)  # wait for 8 seconds so we can look at the window with our text
    
    text.setText('However, there is a catch.')
    text.draw() 
    win.flip()
    core.wait(2)  
    
    text.setText('If you see a picture on the LEFT side of the screen, name the picture in English.')
    text.draw()  
    win.flip()
    core.wait(2)

    text.setText('If you see a picture on the RIGHT side of the screen, name the picture in Dutch.')
    text.draw()
    win.flip()
    core.wait()

    text.setText('Before we get started, here are a few items to practice.')
    text.draw()
    win.flip()
    core.wait(8)
  
    image.setImage(f'{1}.png')
    image.draw()
    win.flip()
    core.wait(5)

    win.flip()  # flip an empty back buffer onto the screen
    core.wait(1)  # wait on blank screen again
    
win.close()  # close the window
core.quit()
