# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual, event

#import csv to be able to write output
import csv

def questions(ppn,win,text):
    #make a list of the number of questions you want to present
    questList = [questnum for questnum in range(4)]

    #define what the questions are
    questions = ["was het leuk?",
                 "was het vet?",
                 "was het cool?",
                 "was het awesome?"]
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
    text.setText('Hier komen de vragen. Druk op een toets van 1 tot 7 om antwoord te geven. Druk om de spatiebalk om te beginnen.')
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

    text.setText("Bedankt voor het invullen van de vragenlijst. Het experiment is nu klaar.")
    text.draw()
    win.flip()
    core.wait(2)

#win.close()
