# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event

#import csv to be able to write output
import csv

def questions(ppn,win,text):
    #make a list of the number of questions you want to present
    questList = [questnum for questnum in range(5)]

    #define what the questions are
    questions = ["When I finished the story I was surprised to see that time had gone by so fast",
                 "When I was reading the story I was focused on what happened in the story",
                 "I felt absorbed in the story",
                 "The story gripped me in such a way that I could close myself off for things that were happening around me",
                 "I was reading in such a concentrated matter that I had forgotten the world around me"]
    '''
    # open a window of 800 by 600 pixels
    win = visual.Window((800, 600), color='white')

    core.wait(1)  # wait for 1 second on a blank window

    # prepare a text stimulus for question presentation, ask for participant number, end with "enter"
    text = visual.TextStim(win, text='Wat is het proefpersoonnummer', color='black')
    text.draw()  # draw the stimulus to the back buffer
    win.flip()  # flip the back buffer with our stimulus to the front
    event.waitKeys(clearEvents = True, keyList=['return'])

    ppn = event.getKeys()
    ppn = ''.join(ppn) 

    #create outputfile for questionnaire answers
    with open(f'{ppn}_questionnaire.tsv', 'w') as questfile:
        writer = csv.writer(questfile, delimiter = '\t')
        writer.writerow(['Question','Answer'])
    '''

    #change color of background to white, change color of text to black
    win.color = [1, 1, 1]
    text.color = [-1, -1, -1]
    win.flip()
    
    #display introduction to questionnaire until space bar press
    text.setText('This is the start of the questionnaire. Indicate whether you agree with these statements. Press a key from 1 to 7 to answer, 1 = totally disagree, 7 = totally agree. Press the space bar to start the questionnaire.')
    text.draw()
    win.flip()
    event.waitKeys(clearEvents = True, keyList=['space'])

    #present all questions and collect answers in output file
    for quest in questList:
        text.setText(questions[quest])
        text.draw()
        win.flip()
        while True:
            response = event.waitKeys()
            response = ''.join(response)
            if response in ['1','2','3','4','5','6','7']:
                answer = response
                break
            else:
                answer = 'NA'
                break
        with open(f'{ppn}_questionnaire.tsv', 'a') as questfile:
            writer = csv.writer(questfile, delimiter='\t')
            writer.writerow([quest+1,f'{answer}'])

    text.setText("Thank you for answering the questions. This is the end of the experiment. Thank you for your participation!")
    text.draw()
    win.flip()
    core.wait(2)

#win.close()
