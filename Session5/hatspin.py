# import psychopy's core module, and the visual module for presenting visual stimuli
from psychopy import core, visual,event


# open a window of 800 by 600 pixels (note the tuple for specifying size!)
win = visual.Window((800, 600), color='teal')
img = visual.ImageStim(win = win, image = None)

count = 1 #keep track of which picture we are on

Increment = 1 #this is so we can control the rotation speed

while True:
	keyPress = event.getKeys(keyList=['space','escape','up','down','right','left'])
	if 'escape' in keyPress: #stop the presentation with spacebar
		break
	elif 'up' in keyPress: #speed up with up key
		if Increment > 0:
			Increment += 1
		else: 
			Increment -= 1
	elif 'down' in keyPress: #slow down with down key
		if Increment > 0:
			Increment -= 1
		elif Increment == 0:
			Increment = Increment
		else: 
			Increment += 1
	elif 'left' in keyPress: #counterclockwise
		if Increment < 0:
			Increment = Increment*-1 #make sure it's a positive number and it will go counterclockwise
	elif 'right' in keyPress: #clockwise
		if Increment > 0:
			Increment = Increment*-1
	elif 'space' in keyPress: #pause
		event.waitKeys(keyList = 'space')		

	#draw the hat
	img.setImage(f'hat_{count}.png')
	img.draw()
	win.flip()

	#increment the file counter
	count += Increment

	#keep this hat spinning
	if count > 360:
		count = 1
	if count < 1:
		count = 360


win.close() #close window