import psychopy.visual
import psychopy.event
import psychopy.core
import math


import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

win = psychopy.visual.Window(size=[800, 800], units="pix", fullscr=True, color=[0, 1, 0])


inst4 = psychopy.visual.TextStim(win,height=34,color='black',units="pix",wrapWidth=1000)
inst4.text = 'Welcome To The Virtual Foraging Task'; inst4.bold=True; inst4.pos=(0,350); inst4.height=30;inst4.draw()
inst4.text = 'You are in the center of a field surrounded by 6 berry shrubs.'; inst4.pos=(0,250); inst4.height=20; inst4.draw()
inst4.text = 'All the shrubs are equi distant from you and from their neighbours.'; inst4.pos=(0,200); inst4.draw() 
inst4.text = 'Click on the shrub you want to pick beries from.'; inst4.pos=(0,150); inst4.draw() 
inst4.text = 'Once you reach the shrub press "SPACEBAR" to harvest the berries.'; inst4.pos=(0,100); inst4.draw() 
inst4.text = 'Click on the shrubs to travel across them.'; inst4.pos=(0,50); inst4.draw() 
inst4.text = 'You have a total of 5 mins to harvest as much berries as you can.'; inst4.pos=(0,0); inst4.draw() 
inst4.text = 'Travel Time is proportional to the distance between shrubs.'; inst4.pos=(0,-50); inst4.draw() 
inst4.text = 'For any adjacent shrub, Travel Time costs 1 sec.'; inst4.pos=(0,-100); inst4.draw() 
inst4.text = 'After pressing Spacebar while on a shrub, wait for the reward to popup.This is your berry harvest time.'; inst4.pos=(0,-150); inst4.draw() 
inst4.text = 'For any shrub, Harvesting Time costs 0.5 sec .'; inst4.pos=(0,-200); inst4.draw() 

inst4.text = 'Happy Foraging';inst4.italic=True; inst4.height=25; inst4.pos=(00,-300); inst4.draw()
inst4.text = 'Press any key to continue';inst4.italic=True; inst4.height=25; inst4.pos=(00,-350); inst4.draw()

win.flip(); psychopy.core.wait(0.2);
psychopy.event.waitKeys()


patch1 = psychopy.visual.ImageStim(win=win, image="assets/berry.png", units="pix", pos=[150,-260])
patch2 = psychopy.visual.ImageStim(win=win, image="assets/berry.png", units="pix", pos=[-150,-260])
patch3 = psychopy.visual.ImageStim(win=win, image="assets/berry.png", units="pix", pos=[-300,0])
patch4 = psychopy.visual.ImageStim(win=win, image="assets/berry.png", units="pix", pos=[-150,260])
patch5 = psychopy.visual.ImageStim(win=win, image="assets/berry.png", units="pix", pos=[150,260])
patch6 = psychopy.visual.ImageStim(win=win, image="assets/berry.png", units="pix", pos=[300,0])
circle = psychopy.visual.ImageStim(win=win, image="assets/man.png", units="pix", pos=[0,0])
myMouse = psychopy.event.Mouse(visible=False, win=win)

e=[0,0,0,0,0,0]
r=[80,80,80,80,80,80]
l=[]
j=0

size_x = patch1.size[0]
size_y = patch1.size[1]

circle.size = [size_x*0.15, size_y*0.15]
patch1.size = patch2.size = patch3.size = patch4.size = patch5.size = patch6.size = [size_x * 0.1, size_y * 0.1]
patch_coord = [[0,0], [150,-260], [-150,-260], [-300,0], [-151,260], [151,260], [300,0]]
#patch_coord = [patch1.pos, patch2.pos, patch3.pos, patch4.pos, patch5.pos, patch6.pos]

clock_fullExp = psychopy.core.Clock()
ghadi_win = psychopy.visual.TextStim(win,height=34,color='black',units="pix",wrapWidth=1000)
ghadi = str(round(clock_fullExp.getTime(),0))
ghadi_win.text = "Time elapsed: " + ghadi; 
ghadi_win.bold=True; ghadi_win.pos=(450,300)

curr_pos = [0,0]
prev_pos = []
flag = 0

inst1 = psychopy.visual.TextStim(win,height=34,color='black',units="pix",wrapWidth=1000)
#inst1 shows current reward

inst2 = psychopy.visual.TextStim(win,height=34,color='black',units="pix",wrapWidth=1000)
inst2.text = 0; 
inst2.bold=True; inst2.pos=(-550,300)
#inst2 shows total reward
     
while clock_fullExp.getTime() < 30:
  
  ghadi = str(round(clock_fullExp.getTime(),0))
  ghadi_win.text = "Time elapsed: " + ghadi; 
  patch1.draw()
  patch2.draw()
  patch3.draw()
  patch4.draw()
  patch5.draw()
  patch6.draw()
  circle.draw()
  inst2.draw()  
  ghadi_win.draw()
  win.flip()

  myMouse = psychopy.event.Mouse(win=win, visible=True)
  
  clock_1 = psychopy.core.Clock()
  clock_1.reset()
  myMouse.clickReset()
  psychopy.event.clearEvents() #get rid of other, unprocessed events
  buttons, times = myMouse.getPressed(getTime = True)
  
  #flag = 0
  while flag==0:
    if (clock_fullExp.getTime() > 30): flag1=1
    buttons, times = myMouse.getPressed(getTime = True)
    pos = myMouse.getPos()
    #print("upar Current (x,y) position : ",pos,end="\r")
    x_pos = pos[0]
    y_pos = pos[1]
    if buttons == [1, 0, 0] or buttons == [0, 0, 1]:
      IsOn1 = (patch_coord[1][0]-20 < x_pos < patch_coord[1][0]+20)  and  (patch_coord[1][1]-20 < y_pos < patch_coord[1][1]+20)
      IsOn2 = (patch_coord[2][0]-20 < x_pos < patch_coord[2][0]+20)  and  (patch_coord[2][1]-20 < y_pos < patch_coord[2][1]+20)
      IsOn3 = (patch_coord[3][0]-20 < x_pos < patch_coord[3][0]+20)  and  (patch_coord[3][1]-20 < y_pos < patch_coord[3][1]+20)
      IsOn4 = (patch_coord[4][0]-20 < x_pos < patch_coord[4][0]+20)  and  (patch_coord[4][1]-20 < y_pos < patch_coord[4][1]+20)
      IsOn5 = (patch_coord[5][0]-20 < x_pos < patch_coord[5][0]+20)  and  (patch_coord[5][1]-20 < y_pos < patch_coord[5][1]+20)
      IsOn6 = (patch_coord[6][0]-20 < x_pos < patch_coord[6][0]+20)  and  (patch_coord[6][1]-20 < y_pos < patch_coord[6][1]+20)
      if IsOn1 or IsOn2 or IsOn3 or IsOn4 or IsOn5 or IsOn6:
        flag=1
        if(IsOn1):
          prev_pos = curr_pos
          curr_pos = patch_coord[1]
          idx=0
        elif(IsOn2):
          prev_pos = curr_pos
          curr_pos = patch_coord[2]
          idx=1
        elif(IsOn3):
          prev_pos = curr_pos
          curr_pos = patch_coord[3]
          idx=2
        elif(IsOn4):
          prev_pos = curr_pos
          curr_pos = patch_coord[4]
          idx=3
        elif(IsOn5):
          prev_pos = curr_pos
          curr_pos = patch_coord[5] 
          idx=4
        elif(IsOn6):
          prev_pos = curr_pos
          curr_pos = patch_coord[6]
          idx=5
  
#  print("\nPrevious position : ",prev_pos," and current position : ",curr_pos)
  
  x1 = prev_pos[0]
  y1 = prev_pos[1]
  x2 = curr_pos[0]
  y2 = curr_pos[1]

  m = (y2-y1)/(x2-x1)
  theta = math.atan(m)
  speed_pix_per_sec= 50
  xpos = 0
  total_dist = ((x2-x1)**2 + (y2-y1)**2)**0.5
  dur=total_dist/speed_pix_per_sec
  speed_costheta = speed_pix_per_sec * math.cos(theta)
  c = y1 - (m*x1)

  clock = psychopy.core.Clock()
  clock.reset()
  while clock.getTime() < dur:
    dist = speed_costheta*clock.getTime()
    #print(dist)
    if(curr_pos[0]<prev_pos[0]): xpos = x1-dist
    else: xpos = x1+dist
    ypos = m*xpos + c
    circle.pos = [xpos,ypos]
    inst2.text="Score: "+str(j)
    ghadi = str(round(clock_fullExp.getTime(),0))
    ghadi_win.text = "Time elapsed: " + ghadi; 
    patch1.draw()
    patch2.draw()
    patch3.draw()
    patch4.draw()    
    patch5.draw()
    patch6.draw()
    circle.draw()
    inst2.draw()
    ghadi_win.draw()
    win.flip()

  all_idx = [0,1,2,3,4,5]
  all_idx.remove(idx)
  flag1 = 0
  while flag1==0:
    if (clock_fullExp.getTime() > 30): flag1=1
    
    ghadi = str(round(clock_fullExp.getTime(),0))
    ghadi_win.text = "Time elapsed: "+ghadi
    
    patch1.draw()
    patch2.draw()
    patch3.draw()
    patch4.draw()    
    patch5.draw()
    patch6.draw()
    circle.draw()
    inst2.draw()
    ghadi_win.draw()
    win.flip()
    
    key_buttons = psychopy.event.getKeys(keyList=['space'])
    buttons, times = myMouse.getPressed(getTime = True)
    pos = myMouse.getPos()
    #print("neeche Current (x,y) position : ",pos,end="\r")
    x_pos = pos[0]
    y_pos = pos[1]
    if key_buttons ==['space']:
      e[idx]=e[idx]+1
      r[idx]=((0.95**(e[idx]-1))*r[idx])//1
      l.append(r[idx])
      print ("exploit",e)
      
      k=0
      for i in range(5):
        if (r[all_idx[i]] <= 96):    
          r[all_idx[i]] = k+(((r[all_idx[i]]*0.1)+r[all_idx[i]]))
          
        if (r[all_idx[i]] ==0): 
            k=5
            r[all_idx[i]] = k+(((r[all_idx[i]]*0.1)+r[all_idx[i]]))
      
      print ("reward",r)
      t=sum(l)
      inst1.text = "+"+str(r[idx]); 
      inst1.bold=True; inst1.pos=(0,300)
      inst2.text="Score: "+str((t))
      ghadi = str(round(clock_fullExp.getTime(),0))
      ghadi_win.text = "Time elapsed: " + ghadi; 
      patch1.draw()
      patch2.draw()
      patch3.draw()
      patch4.draw()    
      patch5.draw()
      patch6.draw()
      circle.draw()
      ghadi_win.draw()
      win.flip()
      
      psychopy.core.wait(2.0)
      ghadi = str(round(clock_fullExp.getTime(),0))
      ghadi_win.text = "Time elapsed: " + ghadi; 
      inst1.text = "+"+str(r[idx]); 
      inst1.bold=True; inst1.pos=(0,300)
      inst1.draw()
      patch1.draw()
      patch2.draw()
      patch3.draw()
      patch4.draw()    
      patch5.draw()
      patch6.draw()
      circle.draw()
      inst2.draw()
      ghadi_win.draw()
      win.flip()
      psychopy.core.wait(0.7)
           
    elif key_buttons==[] and buttons[0]==1:
      IsOn1 = (patch_coord[1][0]-20 < x_pos < patch_coord[1][0]+20)  and  (patch_coord[1][1]-20 < y_pos < patch_coord[1][1]+20)
      IsOn2 = (patch_coord[2][0]-20 < x_pos < patch_coord[2][0]+20)  and  (patch_coord[2][1]-20 < y_pos < patch_coord[2][1]+20)
      IsOn3 = (patch_coord[3][0]-20 < x_pos < patch_coord[3][0]+20)  and  (patch_coord[3][1]-20 < y_pos < patch_coord[3][1]+20)
      IsOn4 = (patch_coord[4][0]-20 < x_pos < patch_coord[4][0]+20)  and  (patch_coord[4][1]-20 < y_pos < patch_coord[4][1]+20)
      IsOn5 = (patch_coord[5][0]-20 < x_pos < patch_coord[5][0]+20)  and  (patch_coord[5][1]-20 < y_pos < patch_coord[5][1]+20)
      IsOn6 = (patch_coord[6][0]-20 < x_pos < patch_coord[6][0]+20)  and  (patch_coord[6][1]-20 < y_pos < patch_coord[6][1]+20)
      if IsOn1 or IsOn2 or IsOn3 or IsOn4 or IsOn5 or IsOn6:
        flag1=1
        if(IsOn1):
          prev_pos = curr_pos
          curr_pos = patch_coord[1]
          idx=0
        elif(IsOn2):
          prev_pos = curr_pos
          curr_pos = patch_coord[2]
          idx=1
        elif(IsOn3):
          prev_pos = curr_pos
          curr_pos = patch_coord[3]
          idx=2
        elif(IsOn4):
          prev_pos = curr_pos
          curr_pos = patch_coord[4]
          idx=3
        elif(IsOn5):
          prev_pos = curr_pos
          curr_pos = patch_coord[5] 
          idx=4
        elif(IsOn6):
          prev_pos = curr_pos
          curr_pos = patch_coord[6]
          idx=5
      
      ghadi = str(round(clock_fullExp.getTime(),0))
      ghadi_win.text = "Time elapsed: " + ghadi; 
      patch1.draw()
      patch2.draw()
      patch3.draw()
      patch4.draw()    
      patch5.draw()
      patch6.draw()
      circle.draw()
      inst2.draw()
      ghadi_win.draw()
      win.flip()
        
      j=sum(l)
      #print(j)
     
inst = psychopy.visual.TextStim(win,height=34,color='black',units="pix",wrapWidth=1000)
inst.text = 'Task Over'; inst.bold=True; inst.pos=(0,300); inst.height=30;inst.draw()
inst.text = 'Thank You for your participation.'; inst.pos=(0,200); inst.height=25; inst.draw()
inst.text = 'Press any key to exit.'; inst.pos=(0,150); inst.draw() 

win.flip(); psychopy.core.wait(0.2);
psychopy.event.waitKeys()
win.close()