# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event

#import random module, to pick textcolor value at random
import random

#import csv to be able to write output
import csv

#make a list of the number of pages you want to present
pageList = [pagenum for pagenum in range(4)]

#define what the text on each page has to be
textperpage = ["Er was eens",
               "Een meisje",
              "en zij at graag",
              "een ijsje"]

#create integer value for backgroundcolor and textcolor (RGB, in python this has to be between -1 and 1)
bgcol = random.uniform(-1.0, 1.0)
textcol = random.uniform(-1.0,1.0)

# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color=[bgcol,bgcol,bgcol], colorSpace = 'rgb')

core.wait(1)  # wait for 1 second on a blank window

# prepare a text stimulus in the earlier defined color, ask for participant number, end with "enter"
text = visual.TextStim(win, text='Wat is het proefpersoonnummer', color=[textcol,textcol,textcol], colorSpace = 'rgb')
text.draw()  # draw the stimulus to the back buffer
win.flip()  # flip the back buffer with our stimulus to the front
event.waitKeys(clearEvents = True, keyList=['return'])

ppn = event.getKeys()

#open outputfile, story values for background color and textcolor
with open(f'{ppn}_colorvalues.csv', 'w') as colvalfile:
    colvalfile.write(f'backgroundcolor = [{bgcol},{bgcol},{bgcol}]\ntextcolor = [{textcol},{textcol},{textcol}]')
    
#create outputfile for readingtimes
with open(f'{ppn}_readingtime.tsv', 'w') as readingfile:
    writer = csv.writer(readingfile, delimiter = '\t')
    writer.writerow(['Page','Time'])

#display welcome text until space bar press
text.setText('Klik op de spatiebalk om te beginnen. Om naar een volgende pagina te gaan druk je ook steeds op de spatiebalk')
text.draw()
win.flip()
event.waitKeys(clearEvents = True, keyList=['space'])

# start the clock
clock = core.Clock()

#present all pages until spacebar press
for page in pageList:
    pagestart = clock.getTime()
    text.setText(textperpage[page])
    text.draw()
    win.flip()
    event.waitKeys(clearEvents = True, keyList=['space'])
    pageend = clock.getTime()
    with open(f'{ppn}_readingtime.tsv', 'a') as readingfile:
        writer = csv.writer(readingfile, delimiter='\t')
        writer.writerow([page+1,pageend-pagestart])

text.setText("Dat was het einde van het verhaal. Er volgt nu een vragenlijst.")
text.draw()
win.flip()
core.wait(2)

win.close()
