import os    
from psychopy import visual, core, event
from PIL import Image

# open inputfile
with open('inputfile.txt', 'r') as inp_list:
    inp_list = inp_list.read()
    inp_lines = inp_list.split('\n')

    inp_columns = []

    for lines in range(len(inp_lines)):
        columns = inp_lines[lines].split('\t')
        inp_columns.append(columns)

# run experiment       
win = visual.Window([800,600], color = 'white')

answers = [[] for y in range(0,18)]

screen = visual.ImageStim(win)
response = [] 

phrase = visual.TextStim(win, text = 'Welkom bij deze zoektaak. \nJe leest zodadelijk een zin waarin een target wordt omschreven. Als je deze hebt gelezen, druk je op spatie. \nIn het volgende scherm ga je op zoek naar dit target. \nAls je het gevonden hebt, druk je op y. Als je het niet kunt vinden, druk je op n.\nProbeer zo snel mogelijk te reageren! \nDruk op spatie om verder te gaan.', color = 'black')
phrase.draw()
win.flip()
response = event.waitKeys(keyList = ['space'])
win.flip()

for trials in range(0,18):
    
    #present fixation cross
    fixcross = visual.TextStim(win, text = '+', color = 'black')
    fixcross.draw()
    win.flip()
    #core.wait(0.3)
    
    target = inp_columns[trials - 1][0]
    condition = inp_columns[trials - 1][0]
    condition = condition[-6:-4]
    
    phrase = visual.TextStim(win, text = f'Kun je de {target[:-7]} vinden op het volgende scherm?', color = 'black')
    phrase.draw()
    win.flip()
    response = event.waitKeys(keyList = ['space'])
    win.flip()
    
    screen.setImage(inp_columns[trials - 1][0])
    screen.draw()
    win.flip()
    time = core.Clock()
       
    while True:
        response = event.waitKeys(keyList = ['y','n'])
        response = ''.join(response)
        if response in ['y', 'n']:
               answer = response
        break
        
    RT = time.getTime()
    
    answers[trials].append(' ')
    
    if answer == 'y':
        answers[trials].append(answer)
        if answer == inp_columns[trials - 1][1]:
            answers[trials].append('correct')
            #answers[trials].append(inp_columns[trials - 1][2])  
        else:
            answers[trials].append('incorrect')
            #answers[trials].append(inp_columns[trials - 1][2])
    elif answer == 'n':
        answers[trials].append(answer)
        if answer == inp_columns[trials - 1][1]:
            answers[trials].append('correct')
            #answers[trials].append(inp_columns[trials - 1][2])
        else:
            answers[trials].append('incorrect')
            #answers[trials].append(inp_columns[trials - 1][2])
    else:
        answers[trials].append('NaN')
    
    
    answers[trials].append(condition)
    RT = RT*1000
    answers[trials].append(RT)
    answers[trials].append(' ')
    
    win.flip()

# write outputfile    
with open('answers.csv', 'w') as output:
    for item in answers:
        output.write("%s\n" % item )

win.close()