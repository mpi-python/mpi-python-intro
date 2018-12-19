## Data collection

import os
import sys
import glob
import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.gui
import psychopy.core
import random


#Setup
base_directory = 'C:\\Users\\migbor\\mpi-python-intro\\Session6'
stimuli_directory = (base_directory + '\\stimuli')
training_results_directory = (base_directory + '\\results\\training')
testing_results_directory = (base_directory + '\\results\\testing')
fonts_directory = (base_directory + '\\fonts')

os.chdir(fonts_directory)
fonts = os.listdir()
n_fonts = len(fonts)

gui = psychopy.gui.Dlg()

gui.addField("Subject ID:")
gui.addField("Group:")
gui.addField("Number of trials:")

gui.show()

subj_id = gui.data[0]
group = gui.data[1]
n_trials = int(gui.data[2])


data_path_training = subj_id + "_training_group_" + group + ".tsv"

if os.path.exists(data_path_training):
    sys.exit("Data path " + data_path_training + " already exists!")

exp_data = []

screen_size = [900,900]
text_color = 'White'

#Training

n_filler = 5
pre_duration_s = 4
blank_duration_s = 0.5
stim_duration_s = 1


#Fetch list of files, shuffle it, load a number sufficient for trials,
#duplicate enough for fillers
if group == "1":
    stim_prefix = "natural_*.png"
elif group == "2":
    stim_prefix = "non-natural_*.png"
else:
    sys.exit("Unknown group number")
    
os.chdir(stimuli_directory)
stim_files = glob.glob(stim_prefix)
np.random.shuffle(stim_files)
total_files = stim_files[0:(n_trials)]
repeats = np.random.choice(n_trials,n_filler,replace=False)
trial_files = []

for files in range(len(total_files)):
    if (list(enumerate(total_files)))[files][0] in repeats:
        trial_files.append((list(enumerate(total_files)))[files][1])
        trial_files.append((list(enumerate(total_files)))[files][1])
    else:
        trial_files.append((list(enumerate(total_files)))[files][1])

print(trial_files)
    
win = psychopy.visual.Window(
    size = screen_size,
    units = "pix",
    fullscr = False
)

stim = psychopy.visual.ImageStim(
    win = win
)

cross = psychopy.visual.TextStim(
    win = win,
    text = "+",
    color = "White",
    pos =(0,0),
    height = 80
)

instructions = psychopy.visual.TextStim(
    win=win,
    wrapWidth=650,
)

instructions.text = """
This experiment consists of two tasks. In task 1 you will see a series of images displayed in the center of the screen, and you need to push a button (P) whenever an image is the same as the one which preceded it.\n
Press any key to begin, and then fixate on the cross.
"""

instructions.draw()
win.flip()

psychopy.event.waitKeys()

clock = psychopy.core.Clock()

trial_count = -1

clock.reset()

while clock.getTime() < pre_duration_s:
        cross.draw()
        win.flip()

for trials in range(len(trial_files)):
    trial_onset = clock.getTime()
    trial_count = trial_count + 1
    while clock.getTime() < (trial_onset + blank_duration_s):
        win.flip()
    while clock.getTime() < (trial_onset + blank_duration_s + stim_duration_s):
        trial_stim = trial_files[trials]
        stim.setImage(trial_stim)
        stim.draw()
        win.flip()
    rt = clock.getTime()
    key_press = 0
    keys = psychopy.event.getKeys(timeStamped = clock)
    
    
    for key in keys:
        if key[0] == "q":
            key_press = 0
        elif key[0] == "p":
            key_press = 1
        else:
            key_press = 2
        rt = key[1]
        
    trial_stim = int(trial_stim[-7:-4])
    trial_data = [trial_count,trial_onset,trial_stim,key_press,rt]
    exp_data.append(trial_data)

#Columns are: Trial Number, Time of Trial, Image ID, Key Pressed (q = 0, p = 1), RT since start of task
os.chdir(training_results_directory)
np.savetxt(data_path_training, exp_data,  delimiter="\t")

training_done = 1

#Testing

data_path_testing = subj_id + "_testing_group_" + group + ".tsv"

n_font_sizes = 3
pre_duration_s = 4
blank_duration_s = 0.5

exp_data = []

font_size = [50,60,70]
font_name = ['SentyWen', 'FZJingLeiS-R-GB','Microsoft JhengHei','Source Han Serif SC Medium']
font_location = {font_name[0]: (fonts_directory + r'\SentyWEN2017_0.ttf'),
                 font_name[1]: (fonts_directory + r'\FZJingLei.fon'),
                 font_name[2]: (fonts_directory + r'\msjh.ttc'),
                 font_name[3]: (fonts_directory + r'\SourceHanSerifSC-Medium.otf')}
symbol_positions = ((0,(screen_size[1]*0.4)), #Top
                    ((screen_size[0]*0.2),(screen_size[1]*0.2)),
                    ((screen_size[0]*0.4),0), #Right
                    ((screen_size[0]*0.2),(screen_size[1]*-0.2)),
                    (0,(screen_size[1]*-0.4)), #Bottom
                    ((screen_size[0]*-0.2),(screen_size[1]*-0.2)),
                    ((screen_size[0]*-0.4),0), #Left
                    ((screen_size[0]*-0.2),(screen_size[1]*0.2)))


os.chdir(stimuli_directory)

with open(r'C:\\Users\\migbor\\mpi-python-intro\\Session6\\stimuli\\characters.txt',encoding="utf8") as stimuli_file:
    chinese_text = stimuli_file.read()
    chinese_lines = chinese_text.split('\n')
    del chinese_lines[0]

np.random.shuffle(chinese_lines)
stim_list_1 = chinese_lines[0:(int(n_trials))]
stim_list_2 = chinese_lines[(int(n_trials)):((int(n_trials))+(int(n_trials)))]
print(stim_list_1)
print(stim_list_2)
condition_list = [0] * (int(n_trials/2)) + [1] * (int(n_trials/2))
np.random.shuffle(condition_list)

#Setup text in drawing window
#Win - what window object to display this in
#Text - textstim render text to display
#Color - Set render colour ([1,1,1] is White, opposite sign is Black, default is "psychophysics gray", strings also usable)
#fontFiles - location of font .ttf file used
#font - Name of font to use
#height - size in 'units' of text to display, with width set by font
text = psychopy.visual.TextStim(
    win = win,
    color = "White",
) 

instructions = psychopy.visual.TextStim(
    win=win,
    wrapWidth=650,
)

instructions.text = """
You've completed task 1!\n
Now, in task 2 you will see pairs of Chinese characters displayed in one of eight possible positions on the screen, each rendered in different font types and sizes.\n
You need to indicate, as quickly as you can, whether the two characters are the same (by pressing P), or if they're different (by pressing Q), regardless of font type/size differences.\n
Press any key to display the positions on the screen where characters may appear, then press
any key again to begin.
"""

instructions.draw()
win.flip()

psychopy.event.waitKeys()

clock = psychopy.core.Clock()

trial_count = -1

clock.reset()

for position in range(len(symbol_positions)):
    text.height = 60
    text.text = "*"
    text.pos = symbol_positions[position]
    text.draw()

win.flip()
psychopy.event.waitKeys()

for trials in range(len(stim_list_1)):
    trial_onset = clock.getTime()
    trial_count = trial_count + 1
    font_type_array = np.random.choice(n_fonts,2,replace=False)
    font_size_array = np.random.choice(n_font_sizes,2,replace=False)
    symbol_position_array = np.random.choice(8,2,replace=False)
    while clock.getTime() < (trial_onset + blank_duration_s):
        win.flip()
    
    # Build character 1    
    text.font = font_name[font_type_array[0]]
    text.fontFiles = [font_location[font_name[font_type_array[0]]]]
    text.height = font_size[font_size_array[0]]
    text.pos = symbol_positions[symbol_position_array[0]]
    text.text = stim_list_1[trials]
    text.draw()
    
    # Build character 2   
    text.font = font_name[font_type_array[1]]
    text.fontFiles = [font_location[font_name[font_type_array[1]]]]
    text.height = font_size[font_size_array[1]]
    text.pos = symbol_positions[symbol_position_array[1]]
    if condition_list[trials] == 0:
        text.text = stim_list_1[trials]
    elif condition_list[trials] == 1:
        text.text = stim_list_2[trials]
    text.draw()
    win.flip()
    
    keys = psychopy.event.waitKeys(keyList=['q','p',],timeStamped = clock)
    print(keys)
    
    for key in keys:
        if key[0] == "q":
            key_press = 0
        elif key[0] == "p":
            key_press = 1
        else:
            key_press = 2
        rt = key[1]
    
    #Columns are: Trial Number, Time of Trial, Condition (Same = 1, Diff = 0), Key Pressed (q = 0, p = 1), RT since start of task
    trial_data = [trial_count,trial_onset,condition_list[trials],key_press,rt]
    exp_data.append(trial_data)

os.chdir(testing_results_directory)
np.savetxt(data_path_testing, exp_data,  delimiter="\t")

    
instructions.text = """
Tasks complete!\n
Thank you for participating, press any key to exit.
"""

instructions.draw()
win.flip()
psychopy.event.waitKeys()
    
win.close()