#This is the code for the switch experiment 

from psychopy import core, visual, event 

win = visual.Window(color = 'white', fullscr = True) #Open a window with a white background, full screen instead of pixels 

core.wait(2)  # Wait two seconds

# prepare a text stimulus
text = visual.TextStim(win, text='Welcome to my first experiment', color='Black', font = 'arial')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
core.wait(5)  # wait for 1 second so we can look at the window with our fixation cross

while True:
    keys = event.getKeys(keyList=['space', 'escape'])
    
    if 'escape' in keys:
        break
        
    elif 'space' in keys:
        event.waitKeys(keyList=['space'])
        
##Omdat je hier dezelfde vier regels telkens herhaalt, kun je hier ook een functie voor schrijven, waarbij je alleen de tijd en de tekst zelf aanpast. Maar dit kan ook. 
        
                                
    text.setText('In this experiment, you will get to see pictures. Your task is to name the pictures as quickly as possible.')
    text.draw()  # draw to back buffer again
    win.flip()
    core.wait(8)  # wait for 8 seconds so we can look at the window with our text
    
    text.setText('However, there is a catch.')
    text.draw() 
    win.flip()
    core.wait(5)  
    
    text.setText('If you see a picture on the LEFT side of the screen, name the picture in English.')
    text.draw()  
    win.flip()
    core.wait(8)

    text.setText('If you see a picture on the RIGHT side of the screen, name the picture in Dutch.')
    text.draw()
    win.flip()
    core.wait(8)

    text.setText('Before we get started, here are a few items to practice.')
    text.draw()
    win.flip()
    core.wait(8)

    win.flip()  # flip an empty back buffer onto the screen
    core.wait(1)  # wait on blank screen again

win.close()  # close the window
