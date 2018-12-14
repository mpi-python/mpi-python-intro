# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event
import storypresentation, questionnaires

#import random module, to pick textcolor value at random
import random

#import csv to be able to write output
import csv

#create integer value for backgroundcolor and textcolor (RGB, in python this has to be between -1 and 1)
bgcol = random.uniform(-1.0, 1.0)
textcol = random.uniform(-1.0,1.0)

# open a window of 800 by 600 pixels in the earlier defined background color
win = visual.Window((800, 600), color=[1,1,1],colorSpace = 'rgb')

core.wait(1)  # wait for 1 second on a blank window

# prepare a text stimulus in the earlier defined color, ask for participant number, end with "enter"
text = visual.TextStim(win, text='Wat is het proefpersoonnummer', color=[-1,-1,-1], colorSpace = 'rgb')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
event.waitKeys(clearEvents = True, keyList=['return'])

ppn = event.getKeys()
ppn = ''.join(ppn)

#open outputfile, story values for background color and textcolor
with open(f'{ppn}_colorvalues.csv', 'w') as colvalfile:
    colvalfile.write(f'backgroundcolor = [{bgcol},{bgcol},{bgcol}]\ntextcolor = [{textcol},{textcol},{textcol}]')
    
#create outputfile for readingtimes
with open(f'{ppn}_readingtime.tsv', 'w') as readingfile:
    writer = csv.writer(readingfile, delimiter = '\t')
    writer.writerow(['Page','Time'])
    
#create outputfile for questionnaire answers
with open(f'{ppn}_questionnaire.tsv', 'w') as questfile:
    writer = csv.writer(questfile, delimiter = '\t')
    writer.writerow(['Question','Answer'])

storypresentation.storypres(bgcol,textcol,ppn,win,text)
questionnaires.questions(ppn,win,text)
 

win.close()