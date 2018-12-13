
""""
Behavioral experiment designed to test categorization of kinematically modulated actions into 3 different intentional categories.

Uses 1,2,3 buttons as responses. Stick-light figures from Trujillo et al., 2018. Beh Res Meth are used for stimuli. Records response,
RT, and stimulus info

Version 1.0 - 10.12.2018

"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
import psychopy.core
from numpy import random
from numpy.random import shuffle
from psychopy.constants import *  # things like STARTED, FINISHED

import os  # handy system and path functions
import sys # to get file system encoding

#=INITIALIZE============================
#set up some initial variables

#name the experiment
expName = 'Intentional_Skeletons'

#bring up the gui that gets your participant number, than pass it to the output filename
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

expInfo['date'] = data.getDateStr()  # add a simple timestamp


filename = 'D:\\data\\fMRI_Social_Skeletons\\' + u'beh/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

endExpNow = False  # flag for 'escape' or other condition => quit the exp

#how many trials?
numTrials = 2


#load in the stimulus video paths
with open('D:\\data\\fMRI_Social_Skeletons\\stimuli\\social_skeletons_pilot_stimA.txt') as f:
    stimpaths = f.read().splitlines()
random.shuffle(stimpaths)
#load the Primes: single words describing each action. index+1 corresponds to the second number in the video name.
with open('D:\\data\\fMRI_Social_Skeletons\\stimuli\\prime_text.txt') as f:
        Prime_text = f.read().splitlines()


# Setup the Window
win = visual.Window(size=(1024, 768), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
   
#
#Now set up everything to actually run
trialClock = core.Clock()
globalClock = core.Clock()

#------BEGIN-----------
# Ending Text
Begin_text = visual.TextStim(win=win, ori=0, name='Begin_text',
    text=u'Ready?',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)


#------END-----------
# Ending Text
End_text = visual.TextStim(win=win, ori=0, name='End_text',
    text=u'The End!',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

#------TRIAL-----------

#This will inform the participant what the action will be. The word 'act' will be replaced
Prime = visual.TextStim(win=win, ori=0, name='Prime',
    text='act',   font='Arial',
    pos=[0,0], height=0.1,wrapWidth=None, 
    color='white', colorSpace='rgb',opacity=1,
    depth=-1.0)
    


movie = visual.MovieStim3(win=win, name='movie',
    noAudio = True,
    filename='C:\\Users\\James\\Documents\\MATLAB\\skeletons_whole\\2_3_skeleton.avi',
    ori=0, pos=[0, 0], opacity=1,
    depth=-2.0,
    )

#Text stimulus
Response_text = visual.TextStim(win=win, ori=0, name='Response_text',
    text=u'           \n\nTeacher\t\tNeutral\t\tStudent\n  [1]                               [0]',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
    
    
#=====WAIT FOR START================
#draw the 'Ready?' text
Begin_text.draw()
win.flip()
#wait for a button press
event.waitKeys(keyList=['1','2','3'])
#now the timer begins
globalClock.reset()

#================TRIAL======================
for Trial in range(1, numTrials):
#-----prepare
    
    #get the next stimulus path
    stimStr = stimpaths[Trial]
    #split the string by tab. [0] = video path, [1] = communicative context (0=NC, 1=C)
    stims = stimStr.split('\t')
    strstims = str(stims[0])
    #split the string so we have: A = actor num, B = action num, C = 'skeleton'
    A, B, C = strstims.split('_')
    
    #set jitter between 3.5 and 4.5s
    Jitter = random.uniform(3.5,4.5)
    
    # Get the prime corresponding to the current video
    prime_current = Prime_text[int(B)]
    
    
    Prime = visual.TextStim(win=win, ori=0, name='Prime',
        text=(prime_current),   font='Arial',
        pos=[0,0], height=0.1,wrapWidth=None,
        color='white', colorSpace='rgb',opacity=1,
        depth=-1.0)

    
    movie.filename=u'C:\\Users\\James\\Documents\\MATLAB\\skeletons_whole\\fMRI_pilot\\%s.avi'%(stims[0]),

    trialClock.reset()  # reset the trial clock
    
    key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse

    #initialize the Components, which control the program flow
    TrialComponents = []
    TrialComponents.append(Prime)
    TrialComponents.append(movie)
    TrialComponents.append(Response_text)
    TrialComponents.append(key_resp)
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    continueRoutine = True #used to jeep the trial going until its done
    
#----------start
    
    while continueRoutine == True:
        
        t = trialClock.getTime()
        #if the Prime hasn't been shown yet, draw and show it
        if t > 0 and Prime.status == NOT_STARTED:
            Prime.draw()
            win.flip()
            Prime.onset = t
            Prime.status = STARTED
            
        #after 1.5 seconds, stop showing the prime (give us a blank screen
        if Prime.status == STARTED and t > 1.5:
            win.flip
            Prime.status = FINISHED
            
        #check if we should play the movie; wait until 1s after prime has been shown
        if Prime.status == FINISHED and movie.status == NOT_STARTED and t > (2.5 + Prime.onset):            
            #Prime.setAutoDraw(False) 

            movie.onset = trialClock.getTime()
            movie.tStart = t  
            movie.setAutoDraw(True)
            win.flip()
            
            
        #check for ending
        continueRoutine = False 
        for thisComponent in TrialComponents:
            if thisComponent.status != FINISHED:
                continueRoutine = True #if any of them haven't finished, continue routine
        
        #make sure we can always stop with the Escp button
        if event.getKeys(keyList=["escape"]):
            core.quit()
            
        
        # refresh the screen  
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
        