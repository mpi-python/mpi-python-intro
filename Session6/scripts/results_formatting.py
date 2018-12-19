## Results formatting

import os
import sys
import glob
import numpy as np
import psychopy.visual
import psychopy.event
import psychopy.gui
import psychopy.core
import random

import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score

## Training Analysis

os.chdir(training_results_directory)
files = os.listdir()
n_subjects = len(files)


#Columns are: Trial Number, Time of Trial, Image ID, Key Pressed (q = 0, p = 1), RT since start of task

training_results = pd.DataFrame()

for subject in range(n_subjects):
    
    #Get SubjID and Group
    subj_id = files[subject].partition("_")[0]
    group = files[subject][-11:].partition("_")[2]
    group = group.partition(".")[0]
    
    #Load subject dataframe
    subj_results = pd.read_csv(files[subject],sep = '\t',
                          names = ["TrialNumber", "TrialTimestamp", "ImageID", "KeyPressed","RT"])

    #Add column for repeat trials
    ImageID_vector = subj_results['ImageID'].values
    RepeatTrial_vector = [0]
    for trials in range((len(ImageID_vector))-1):
        if ImageID_vector[trials + 1] == ImageID_vector[trials]:
            RepeatTrial_vector.append(1)
        else:
            RepeatTrial_vector.append(0)
    subj_results = subj_results.assign(RepeatTrial = RepeatTrial_vector)

    #Add columns with SubjectID and Group
    
    SubjID_vector = []
    Group_vector = []
    for trials in range((len(ImageID_vector))):
        SubjID_vector.append(int(subj_id))
        Group_vector.append(int(group))
    subj_results = subj_results.assign(SubjID = SubjID_vector)
    subj_results = subj_results.assign(Group = Group_vector)
    
    #Add column with true per-trial RT and accuracy column
    TrialTime_vector = subj_results['TrialTimestamp'].values
    RT_vector = subj_results.query('RepeatTrial == 1')['RT']
    KeyPress_vector = subj_results['KeyPressed'].values
    TrialRT_vector = []
    Accuracy_vector = []
    for trials in range((len(ImageID_vector))):
        if RepeatTrial_vector[trials] == 1:
            trial_time = TrialTime_vector[trials]
            rt_time = RT_vector[trials]
            TrialRT_vector.append(rt_time-trial_time)
            if KeyPress_vector[trials] == 1:
                Accuracy_vector.append(1)
            else:
                Accuracy_vector.append(0)
        else:
            TrialRT_vector.append(0) 
            Accuracy_vector.append(0)
    subj_results = subj_results.assign(TrialRT = TrialRT_vector)
    subj_results = subj_results.assign(Accuracy = Accuracy_vector)
    training_results = training_results.append(subj_results)
    del subj_results
    
training_results.reset_index(drop=True)
 
    
## Testing Analysis

os.chdir(testing_results_directory)
files = os.listdir()
n_subjects = len(files)


#Columns are: Trial Number, Time of Trial, Condition (Same = 1, Diff = 0), Key Pressed (q = 0, p = 1), RT since start of task

testing_results = pd.DataFrame()

for subject in range(n_subjects):
    
    #Get SubjID and Group
    subj_id = files[subject].partition("_")[0]
    group = files[subject][-11:].partition("_")[2]
    group = group.partition(".")[0]
    
    #Load subject dataframe
    subj_results = pd.read_csv(files[subject],sep = '\t',
                          names = ["TrialNumber", "TrialTimestamp", "Condition", "KeyPressed","RT"])

    #Add columns with SubjectID and Group
    Condition_vector = subj_results['Condition'].values
    SubjID_vector = []
    Group_vector = []
    for trials in range((len(Condition_vector))):
        SubjID_vector.append(int(subj_id))
        Group_vector.append(int(group))
    subj_results = subj_results.assign(SubjID = SubjID_vector)
    subj_results = subj_results.assign(Group = Group_vector)
    
    #Add column with true per-trial RT and accuracy column
    TrialTime_vector = subj_results['TrialTimestamp'].values
    RT_vector = subj_results['RT'].values
    KeyPress_vector = subj_results['KeyPressed'].values
    TrialRT_vector = []
    Accuracy_vector = []
    for trials in range((len(Condition_vector))):
            trial_time = TrialTime_vector[trials]
            rt_time = RT_vector[trials]
            if Condition_vector[trials] == KeyPress_vector[trials]:
                TrialRT_vector.append(rt_time-trial_time)
                Accuracy_vector.append(1)
            else:
                TrialRT_vector.append(rt_time-trial_time)
                Accuracy_vector.append(0)
    subj_results = subj_results.assign(TrialRT = TrialRT_vector)
    subj_results = subj_results.assign(Accuracy = Accuracy_vector)
    
    testing_results = testing_results.append(subj_results)
    del subj_results
    
testing_results.head()