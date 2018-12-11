#This is the code for the switch experiment 

#First import the necessary libraries 
from psychopy import core, visual, event, gui, data, voicekey
from psychopy.tools.filetools import fromFile, toFile
from PIL import Image
import sounddevice as sd
import numpy, random #for handling various numerical/mathematical functions
import os

#Set the directory to the current directory
directory = os.getcwd()


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
    core.wait(2) #core.wait is until I figure the voicekey out
    return

#Presenting stimuli, using a window, a picture, and defining the language
def presentStim(win, pict, lang):
    trialpic = trial(win, pict, lang) #trial-generating-function
    vk = voicekey.OnsetVoiceKey(sec=2.0, file_out='try.wav', more_processing = False, autosave = True) #The built-in voice-key
    timer = core.getTime()
    starttime = time.time()
    vk_RT = vk.event_onset
    vk.stop()
    vkstopped = time.time()
    return


###INSTRUCTIONS###
presentInstr(win, 'Welcome to this experiment.\n\nPress any key to continue.')
presentInstr(win, 'You will get to see pictures. \n\nYour task is to name the pictures as quickly as possible.')
presentInstr(win, 'However, there is a catch.')
presentInstr(win, 'If you see a picture on the LEFT side of the screen, name the picture in English.')
presentInstr(win, 'If you see a picture on the RIGHT side of the screen, name the picture in Dutch.')
presentInstr(win, 'Ready? \n\nPress a key to start!')

###EXPERIMENT###
#I should be able to randomize this:
'''
images = []
for file in os.listdir(directory):
    if file.endswith('.png'):
        images.append(file)

              
#randomize list
random.shuffle(images)

for i in range(0, (len(images)):
'''
presentStim(win, '1.png', 'EN')
trial(win, '2.png', 'EN')
trial(win, '3.png','EN')
trial(win, '4.png', 'NL')
trial(win, '5.png', 'NL')
trial(win, '6.png','EN')
trial(win, '7.png', 'NL')

#Cleanup
win.close()
core.quit()


