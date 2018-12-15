#make a function to save data after each trial
# function from https://discourse.psychopy.org/t/is-there-any-way-to-save-exp-data-after-every-trial/3173/2
def SaveData(trial,prime,target,RT,accuracy):  
    # open file
    import os, csv
    os.chdir("C:/Users/limrav/mpi-python-intro/Session6")
    fileName = 'mylogfile.csv'  
    with open(fileName, 'ab') as saveFile: #'a' = append; 'w' = writing; 'b' = in binary mode
        fileWriter = csv.writer(saveFile, delimiter='\t') #generate fileWriter object
        if os.stat(fileName).st_size == 0: #if file is empty, insert header
            fileWriter.writerow('trial', 'prime', 'target', 'RT', 'accuracy')        
        #write trial
        fileWriter.writerow(trial, prime, target, RT, accuracy)