#This is the code for the switch experiment 

#First import the necessary libraries 
#Import sounddevice as given in the HINTS file
import sounddevice as sd
import soundfile as sf
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import core, visual, event, gui, data, clock, logging
from psychopy.tools.filetools import fromFile, toFile
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy, random #for handling various numerical/mathematical functions
import os 
import sys #to get file system encoding

#Ensure that relative paths start from same directory as script
_thisDir = os.getcwd()

#Information on the experiment session
expName = 'Switch_experiment'
expInfo = {'Participant': '', 'Gender':'', 'Age': ''}
dlg = gui.DlgFromDict(dictionary = expInfo, title = expName)
if dlg.OK == False:
    core.quit() #Participant pressed cancel
expInfo['date'] = data.getDateStr() #add a simple timestamp
expInfo['expName'] = expName

#Data file name stem = absolute path + name; later add .csv
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])

#Save log file
logFile = logging.LogFile(filename + '.log', level = logging.EXP)
logging.console.setLevel(logging.WARNING) #this outputs to the screen, not a file

#You can implement and 'escape' to quit the experiment
endExpNow = False 

#Start code - component code to be run before the window creation
wavDirName = filename + '.wav' #save the .wav file
if not os.path.isdir(wavDirName):
    os.makedirs(wavDirName) 

#Setting up the microphone
sd.default.samplerate = 48000 #record at 48000 samples per second
sd.default.channels = 1 #record in mono

#Create window and stimuli
win = visual.Window([1280, 720], color = 'white', monitor = 'testMonitor', units = 'cm') #Open a window with a white background
text = visual.TextStim(win, None, color='black', font = 'arial') #Prepare a text stimulus
image = visual.ImageStim(win, None) 
LeftIm = visual.ImageStim(win, None) #Create the left images
LeftIm.setPos((-8,0)) #Define the position on the screen
RightIm = visual.ImageStim(win, None) #Create the right images 
RightIm.setPos((8,0)) #Define the position on the screen

#Clocks to keep track of time
globalClock = core.Clock()
trialClock = core.Clock()

#The needed functions
#Function for instruction test
def instr(win, myText):
    text.setText(myText)
    text.draw()  # draw to back buffer again
    win.flip()
    return

#Function to present the instruction text and to continue 
def presentInstr(win, myText):
    event.clearEvents()
    while len(event.getKeys())==0:
        instr(win, myText)
    return

#Function for generating the trials
def trial(win, pict, lang):
    if lang == 'EN': 
        LeftIm.setImage(pict)
        LeftIm.draw()
    else:
        #i.e., the Dutch trials 
        RightIm.setImage(pict)
        RightIm.draw() 
        
    win.flip()
    sd.rec(4 * sd.default.samplerate) #record for four seconds
    sd.wait() #finish recording before moving on
    return

##GET PARTICIPANT INFO##
#ppInfo()

###INSTRUCTIONS###
presentInstr(win, 'Welcome to this experiment.\n\nPress any key to continue.')
presentInstr(win, 'You will get to see pictures. \n\nYour task is to name the pictures as quickly as possible.')
presentInstr(win, 'However, there is a catch.')
presentInstr(win, 'If you see a picture on the LEFT side of the screen, name the picture in English.')
presentInstr(win, 'If you see a picture on the RIGHT side of the screen, name the picture in Dutch.')
presentInstr(win, 'Ready? \n\nPress a key to start!')

###EXPERIMENT###
#This can probably be done in a better way
trial(win, '1.png', 'EN')
trial(win, '2.png', 'EN')
trial(win, '3.png','EN')
trial(win, '4.png', 'NL')
trial(win, '5.png', 'NL')
trial(win, '6.png','EN')
trial(win, '7.png', 'NL')

#Cleanup
win.close()
core.quit()


