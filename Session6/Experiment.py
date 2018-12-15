from psychopy import core, visual, event
import os, numpy, pprint, SaveData
from PIL import Image


# Make the stims
os.chdir("C:/Users/limrav/mpi-python-intro/Session6/stims")

files = 'apple.bmp', 'banana.bmp', 'frog.bmp' , 'horse.bmp', 'rose.bmp' , 'sunflower.bmp'
pics=[]
pics_names=[]
words=[]
responses = []

for name in files:
        pics.append(Image.open(name))
        word=str(name)
        word=word.replace(".bmp","")
        words.append(word)
        pics_names.append(word)

# randomize the stims
stims_words = numpy.random.choice(range(0,6), size=50, replace=True)
stims_pics = numpy.random.choice(range(0,6), size=50, replace=True)

# Opening screen
win = visual.Window((800, 600), color = 'white') # open a window of 800 by 600 pixels 
core.wait(1) 

# prepare a text stimulus
text = visual.TextStim(win, text='Welcome!', color='black')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
core.wait(2)  # wait for 2 seconds

text.setText('For the next few minutes, you will see pictures and words. Your goal is to match the picture to the word as fast as you can. Click "A" if the picture matches the word, and "K" if it does not match. You can exit at any time using the Esc button.')  # replace our text with instructions
text.draw()  # draw to back buffer again
win.flip()
core.wait(5)  # wait for XX seconds so we can read the instructions

win.flip()  # flip an empty back buffer onto the screen
core.wait(1)  # wait on blank screen again

# Run the experiment

clock = core.Clock()
cross = visual.TextStim(win, text='+', color='black') # fixation cross
image = visual.ImageStim(win, None)
fileName = "mylogfile.csv"  


n=0 

while n < 10: # no. of trials   
    # show the image for 1 sec
    image.setImage(pics[stims_pics[n]]) 
    image.draw()
    win.flip()
    core.wait(1) 
    # show a cross                    
    cross.draw()  
    win.flip()  
    core.wait(0.5) 
    # show the word for 1 sec
    text = visual.TextStim(win, text=words[stims_words[n]], color='black')
    text.draw()
    win.flip()
        #wait for a button press
    keys = event.waitKeys(keyList=['escape','a', 'k'],timeStamped=clock)
    if keys: # if at least one key exists in the list
        if 'escape' in keys: 
            core.quit()
            win.close()
        # For some reason, this is NOT working - I tried everything, including "break" and sys.exit() - but it just skips to next trial
        # I spent over an hour searching the web for explanations/solutions, but in all cases the Esc button just moved on to the next trial
        else:
            if pics_names[stims_pics[n]] == words[stims_words[n]]:
                 acc=1
            else:
                 acc=0
        # SaveData.SaveData(n,pics_names[stims_pics[n]],words[stims_words[n]],str(keys[1]),acc) 
        # I tried to save the data after each trial but this doesn't work...
        # I have already spent more than 8 hours on this, so at this point I'm letting it go - sorry...
        n += 1       

# End experiment
text = visual.TextStim(win, text='Thank you for participating!', color='black')
text.draw()
win.flip()
core.wait(1)
win.close()  # close the window
