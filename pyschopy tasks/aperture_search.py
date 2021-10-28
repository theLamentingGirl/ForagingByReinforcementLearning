#imports
from __future__ import absolute_import, division
import numpy as np

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock

from psychopy.tools.monitorunittools import posToPix

import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


# Setup the Window
win = visual.Window(
    size=[800, 800], fullscr=True, screen=0, 
    winType='pyglet',allowGUI=False, allowStencil=True,
    monitor='testMonitor', color=[-0.600,-0.200,-0.600], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
#Remember units are in pix units by default for the while window. Don't try to keep changing it for element to element

#inputs
default_keyboard = keyboard.Keyboard()
default_mouse = event.Mouse()

#INITIALISING lists
reward = [80,80,80]
exploit = [0,0,0]
collected = [0,0,0]
reward_index = [0,1,2] 
# replenish = [0,0,0]

start_time = clock.getAbsTime()


#INITILISING IMG 
grass = visual.ImageStim(win,image = 'assets/grass.jpg',size = (800,800))

berry1 = visual.ImageStim(win,image = 'assets/berry.png',pos = (150,200), size=(50,50))
berry2 = visual.ImageStim(win,image = 'assets/berry.png',pos = (-150,200), size=(50,50))
berry3 = visual.ImageStim(win,image = 'assets/berry.png',pos = (-150,-200), size=(50,50))

#initialising text
text = visual.TextStim(win, text= 'Total reward:'+str(reward),height=24,bold=True) #Total reward text
welcome_text = visual.TextStim(win,text = 'Use mouse to navigate through the field.\n Click on the berry to collect reward. \n When berry is clicked, there is a harvest time of 5s you should wait after which you get the reward. \n To begin the experiment press any key. Press esc to exit. ')
time_text = visual.TextStim(win, text = 'Time elapsed:'+str(clock.getAbsTime() - start_time),height=24,bold=True)
reward_text = visual.TextStim(win,text = '',height =24,bold=True)
thanks_text = visual.TextStim(win, text = 'Thank you for your participation.press any key to end the experiment. Go haffun!', bold = True)

'''screen1 :welcome''' 

welcome_text.draw()
win.flip()
event.waitKeys()


'''screen2 : the game'''
continueRoutine = True

#loop running the exp
while continueRoutine:

    #resetting opacity
    grass.opacity = 1

    berry1.opacity = 1
    berry2.opacity = 1
    berry3.opacity = 1

    #getting the location of mouse
    mouse_location = default_mouse.getPos()

    #drawing the elements to be drawn permanently aka every frame
    grass.setAutoDraw(True)

    berry1.setAutoDraw(True)
    berry2.setAutoDraw(True)
    berry3.setAutoDraw(True)

    #aperture is drawn every frame and aperture gets to position of mouse foe the 'spotlight' like movemnet to happen
    aperture = visual.Aperture(win, name='aperture',shape = 'circle', units = 'pix',size=100, pos=default_mouse.getPos())
    
    #setting the position where the reward and time elapsed will be displayed
    text.pos = [-580,300]
    time_text.pos=[580,300]
    reward_text.pos = default_mouse.getPos()

    #changing the texts on every update
    time_elapsed = clock.getAbsTime() - start_time
    time_text.text = 'Time elapsed:'+ str(clock.getAbsTime() - start_time)
    text.text = 'Total reward:'+str(np.sum(collected))

    #making the berry images a clickable stimuli
    berry1_click = default_mouse.isPressedIn(berry1,buttons=[0])
    berry2_click = default_mouse.isPressedIn(berry2,buttons=[0])
    berry3_click = default_mouse.isPressedIn(berry3,buttons=[0])

    berry_click = [berry1_click,berry2_click,berry3_click]
        
    for i in range(len(berry_click)):
        if berry_click[i]:
            # disappering the objects to display the reward at that moment
            click_time = time_elapsed
            grass.opacity = 0

            berry1.opacity = 0
            berry2.opacity = 0
            berry3.opacity = 0
            
            exploit[i] = exploit[i] + 1
            print("Array of exploits",exploit) #this is our data for trajectory travelled

            #reward equation
            reward[i] = ((0.95**(exploit[i]-1))*reward[i])//1
            collected[i] = collected[i] + reward[i]
            print("This is the reward collected", collected)
            #replenishment eqn
            reward_index.remove(i)

            for j in range(len(reward_index)):
                if reward[reward_index[j]] <= 96:
                    k = 0
                    reward[reward_index[j]] = k + (((reward[reward_index[j]]*0.1)+reward[reward_index[j]]))
                elif reward[reward_index[j]] == 0:
                    k = 5
                    reward[reward_index[j]] = k + (((reward[reward_index[j]]*0.1)+reward[reward_index[j]]))

            reward_index.append(i)


            reward_text.text = '+'+str(reward[i])

            reward_text.draw()
            text.draw()
            
            '''TO ADD A COUNTDOWN OF 5s'''

            win.flip()
            core.wait(5)
            
    text.draw()
    time_text.draw()

    aperture.enabled = True 

    win.flip()

    #to force quit the experiment
    if default_keyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    #to stop the experiment in 'x' seconds
    if (clock.getAbsTime() - start_time)>30:
        print("Experiment done")
        thanks_text.draw()
        win.flip()
        # core.wait(0.2)
        event.waitKeys()
        win.close()
        continueRoutine = False



'''screen 3: Thank you'''


# inst = visual.TextStim(win,height=34,color='black',units="pix",wrapWidth=1000)
# inst.text = 'Task Over'; inst.bold=True; inst.pos=(0,300); inst.height=30;inst.draw()
# inst.text = 'Thank You for your participation.'; inst.pos=(0,200); inst.height=25; inst.draw()
# inst.text = 'Press any key to exit.'; inst.pos=(0,150); inst.draw() 

# win.flip(); core.wait(0.2);
# event.waitKeys()
# win.close()

