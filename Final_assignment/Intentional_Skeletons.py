
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


#=SUBROUTINES=====================
def present_stim(module, t):
    module.onset = t
    module.setAutoDraw(True)
    return module

def Check_for_quit(event):
    if event.getKeys(keyList=["escape"]):
        core.quit()

def reset_components(TrialComponents):
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    print('reset done')
    
#load the video into a moviestim object
def load_movie_stim(video_name):
    movie = visual.MovieStim3(win=win, name='movie',
        noAudio = True, size = (120,90),
        filename= u'stimuli/%s.avi'%video_name,
        ori=0, pos=[0, 0], opacity=1,
        depth=-2.0,
        )
    return movie
#=INITIALIZE============================
#set up some initial variables

#name the experiment
expName = 'Intentional_Skeletons'

#bring up the gui that gets your participant number, than pass it to the output filename
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

expInfo['date'] = data.getDateStr()  # add a simple timestamp


filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

endExpNow = False  # flag for 'escape' or other condition => quit the exp

#how many trials?
numTrials = 120

#Experiment handler to help with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#load in the stimulus video paths
with open('stimuli/social_skeletons_stims.txt') as f:
    stimpaths = f.read().splitlines()
random.shuffle(stimpaths)
#load the Primes: single words describing each action. index+1 corresponds to the second number in the video name.
with open('stimuli/prime_text.txt') as f:
        Prime_text = f.read().splitlines()


# Setup the Window
win = visual.Window(size=(1024, 768), fullscr=True, screen=0, allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
 
#we'll need this later
expInfo['frameRate']=win.getActualFrameRate()

#
#Now set up everything to actually run
trialClock = core.Clock()
globalClock = core.Clock()

#------BEGIN-----------
# Intro Text
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
    
#load_movie_stim('stimuli/2_3_skeleton.avi')

#Text stimulus
Response_text = visual.TextStim(win=win, ori=0, name='Response_text',
    text=u'           \n\nTeacher\t\t\t\tNeutral\t\t\t\tStudent\n  [1]\t\t\t\t\t\t\t[2]\t\t\t\t\t\t\t[3]',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-2.0)
    
#static period between trials
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

    
    
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
    
    #set jitter between 0.1 1.0s - this will be the time between Prime and movie
    Jitter = random.uniform(0.1,1.0)
    
    # Get the prime corresponding to the current video
    prime_current = Prime_text[int(B)]
    
    Prime.text=(prime_current)
    
    #movie.loadMovie=u'stimuli/%s.avi'%(stims[0]),
    movie = load_movie_stim(stims[0])
    
    trialClock.reset()  # reset the trial clock
    
    t = 0 #reset this every time
    
    key_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse

    #initialize the Components, which control the program flow
    TrialComponents = []
    TrialComponents.append(Prime)
    TrialComponents.append(movie)
    TrialComponents.append(Response_text)
    TrialComponents.append(key_resp)
    TrialComponents.append(ISI)
    reset_components(TrialComponents)

    continueRoutine = True #used to jeep the trial going until its done
#----------start
    
    while continueRoutine == True:
        t = trialClock.getTime()
        
        #if the Prime hasn't been shown yet, draw and show it
        if t > 0 and Prime.status == NOT_STARTED:
            #Prime.draw()#we cant use this method because the window has to be flipped at the end of the routine for the video
            Prime = present_stim(Prime,t)

            
        #after 1.5 seconds, stop showing the prime (give us a blank screen
        if Prime.status == STARTED and t > Prime.onset + Jitter:
            Prime.setAutoDraw(False)
            
        #check if we should play the movie; wait until 1s after prime has been shown
        if Prime.status == FINISHED and movie.status == NOT_STARTED and t > (1.5 + Prime.onset):            
            movie = present_stim(movie, t)
            
        #after playing the video, we ask for the response
        if movie.status == FINISHED and Response_text.status == NOT_STARTED:
            Response_text = present_stim(Response_text, t)
            event.clearEvents(eventType='keyboard') #make sure no previous button presses remain
            
        if Response_text.status == STARTED:
            theseKeys = event.getKeys(keyList=['1','escape','2','3'])
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp.keys = theseKeys[-1]  # just the last key pressed
                key_resp.rt = key_resp.clock.getTime()
                key_resp.status = FINISHED
                Response_text.setAutoDraw(False)
            elif t >= Response_text.onset + 3:
                Response_text.setAutoDraw(False)
                key_resp.keys = 'NA'
                key_resp.rt = 'NA'
                key_resp.status = FINISHED
        #ISI
        if Response_text.status == FINISHED and ISI.status == NOT_STARTED:
            win.flip()
            ISI.tStart = t
            ISI.start(0.5)
        elif ISI.status == STARTED and t >= ISI.tStart + 0.5:
            ISI.status = FINISHED
            
        Check_for_quit(event)    
         
        #check for ending
        continueRoutine = False 
        for thisComponent in TrialComponents:
            if thisComponent.status != FINISHED:
                continueRoutine = True #if any of them haven't finished, continue routine                
        # refresh the screen  
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #---------------Data Logging:
    
    thisExp.addData('Onset Prime', Prime.onset)
    thisExp.addData('Jitter', Jitter)
    thisExp.addData('Onset movie', movie.onset)
    thisExp.addData('Onset Response text', Response_text.onset)
    thisExp.addData('Response', key_resp.keys)
    if key_resp.rt != 'NA':
        thisExp.addData('Response RT', key_resp.rt-Response_text.onset)
    else: thisExp.addData('Response RT', 'NA')
    thisExp.addData('Movie: actor', A)
    thisExp.addData('Movie: item', B)
    thisExp.addData('CTX', stims[1])
   
  #----------------------- end of trial - move to next line in data output
    thisExp.nextEntry()
t = globalClock.getTime()   
present_stim(End_text,t)
win.flip()
core.wait(2.0)