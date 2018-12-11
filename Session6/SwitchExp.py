#New attempt
    
from psychopy import core, visual, event 

#First, define functions

def cont():
    
def VK()
    
def instr(text):
    text.setText(text)
    text.draw()  # draw to back buffer again
    win.flip()
    core.wait()
    
def stim(name, resp):
    image.setImage(name)
    image.draw()
    win.flip()
    core.wait(resp)

win = visual.Window(color = 'white', fullscr = True) #Open a window with a white background, full screen instead of pixels 
text = visual.TextStim(win, None, color='Black', font = 'arial')
image = visual.ImageStim(win, None)

while True:
    instr('Welcome to this experiment', '2.0')
    
    if len(event.getKeys())>0:
        break 
    event.clearEvents()

win.close()
core.quit()