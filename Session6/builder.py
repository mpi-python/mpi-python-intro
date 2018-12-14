#This is the code for the switch experiment 

from psychopy import core, visual, event 
import os

directory = os.getcwd()

win = visual.Window([1280, 720], color = 'white', fullscr = True) #Open a window with a white background
text = visual.TextStim(win, None, color='Black', font = 'arial') #Prepare a text stimulus
image = visual.ImageStim(win, None) 
LeftIm = visual.ImageStim(win, None) #Create the left images
LeftIm.setPos((-8,0)) #Define the position on the screen
RightIm = visual.ImageStim(win, None) #Create the right images
RightIm.setPos((8,0)) #Define the position on the screen

endExpNow = False 

#The needed functions
def instr(win, myText):
    text.setText(myText)
    text.draw()  # draw to back buffer again
    win.flip()
    core.wait()

      
#Instruction component
instrClock = core.Clock()
instr1 = instr(win, 'Welcome to this experiment.\n\nPress space to continue.')
instr2 = instr(win, 'You will get to see pictures. \n\nYour task is to name the pictures as quickly as possible.')
instr3 = instr(win, 'However, there is a catch.')
instr4 = instr(win, 'If you see a picture on the LEFT side of the screen, name the picture in English.')
instr5 = instr(win, 'If you see a picture on the RIGHT side of the screen, name the picture in Dutch.')
instr6 = instr(win, 'Ready? \n\nPress space to start!')

#Create some timers 
globalClock = core.Clock() #To track the time since experiment started
routineTimer = core.CountdownTimer() #To track time remaining of each routine

#Prepare to start routine Instruction
t = 0
instrClock.reset() #Reset the clock
frameN = -1
continueRoutine = True
key_cont = event.BuilderKeyResponse()
instrComponents = [key_cont, instr%]
for component in instrComponents:
    if has attr(component, 'status'):
        component.status = NOT_STARTED
        
#Start Instruction
while continueRoutine:
    t = instrClockgetTime()
    frameN = frameN + 1 #number of completed frames
    
    #keys
    if t >= 0.0 and key_cont_status == NOT_STARTED:
        #keep track of start time/frame for later
        key_cont.tStart = 1
        key_cont.frameNStart = FrameN
        key_cont.status = STARTED
        even.clearEvents(eventType = 'keyboard')
    if key_cont.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        if 'escape' in theseKeys:
            endExpNow = True
  
win.close()  # close the window
core.quit()
