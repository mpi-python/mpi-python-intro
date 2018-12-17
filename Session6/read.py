#First import the necessary libraries 
#Import sounddevice as given in the HINTS file
import sounddevice as sd
import soundfile as sf
from psychopy import prefs
prefs.general['audioLib'] = ['pygame']
from psychopy import core, visual, event, gui, data, clock, logging
from psychopy.tools.filetools import fromFile, toFile
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
import os 
import sys
import seaborn as sns

path = './recordings' #Define the right directory
os.chdir(path)

rec = [] #Create an empty list for recordings
listRec = os.listdir('.') 

#Create a list of all the .wav files in the directory
for file in listRec:
    if file.endswith(".wav"):
         rec.append(file)

for files in listRec:
    recordings, samplerate = sf.read(files) #Read all .wav files 
    energy = np.square(recordings) #create a variable "energy" of the squared recordings-array
    Emax = np.max(energy)
    energyNorm = (energy/Emax) #Normalize these values
    index = [index for index, value in enumerate(energyNorm) if value > 0.2] #Ok so this is quite unprecise and there are multiple solutions to this problem (e.g., comparing multiple indices, getting rid of noise beforehand) , but for this exercise I will keep it like this. 
    RT = index[0]/samplerate #This is the reaction time
    print(RT) #Sanity check
    


 


    