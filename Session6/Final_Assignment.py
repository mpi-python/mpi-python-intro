#import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event
import pandas as pd
import numpy as np
import os
from PIL import Image
import subprocess as sp
import sounddevice as sd
import soundfile as sf

# import input list
input_list = pd.read_excel('List_random.xlsx')
# settings to record
sd.default.samplerate = 48000  # set sounddevice to record at 48k samples per second
sd.default.channels = 1

# open a window
win = visual.Window((1200, 700), color='black')

core.wait(1)  # wait for 1 second on a blank window

participant = visual.TextStim(win, text='participant number', color='white')
participant.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
p_num = event.waitKeys(keyList = ['1','2','3','4','5','6','7','8','9'], maxWait = 300)  # wait for 1 second so we can look at the window 
os.mkdir(f'C:/Users/lauri/mpi-python-intro/Session6/Output/{str(p_num[0])}')


## INSTRUCTION SCREENS
instructions = visual.TextStim(win, text=f'Instructions: \nyou will see two verbs, which will be followed by 4 shapes.' \
                               + f'You have to describe the scene using the verbs and the shapes highlighted in white.' \
                               + f'Press space to see an example', color='white')
instructions.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
event.waitKeys(keyList = 'space', maxWait = 100)  # wait for 1 second so we can look at the window with our fixation cross
win.flip()
verbs = visual.TextStim(win, text = '', color='white')

# prepare two verbs for presentation
verbs.setText(f'{input_list.Verb[59]}       {input_list.Verb2[59]}' )
verbs.pos = (0,0.4)
    
# prepare shapes for subject\sent1
shape1 = visual.Rect(win, width = 0.15, height = 0.2, fillColor = input_list.Color1[59], lineWidth = 3, \
                     lineColor = input_list.Focus1[59], pos=(-0.6,0))
shape2 = visual.Rect(win, width = 0.15, height = 0.2, fillColor = input_list.Color2[59], lineWidth = 3, \
                     lineColor = input_list.Focus2[59], pos=(-0.2,0))
# prepare shapes for object\sent2    
shape3 = visual.Circle(win, radius = 0.1, fillColor = input_list.Color3[59], lineWidth = 3, \
                       lineColor = input_list.Focus3[59], pos=(0.2,0))
shape4 = visual.Circle(win, radius = 0.1, fillColor = input_list.Color4[59], lineWidth = 3, \
                       lineColor = input_list.Focus4[59], pos=(0.6,0))
# select which objects are highlighted   
cond1 = visual.Rect(win, width = 1.6, height = 0.6, fillColor = None, lineWidth = 3, lineColor = 'white')
cond2 = visual.Rect(win, width = 0.75, height = 0.4, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.4,0))
instructions.setText('The expected output is : \nHet groene vierkant gelooft dat de gele cirkel danst')
instructions.pos = (0,-0.5)
verbs.draw()
shape1.draw()
shape2.draw()
shape3.draw()
shape4.draw()
cond1.draw()
cond2.draw()
instructions.draw() 
win.flip()
event.waitKeys(keyList = 'space', maxWait = 100) 
   
# change highlighting for different condition: int example
cond1 = visual.Rect(win, width = 0.75, height = 0.4, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.4,0))
cond2 = visual.Rect(win, width = 0.75, height = 0.4, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.4,0))
instructions.setText('The expected output is : \nHet groene vierkant gelooft en de gele cirkel danst')
instructions.draw()  
verbs.draw()
shape1.draw()
shape2.draw()
shape3.draw()
shape4.draw()
cond1.draw()
cond2.draw()
win.flip()
event.waitKeys(keyList = 'space', maxWait = 100)

  
# change highlighting for different condition: NP example
cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.6,0))
cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.2,0))
instructions.setText('The expected output is:\nHet groene vierkant \nGeloven \nDe gele cirkel \nDansen')
instructions.draw()
verbs.draw()
shape1.draw()
shape2.draw()
shape3.draw()
shape4.draw()
cond1.draw()
cond2.draw()
win.flip()
event.waitKeys(keyList = 'space', maxWait = 100)
          
# change highlighting for different condition: W list example
cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'black', pos=(-0.6,0))
cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'black', pos=(0.6,0))
instructions.setText('The expected output is : Groen \tVierkant \tGeloven \tGeel \tCirkel \tDansen. \nWhen you are done describing the scene press space to move on. \nYou are now ready to start.')
instructions.draw()
verbs.draw()
shape1.draw()
shape2.draw()
shape3.draw()
shape4.draw()
cond1.draw()
cond2.draw()
win.flip()
event.waitKeys(keyList = 'space', maxWait = 100)

#initiate array to save RTs
times_array = np.zeros((60,2), dtype = float)

# experiment starts 
for trial in range(0,60):
    key_press = event.getKeys('escape')
    if 'escape' in key_press:
        break
    # prepare a text stimulus
    text = visual.TextStim(win, text='+', color='white')
    text.draw()  # draw the stimulus to the back buffer
    win.flip()  # flip the back buffer with our stimulus to the front
    core.wait(0.3)  # wait for 1 second so we can look at the window with our fixation cross

      
# prepare shapes for subject\sent1
    if input_list.Subject[trial] == 'square':
        shape1 = visual.Rect(win, width = 0.15, height = 0.2, fillColor = input_list.Color1[trial], lineWidth = 3, \
                             lineColor = input_list.Focus1[trial], pos=(-0.6,0))
        shape2 = visual.Rect(win, width = 0.15, height = 0.2, fillColor = input_list.Color2[trial], lineWidth = 3, \
                             lineColor = input_list.Focus2[trial], pos=(-0.2,0))
    elif input_list.Subject[trial] == 'circle':
        shape1 = visual.Circle(win, radius = 0.1, fillColor = input_list.Color1[trial], lineWidth = 3, \
                               lineColor = input_list.Focus1[trial], pos=(-0.6,0))
        shape2 = visual.Circle(win, radius = 0.1, fillColor = input_list.Color2[trial], lineWidth = 3, \
                               lineColor = input_list.Focus2[trial], pos=(-0.2,0))
    else:
        shape1 = visual.Polygon(win, radius = 0.1, fillColor = input_list.Color1[trial], lineWidth = 3, \
                                lineColor = input_list.Focus1[trial], pos=(-0.6,0))
        shape2 = visual.Polygon(win, radius = 0.1, fillColor = input_list.Color2[trial], lineWidth = 3, \
                                lineColor = input_list.Focus2[trial], pos=(-0.2,0))
# prepare shapes for object\sent2    
    if input_list.Object[trial] == 'square':
        shape3 = visual.Rect(win, width = 0.15, height = 0.2, fillColor = input_list.Color3[trial], lineWidth = 3, \
                             lineColor = input_list.Focus3[trial], pos=(0.2,0))
        shape4 = visual.Rect(win, width = 0.15, height = 0.2, fillColor = input_list.Color4[trial], lineWidth = 3, \
                             lineColor = input_list.Focus4[trial], pos=(0.6,0))
    elif input_list.Object[trial] == 'circle':
        shape3 = visual.Circle(win, radius = 0.1, fillColor = input_list.Color3[trial], lineWidth = 3, \
                               lineColor = input_list.Focus3[trial], pos=(0.2,0))
        shape4 = visual.Circle(win, radius = 0.1, fillColor = input_list.Color4[trial], lineWidth = 3, \
                               lineColor = input_list.Focus4[trial], pos=(0.6,0))
    else:
        shape3 = visual.Polygon(win, radius = 0.1, fillColor = input_list.Color3[trial], lineWidth = 3, \
                                lineColor = input_list.Focus3[trial], pos=(0.2,0))
        shape4 = visual.Polygon(win, radius = 0.1, fillColor = input_list.Color4[trial], lineWidth = 3, \
                                lineColor = input_list.Focus4[trial], pos=(0.6,0))
# select which highlighting to specify condition    
    if input_list.Condition[trial] == 'CP':
        cond1 = visual.Rect(win, width = 1.6, height = 0.6, fillColor = None, lineWidth = 3, lineColor = 'white')
        cond2 = visual.Rect(win, width = 0.75, height = 0.4, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.4,0))
    elif input_list.Condition[trial] == 'INT':
        cond1 = visual.Rect(win, width = 0.75, height = 0.4, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.4,0))
        cond2 = visual.Rect(win, width = 0.75, height = 0.4, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.4,0))
    elif input_list.Condition[trial] == 'NP':
        if input_list.Order[trial] == 11:
            cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.6,0))
            cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.2,0))
        elif input_list.Order[trial] == 12:
            cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.6,0))
            cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.6,0))
        elif input_list.Order[trial] == 21:
            cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.2,0))
            cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.2,0))
        else:
            cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(-0.2,0))
            cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'white', pos=(0.6,0))

    else:
        cond1 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'black', pos=(-0.6,0))
        cond2 = visual.Rect(win, width = 0.35, height = 0.3, fillColor = None, lineWidth = 3, lineColor = 'black', pos=(0.6,0))
    # prepare verbs and draw 
    verbs.setText(f'{input_list.Verb[trial]}       {input_list.Verb2[trial]}')  # replace our text
    verbs.draw()  # draw to back buffer again
        
    shape1.draw()
    shape2.draw()
    shape3.draw()
    shape4.draw()
    cond1.draw()
    cond2.draw()
    win.flip()
    # start the clock
    clock = core.Clock()
    timepres = clock.getTime()
    samples = sd.rec(10 * sd.default.samplerate)
    #sd.wait()
    event.waitKeys(keyList = 'space', maxWait = 15)
    timeresp = clock.getTime()
    
    sf.write(f'C:/Users/lauri/mpi-python-intro/Session6/Output/{str(p_num[0])}/{trial+1}.wav', samples, sd.default.samplerate)
    
    if trial == 14 or trial == 29 or trial == 44:
        textpause = visual.TextStim(win, text='You can take a break now. Press space when you are ready to start', color='white')
        textpause.draw()  # draw the stimulus to the back buffer
        win.flip()  # flip the back buffer with our stimulus to the front
        event.waitKeys(keyList = 'space', maxWait = 300)  # wait for 1 second so we can look at the window with our fixation cross

    # save times in array    
    times_array[trial,0] = timepres
    times_array[trial,1] = timeresp
    
    win.flip()
    core.wait(0.3)

# save data to csv    
times = pd.DataFrame(times_array, columns = ['Present time', 'RT'])
times.to_csv(f'{p_num}resptime.csv')
    
endtext = visual.TextStim(win, text='The experiment is now over. Bedankt voor je deelname.', color='white')
endtext.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
event.waitKeys(keyList = 'space', maxWait = 100)  # wait for 1 second so we can look at the window with our fixation cross


win.close()  # close the window