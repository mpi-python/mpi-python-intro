# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event

#import random module, to pick textcolor value at random
import random

#import csv to be able to write output
import csv

def storypres(bgcol,textcol,ppn,win,text):
    #make a list of the number of pages you want to present
    pageList = [pagenum for pagenum in range(4)]

    #define what the text on each page has to be
    textperpage = ["For the fourth time in as many years, they were confronted with the problem of what birthday present to take to a young man who was incurably deranged in his mind. Desires he had none. Man-made objects were to him either hives of evil, vibrant with a malignant activity that he alone could perceive, or gross comforts for which no use could be found in his abstract world. After eliminating a number of articles that might offend him or frighten him (anything in the gadget line, for instance, was taboo), his parents chose a dainty and innocent trifle—a basket with ten different fruit jellies in ten little jars.",
                   "At the time of his birth, they had already been married for a long time; a score of years had elapsed, and now they were quite old. Her drab gray hair was pinned up carelessly. She wore cheap black dresses. Unlike other women of her age (such as Mrs. Sol, their next-door neighbor, whose face was all pink and mauve with paint and whose hat was a cluster of brookside flowers), she presented a naked white countenance to the faultfinding light of spring. Her husband, who in the old country had been a fairly successful businessman, was now, in New York, wholly dependent on his brother Isaac, a real American of almost forty years’ standing. They seldom saw Isaac and had nicknamed him the Prince.",
                  "That Friday, their son’s birthday, everything went wrong. The subway train lost its life current between two stations and for a quarter of an hour they could hear nothing but the dutiful beating of their hearts and the rustling of newspapers. The bus they had to take next was late and kept them waiting a long time on a street corner, and when it did come, it was crammed with garrulous high-school children. It began to rain as they walked up the brown path leading to the sanitarium. There they waited again, and instead of their boy, shuffling into the room, as he usually did (his poor face sullen, confused, ill-shaven, and blotched with acne), a nurse they knew and did not care for appeared at last and brightly explained that he had again attempted to take his life. He was all right, she said, but a visit from his parents might disturb him. The place was so miserably understaffed, and things got mislaid or mixed up so easily, that they decided not to leave their present in the office but to bring it to him next time they came.",
                  "Outside the building, she waited for her husband to open his umbrella and then took his arm. He kept clearing his throat, as he always did when he was upset. They reached the bus-stop shelter on the other side of the street and he closed his umbrella. A few feet away, under a swaying and dripping tree, a tiny unfledged bird was helplessly twitching in a puddle."]
    
    '''
    #create integer value for backgroundcolor and textcolor (RGB, in python this has to be between -1 and 1)
    bgcol = random.uniform(-1.0, 1.0)
    textcol = random.uniform(-1.0,1.0)

    # open a window of 800 by 600 pixels in the earlier defined background color
    win = visual.Window((800, 600), color=[bgcol,bgcol,bgcol], colorSpace = 'rgb')

    core.wait(1)  # wait for 1 second on a blank window

    # prepare a text stimulus in the earlier defined color, ask for participant number, end with "enter"
    text = visual.TextStim(win, text='Wat is het proefpersoonnummer', color=[textcol,textcol,textcol], colorSpace = 'rgb')
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
    '''


    #change color of background to random color, change color of text to random color
    win.color = [bgcol, bgcol, bgcol]
    text.color = [textcol, textcol, textcol]
    win.flip()
    
    #display welcome text until space bar press
    text.setText('You are going to read a story. Press the space bar to start. To proceed to the next page in the story, you also press the space bar.')
    text.draw()
    win.flip()
    event.waitKeys(clearEvents = True, keyList=['space'])

    # start the clock to record reading time per page
    clock = core.Clock()

    #present all pages until spacebar press
    for page in pageList:
        pagestart = clock.getTime() #clock time at start of page presentation
        text.setText(textperpage[page])
        text.draw()
        win.flip()
        event.waitKeys(clearEvents = True, keyList=['space'])
        pageend = clock.getTime() #clock time at end of page presentation
        with open(f'{ppn}_readingtime.tsv', 'a') as readingfile:
            writer = csv.writer(readingfile, delimiter='\t')
            writer.writerow([page+1,pageend-pagestart])

    text.setText("This is the end of the story. You will now fill in a questionnaire.")
    text.draw()
    win.flip()
    core.wait(2)

#win.close()
