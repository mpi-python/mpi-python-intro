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
import fnmatch
import seaborn as sns

path = './recordings'
os.chdir(path)

rec = []
listRec = os.listdir('.')

pattern = '*.wav'
for file in listRec:
    #if file.endswith(".wav"):
    #    rec.append(file)
    if fnmatch.fnmatch(file, pattern):
        rec.append(file)

print(rec)

#for file 
'''
for i in 
recordings, samplerate = sf.read('1.wav')

#recordings = sf.read('1.wav')
#sns.lineplot(data = recordings)

energy = np.square(recordings)
Emin = 0
Emax = np.max(energy)
energyNorm = (energy/Emax)
# print(energyNorm)
# print(energy)

index = [index for index, value in enumerate(energyNorm) if value > 0.14]
#print(index[0]) ##where energy is larger than 0.0001

RT = index[0]/samplerate
print(RT)

# print(recordings)
# print(energy)

# index = np.argmin(energy == 0.001)
# print(index)
 
#Maybe: get rid of noise before calculating the threshold! 
'''

    