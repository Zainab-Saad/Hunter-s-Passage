import tkinter as tk
import timeit
from winsound import *
from random import randint as rand

#define radiobuttons of mode button
mode_selected=False
def mode_click():
    global v
    v=tk.IntVar()
    tk.Radiobutton(frame,text="DARK MODE ",variable=v,value=2,indicatoron=0).place(x=250,y=100)
    tk.Radiobutton(frame,text="LIGHT MODE",variable=v,value=1,indicatoron=0).place(x=250,y=75)
    global mode_selected
    mode_selected=True

stopped=False
bosskey=True


#boss key , window minimizes on pressing b on keyboard
def bosskey(event):
    global bosskey
    if bosskey:
        #make the window minimize 
        window.state(newstate='iconic')
        bosskey=False
    else:
        window.state(newstate='normal')
    
#pause, game pauses on pressing p on keyboard
def pause_play(event):
    global stopped
    if stopped:
        stopped = False
    else:
        stopped = True

#checks after intervals if bullet hits enemy, if it does delete bullet and enemy from canvas, and add 100 points to total score
def killing_enemy():
    global points_on_shooting
    
    
    if (eB5_L2[0]<bB_L2[2]<eB5_L2[2] and eB5_L2[1]<bB_L2[1]<eB5_L2[3]) or (eB5_L2[0]<bB_L2[2]<eB5_L2[2] and eB5_L2[1]<bB_L2[3]<eB5_L2[3]) or (eB5_L2[0]<bB_L2[0]<eB5_L2[2] and eB5_L2[1]<bB_L2[1]<eB5_L2[3]) or (eB5_L2[0]<bB_L2[0]<eB5_L2[2] and eB5_L2[1]<bB_L2[3]<eB5_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy5_L2)
        global en5
        if en5=='present':
            canvas.delete(rectangle)
        en5='absent'
        Variable=False
        
    elif (eB6_L2[0]<bB_L2[2]<eB6_L2[2] and eB6_L2[1]<bB_L2[1]<eB6_L2[3]) or (eB6_L2[0]<bB_L2[2]<eB6_L2[2] and eB6_L2[1]<bB_L2[3]<eB6_L2[3]) or (eB6_L2[0]<bB_L2[0]<eB6_L2[2] and eB6_L2[1]<bB_L2[1]<eB6_L2[3]) or (eB6_L2[0]<bB_L2[0]<eB6_L2[2] and eB6_L2[1]<bB_L2[3]<eB6_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy6_L2)
        global en6
        if en6=='present':
            canvas.delete(rectangle)
        
        en6='absent'
        
        
        Variable=False
        
    elif (eB7_L2[0]<bB_L2[2]<eB7_L2[2] and eB7_L2[1]<bB_L2[1]<eB7_L2[3]) or (eB7_L2[0]<bB_L2[2]<eB7_L2[2] and eB7_L2[1]<bB_L2[3]<eB7_L2[3]) or (eB7_L2[0]<bB_L2[0]<eB7_L2[2] and eB7_L2[1]<bB_L2[1]<eB7_L2[3]) or (eB7_L2[0]<bB_L2[0]<eB7_L2[2] and eB7_L2[1]<bB_L2[3]<eB7_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy7_L2)
        global en7
        if en7=='present':
            canvas.delete(rectangle)
        
        en7='absent'
        
        
        Variable=False
        
    elif (eB8_L2[0]<bB_L2[2]<eB8_L2[2] and eB8_L2[1]<bB_L2[1]<eB8_L2[3]) or (eB8_L2[0]<bB_L2[2]<eB8_L2[2] and eB8_L2[1]<bB_L2[3]<eB8_L2[3]) or (eB8_L2[0]<bB_L2[0]<eB8_L2[2] and eB8_L2[1]<bB_L2[1]<eB8_L2[3]) or (eB8_L2[0]<bB_L2[0]<eB8_L2[2] and eB8_L2[1]<bB_L2[3]<eB8_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy8_L2)
        global en8
        if en8=='present':
            canvas.delete(rectangle)
        
        en8='absent'
        
        
        Variable=False
        
    elif (eB9_L2[0]<bB_L2[2]<eB9_L2[2] and eB9_L2[1]<bB_L2[1]<eB9_L2[3]) or (eB9_L2[0]<bB_L2[2]<eB9_L2[2] and eB9_L2[1]<bB_L2[3]<eB9_L2[3]) or (eB9_L2[0]<bB_L2[0]<eB9_L2[2] and eB9_L2[1]<bB_L2[1]<eB9_L2[3]) or (eB9_L2[0]<bB_L2[0]<eB9_L2[2] and eB9_L2[1]<bB_L2[3]<eB9_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy9_L2)
        global en9
        if en9=='present':
            canvas.delete(rectangle)
        
        en9='absent'
        Variable=False
        
    elif (eB10_L2[0]<bB_L2[2]<eB10_L2[2] and eB10_L2[1]<bB_L2[1]<eB10_L2[3]) or (eB10_L2[0]<bB_L2[2]<eB10_L2[2] and eB10_L2[1]<bB_L2[3]<eB10_L2[3]) or (eB10_L2[0]<bB_L2[0]<eB10_L2[2] and eB10_L2[1]<bB_L2[1]<eB10_L2[3]) or (eB10_L2[0]<bB_L2[0]<eB10_L2[2] and eB10_L2[1]<bB_L2[3]<eB10_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy10_L2)
        global en10
        if en10=='present':
            canvas.delete(rectangle)
        
        en10='absent'
        
        
        Variable=False
        
    elif (eB1_L2[0]<bB_L2[2]<eB1_L2[2] and eB1_L2[1]<bB_L2[1]<eB1_L2[3]) or (eB1_L2[0]<bB_L2[2]<eB1_L2[2] and eB1_L2[1]<bB_L2[3]<eB1_L2[3]) or (eB1_L2[0]<bB_L2[0]<eB1_L2[2] and eB1_L2[1]<bB_L2[1]<eB1_L2[3]) or (eB1_L2[0]<bB_L2[0]<eB1_L2[2] and eB1_L2[1]<bB_L2[3]<eB1_L2[3]): 
        points_on_shooting+=100
        canvas.delete(Enemy1_L2)
        global en1
        if en1=='present':
            canvas.delete(rectangle)
        
        en1='absent'
        
        
        Variable=False
        
    elif (eB2_L2[0]<bB_L2[2]<eB2_L2[2] and eB2_L2[1]<bB_L2[1]<eB2_L2[3]) or (eB2_L2[0]<bB_L2[2]<eB2_L2[2] and eB2_L2[1]<bB_L2[3]<eB2_L2[3]) or (eB2_L2[0]<bB_L2[0]<eB2_L2[2] and eB2_L2[1]<bB_L2[1]<eB2_L2[3]) or (eB2_L2[0]<bB_L2[0]<eB2_L2[2] and eB2_L2[1]<bB_L2[3]<eB2_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy2_L2)
        global en2
        if en2=='present':
            canvas.delete(rectangle)
        
        en2='absent'
        Variable=False
        
    elif (eB3_L2[0]<bB_L2[2]<eB3_L2[2] and eB3_L2[1]<bB_L2[1]<eB3_L2[3]) or (eB3_L2[0]<bB_L2[2]<eB3_L2[2] and eB3_L2[1]<bB_L2[3]<eB3_L2[3]) or (eB3_L2[0]<bB_L2[0]<eB3_L2[2] and eB3_L2[1]<bB_L2[1]<eB3_L2[3]) or (eB3_L2[0]<bB_L2[0]<eB3_L2[2] and eB3_L2[1]<bB_L2[3]<eB3_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy3_L2)
        global en3
        if en3=='present':
            canvas.delete(rectangle)
        
        en3='absent'
        
        
        Variable=False
        
    elif (eB4_L2[0]<bB_L2[2]<eB4_L2[2] and eB4_L2[1]<bB_L2[1]<eB4_L2[3]) or (eB4_L2[0]<bB_L2[2]<eB4_L2[2] and eB4_L2[1]<bB_L2[3]<eB4_L2[3]) or (eB4_L2[0]<bB_L2[0]<eB4_L2[2] and eB4_L2[1]<bB_L2[1]<eB4_L2[3]) or (eB4_L2[0]<bB_L2[0]<eB4_L2[2] and eB4_L2[1]<bB_L2[3]<eB4_L2[3]):
        points_on_shooting+=100
        canvas.delete(Enemy4_L2)
        global en4
        if en4=='present':
            canvas.delete(rectangle)
        
        en4='absent'
        
        
        Variable=False
        
#release bullets upon pressing spacebar
def shoot(event):
    
    global Variable
    Variable=True
    global rectangle
    rectangle=canvas.create_rectangle((sB_L2[0]+sB_L2[2])//2,(sB_L2[1]+sB_L2[3])//2,((sB_L2[0]+sB_L2[2])//2)+5,(sB_L2[1]+sB_L2[3])//2,tags="rect",fill="red")
    #moves the bullet across canvas
    def bullet_move():
        global bB_L2
        bB_L2=canvas.bbox("rect")
        if bB_L2[2]>=1270:
            canvas.delete(rectangle)
        else:
        
            dx_shoot=15
            dy_shoot=0
            canvas.move(rectangle,dx_shoot,dy_shoot)
            
                
            killing_enemy()
            if Variable==False:
                return
            elif Variable==True:
                window.after(30,bullet_move)
        
    bullet_move()
    
#next four functions bounce the enemy back when it hits the screen and changes its speed upon bouncing too IN LEVEL 1
def move_enemy_up1():
    global eB1
    eB1=canvas.bbox("enemy1")

    
    if eB1[1]>5:
        dx=0
        dy=-40
        if not stopped:
            canvas.move(Enemy1,dx,dy)
        window.after(50,move_enemy_up1)
    else:
        window.after(50,move_enemy1)
def move_enemy_up2():
    global eB2
    eB2=canvas.bbox("enemy2")

    
    if eB2[1]<=900:
        dx=0
        dy=35
        if not stopped:
            canvas.move(Enemy2,dx,dy)
        window.after(50,move_enemy_up2)
    else:
        window.after(50,move_enemy2)

def move_enemy_up3():
    global eB3
    eB3=canvas.bbox("enemy3")

    
    if eB3[1]>5:
        dx=0
        dy=-30
        if not stopped:
            canvas.move(Enemy3,dx,dy)
        window.after(50,move_enemy_up3)
    else:
        window.after(50,move_enemy3)


def move_enemy_up4():
    global eB4
    eB4=canvas.bbox("enemy4")

    
    if eB4[1]<=900:
        dx=0
        dy=37
        if not stopped:
            canvas.move(Enemy4,dx,dy)
        window.after(50,move_enemy_up4)
    else:
        window.after(50,move_enemy4)
        
#next 4 functions move the enemy IN LEVEL 1
def move_enemy1():
    global eB1
    eB1=canvas.bbox("enemy1")
    if eB1[3]<=900:
        dx=0
        dy=35
        if not stopped:
            canvas.move(Enemy1,dx,dy)
        window.after(50,move_enemy1)
    

        
    if eB1[3]>900:
        move_enemy_up1()

def move_enemy2():
    global eB2
    eB2=canvas.bbox("enemy2")
    if eB2[3]>5:
        dx=0
        dy=-60
        if not stopped:
            canvas.move(Enemy2,dx,dy)
        window.after(50,move_enemy2)
    if eB2[3]<=5:
        move_enemy_up2()

def move_enemy3():
    global eB3
    eB3=canvas.bbox("enemy3")
    if eB3[3]<=900:
        dx=0
        dy=45
        if not stopped:
            canvas.move(Enemy3,dx,dy)
        window.after(50,move_enemy3)
    if eB3[3]>900:
        move_enemy_up3()

def move_enemy4():
    global eB4
    eB4=canvas.bbox("enemy4")
    if eB4[3]>5:
        dx=0
        dy=-40
        if not stopped:
            canvas.move(Enemy4,dx,dy)
        window.after(50,move_enemy4)
    if eB4[3]<=5:
        move_enemy_up4()
        

#check collision detection in level 1
#1)determine the bbox of 4 enemies
#2)display label upon collision
def collisionDetection():
    
    if (eB1[0]<sB[2]<eB1[2] and eB1[1]<sB[1]<eB1[3]) or (eB1[0]<sB[2]<eB1[2] and eB1[1]<sB[3]<eB1[3]) or (eB1[0]<sB[0]<eB1[2] and eB1[1]<sB[1]<eB1[3]) or (eB1[0]<sB[0]<eB1[2] and eB1[1]<sB[3]<eB1[3]): 
        canvas.delete(shooter)
        canvas.delete(Enemy1)
        canvas.delete(Enemy2)
        canvas.delete(Enemy3)
        canvas.delete(Enemy4)
        lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
        GO_lbl=tk.Label(lf,text="Do you want to play again?",bg="gray",padx=100,pady=50)
        GO_lbl.config(font='Arial 12')
        GO_lbl.grid(row=0,column=0,columnspan=2)
        GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=canvas.destroy)
        GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
        GO_button1.grid(row=1,column=0)
        GO_button2.grid(row=1,column=1)
        

        lf.place(x=450,y=220)
    #################################   
    if (eB2[0]<sB[2]<eB2[2] and eB2[1]<sB[1]<eB2[3]) or (eB2[0]<sB[2]<eB2[2] and eB2[1]<sB[3]<eB2[3]) or (eB2[0]<sB[0]<eB2[2] and eB2[1]<sB[1]<eB2[3]) or (eB2[0]<sB[0]<eB2[2] and eB2[1]<sB[3]<eB2[3]):
        canvas.delete(shooter)
        canvas.delete(Enemy1)
        canvas.delete(Enemy2)
        canvas.delete(Enemy3)
        canvas.delete(Enemy4)
        
        lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
        GO_lbl=tk.Label(lf,text="Do you want to play again?",bg="gray",padx=100,pady=50)
        GO_lbl.config(font='Arial 12')
        GO_lbl.grid(row=0,column=0,columnspan=2)
        GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=canvas.destroy)
        GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
        GO_button1.grid(row=1,column=0)
        GO_button2.grid(row=1,column=1)
        

        lf.place(x=450,y=220)
    ####################################
    if (eB3[0]<sB[2]<eB3[2] and eB3[1]<sB[1]<eB3[3]) or (eB3[0]<sB[2]<eB3[2] and eB3[1]<sB[3]<eB3[3]) or (eB3[0]<sB[0]<eB3[2] and eB3[1]<sB[1]<eB3[3]) or (eB3[0]<sB[0]<eB3[2] and eB3[1]<sB[3]<eB3[3]):
        canvas.delete(shooter)
        canvas.delete(Enemy1)
        canvas.delete(Enemy2)
        canvas.delete(Enemy3)
        canvas.delete(Enemy4)
        
        lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
        GO_lbl=tk.Label(lf,text="Do you want to play again?",bg="gray",padx=100,pady=50)
        GO_lbl.config(font='Arial 12')
        GO_lbl.grid(row=0,column=0,columnspan=2)
        GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=canvas.destroy)
        GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
        GO_button1.grid(row=1,column=0)
        GO_button2.grid(row=1,column=1)
        

        lf.place(x=450,y=220)
    #####################################
    if (eB4[0]<sB[2]<eB4[2] and eB4[1]<sB[1]<eB4[3]) or (eB4[0]<sB[2]<eB4[2] and eB4[1]<sB[3]<eB4[3]) or (eB4[0]<sB[0]<eB4[2] and eB4[1]<sB[1]<eB4[3]) or (eB4[0]<sB[0]<eB4[2] and eB4[1]<sB[3]<eB4[3]):
        canvas.delete(shooter)
        canvas.delete(Enemy1)
        canvas.delete(Enemy2)
        canvas.delete(Enemy3)
        canvas.delete(Enemy4)
        lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
        GO_lbl=tk.Label(lf,text="Do you want to play again?",bg="gray",padx=100,pady=50)
        GO_lbl.config(font='Arial 12')
        GO_lbl.grid(row=0,column=0,columnspan=2)
        GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=canvas.destroy)
        GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
        GO_button1.grid(row=1,column=0)
        GO_button2.grid(row=1,column=1)
        

        lf.place(x=450,y=220)
    ########################################
    
    
#collision detection with enemies in level 2
#1)determine the bbox of 10 enemies
#2)display label upon collision
def collisiondetection_L2():
    if en1=='present':
        if (eB1_L2[0]<sB_L2[2]<eB1_L2[2] and eB1_L2[1]<sB_L2[1]<eB1_L2[3]) or (eB1_L2[0]<sB_L2[2]<eB1_L2[2] and eB1_L2[1]<sB_L2[3]<eB1_L2[3]) or (eB1_L2[0]<sB_L2[0]<eB1_L2[2] and eB1_L2[1]<sB_L2[1]<eB1_L2[3]) or (eB1_L2[0]<sB_L2[0]<eB1_L2[2] and eB1_L2[1]<sB_L2[3]<eB1_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en2=='present':
        if (eB2_L2[0]<sB_L2[2]<eB2_L2[2] and eB2_L2[1]<sB_L2[1]<eB2_L2[3]) or (eB2_L2[0]<sB_L2[2]<eB2_L2[2] and eB2_L2[1]<sB_L2[3]<eB2_L2[3]) or (eB2_L2[0]<sB_L2[0]<eB2_L2[2] and eB2_L2[1]<sB_L2[1]<eB2_L2[3]) or (eB2_L2[0]<sB_L2[0]<eB2_L2[2] and eB2_L2[1]<sB_L2[3]<eB2_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en3=='present':
        if (eB3_L2[0]<sB_L2[2]<eB3_L2[2] and eB3_L2[1]<sB_L2[1]<eB3_L2[3]) or (eB3_L2[0]<sB_L2[2]<eB3_L2[2] and eB3_L2[1]<sB_L2[3]<eB3_L2[3]) or (eB3_L2[0]<sB_L2[0]<eB3_L2[2] and eB3_L2[1]<sB_L2[1]<eB3_L2[3]) or (eB3_L2[0]<sB_L2[0]<eB3_L2[2] and eB3_L2[1]<sB_L2[3]<eB3_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en4=='present':
        if (eB4_L2[0]<sB_L2[2]<eB4_L2[2] and eB4_L2[1]<sB_L2[1]<eB4_L2[3]) or (eB4_L2[0]<sB_L2[2]<eB4_L2[2] and eB4_L2[1]<sB_L2[3]<eB4_L2[3]) or (eB4_L2[0]<sB_L2[0]<eB4_L2[2] and eB4_L2[1]<sB_L2[1]<eB4_L2[3]) or (eB4_L2[0]<sB_L2[0]<eB4_L2[2] and eB4_L2[1]<sB_L2[3]<eB4_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en5=='present':
        if (eB5_L2[0]<sB_L2[2]<eB5_L2[2] and eB5_L2[1]<sB_L2[1]<eB5_L2[3]) or (eB5_L2[0]<sB_L2[2]<eB5_L2[2] and eB5_L2[1]<sB_L2[3]<eB5_L2[3]) or (eB5_L2[0]<sB_L2[0]<eB5_L2[2] and eB5_L2[1]<sB_L2[1]<eB5_L2[3]) or (eB5_L2[0]<sB_L2[0]<eB5_L2[2] and eB5_L2[1]<sB_L2[3]<eB5_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en6=='present':
        if (eB6_L2[0]<sB_L2[2]<eB6_L2[2] and eB6_L2[1]<sB_L2[1]<eB6_L2[3]) or (eB6_L2[0]<sB_L2[2]<eB6_L2[2] and eB6_L2[1]<sB_L2[3]<eB6_L2[3]) or (eB6_L2[0]<sB_L2[0]<eB6_L2[2] and eB6_L2[1]<sB_L2[1]<eB6_L2[3]) or (eB6_L2[0]<sB_L2[0]<eB6_L2[2] and eB6_L2[1]<sB_L2[3]<eB6_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en7=='present':
        if (eB7_L2[0]<sB_L2[2]<eB7_L2[2] and eB7_L2[1]<sB_L2[1]<eB7_L2[3]) or (eB7_L2[0]<sB_L2[2]<eB7_L2[2] and eB7_L2[1]<sB_L2[3]<eB7_L2[3]) or (eB7_L2[0]<sB_L2[0]<eB7_L2[2] and eB7_L2[1]<sB_L2[1]<eB7_L2[3]) or (eB7_L2[0]<sB_L2[0]<eB7_L2[2] and eB7_L2[1]<sB_L2[3]<eB7_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en8=='present':
        if (eB8_L2[0]<sB_L2[2]<eB8_L2[2] and eB8_L2[1]<sB_L2[1]<eB8_L2[3]) or (eB8_L2[0]<sB_L2[2]<eB8_L2[2] and eB8_L2[1]<sB_L2[3]<eB8_L2[3]) or (eB8_L2[0]<sB_L2[0]<eB8_L2[2] and eB8_L2[1]<sB_L2[1]<eB8_L2[3]) or (eB8_L2[0]<sB_L2[0]<eB8_L2[2] and eB8_L2[1]<sB_L2[3]<eB8_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en9=='present':
        if (eB9_L2[0]<sB_L2[2]<eB9_L2[2] and eB9_L2[1]<sB_L2[1]<eB9_L2[3]) or (eB9_L2[0]<sB_L2[2]<eB9_L2[2] and eB9_L2[1]<sB_L2[3]<eB9_L2[3]) or (eB9_L2[0]<sB_L2[0]<eB9_L2[2] and eB9_L2[1]<sB_L2[1]<eB9_L2[3]) or (eB9_L2[0]<sB_L2[0]<eB9_L2[2] and eB9_L2[1]<sB_L2[3]<eB9_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################
    if en10=='present':
        if (eB10_L2[0]<sB_L2[2]<eB10_L2[2] and eB10_L2[1]<sB_L2[1]<eB10_L2[3]) or (eB10_L2[0]<sB_L2[2]<eB10_L2[2] and eB10_L2[1]<sB_L2[3]<eB10_L2[3]) or (eB10_L2[0]<sB_L2[0]<eB10_L2[2] and eB10_L2[1]<sB_L2[1]<eB10_L2[3]) or (eB10_L2[0]<sB_L2[0]<eB10_L2[2] and eB10_L2[1]<sB_L2[3]<eB10_L2[3]): 
            canvas.delete(shooter_L2)
            canvas.delete(Enemy1_L2)
            canvas.delete(Enemy2_L2)
            canvas.delete(Enemy3_L2)
            canvas.delete(Enemy4_L2)
            canvas.delete(Enemy5_L2)
            canvas.delete(Enemy6_L2)
            canvas.delete(Enemy7_L2)
            canvas.delete(Enemy8_L2)
            canvas.delete(Enemy9_L2)
            canvas.delete(Enemy10_L2)
            lf=tk.LabelFrame(canvas,text="GAME OVER",bg="pink")
            GO_lbl=tk.Label(lf,text="Do you want to start level 2 again?",bg="gray",padx=100,pady=50)
            GO_lbl.config(font='Arial 12')
            GO_lbl.grid(row=0,column=0,columnspan=2)
            GO_button1=tk.Button(lf,text="Yes",padx=60,pady=25,command=game_loopL2)
            GO_button2=tk.Button(lf,text="No",padx=60,pady=25,command=window.destroy)
            GO_button1.grid(row=1,column=0)
            GO_button2.grid(row=1,column=1)
            

            lf.place(x=450,y=220)
            canvas.after(2500,lf.destroy)
    #################################   
    

#setting up canvas for level 1
#placing shooter and 4 enemies
def canvas_thingsL1():
    global canvas
    #background for light mode
    def bg_lightmode():
        global canvas
        canvas =tk.Canvas(window,width=1280,height =720,bg="#06d0ff")
        canvas.pack()
        canvas.create_oval(-80,-50,100,150,fill="yellow")
        canvas.create_rectangle(0,650,320,720,fill="#b15126",width=0)
        canvas.create_rectangle(320,650,640,720,fill="#c45126",width=0)
        canvas.create_rectangle(640,650,960,720,fill="#d75126",width=0)
        canvas.create_rectangle(960,650,1280,720,fill="#e95126",width=0)

    #background for dark mode
    def bg_darkmode():
        global canvas
        canvas=tk.Canvas(window,width=1280,height=720)
        canvas.pack(expand=True)
        canvas.config(bg="#263235")
        c=["white","#fefefe","#fdfdfd"]
        for i in range(360):
            x=rand(1,1280)
            y=rand(1,300)
            size=rand(2,5)
            f=rand(0,2)
            xy=(x,y,x+size,y+size)
            tmp_star=canvas.create_oval(xy)
            canvas.itemconfig(tmp_star,fill=c[f])
        
    #sets the bg according to mode selected by user, starts game in light mode by default if no mode selected
    if mode_selected==True:
        which_mode_selected=v.get()
        if which_mode_selected==1:
            bg_lightmode()
        elif which_mode_selected==2:
            bg_darkmode()
        else:
            bg_lightmode()
    elif mode_selected==False:
        bg_lightmode()
        
        
    lbl=canvas.create_text(1220,20,text="END",font=("Arial 20 bold"))

    global img
    img= tk.PhotoImage(file="shooter4_gif_resized.gif")
    global enemy1
    enemy1=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy2
    enemy2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy3
    enemy3=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy4
    enemy4=tk.PhotoImage(file="enemy_game4_resized.gif")

    ###########################
    global shooter
    shooter=canvas.create_image(0, 650, image=img,anchor='nw',tags="shooter")

    
    global Enemy1
    Enemy1=canvas.create_image(200, 220, image=enemy1,tags="enemy1")
    global Enemy2
    Enemy2=canvas.create_image(500, 220, image=enemy2,tags="enemy2")
    global Enemy3
    Enemy3=canvas.create_image(800, 220, image=enemy3,tags="enemy3")
    global Enemy4
    Enemy4=canvas.create_image(1100, 220, image=enemy4,tags="enemy4")
    
    ############################
    global eB1
    eB1=canvas.bbox("enemy1")
    global eB2
    eB2=canvas.bbox("enemy2")
    global eB3
    eB3=canvas.bbox("enemy3")
    global eB4
    eB4=canvas.bbox("enemy4")
    
#setting up canvas for level 2
#plaicing shooter and 10 enemies
def canvas_thingsL2():
    
    canvas.delete(shooter)
    canvas.delete(Enemy1)
    canvas.delete(Enemy2)
    canvas.delete(Enemy3)
    canvas.delete(Enemy4)
    

    ###########################

    global img_L2
    img_L2= tk.PhotoImage(file="shooter4_gif_resized.gif")
    global enemy1_L2
    enemy1_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy2_L2
    enemy2_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy3_L2
    enemy3_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy4_L2
    enemy4_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy5_L2
    enemy5_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy6_L2
    enemy6_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy7_L2
    enemy7_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy8_L2
    enemy8_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy9_L2
    enemy9_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    global enemy10_L2
    enemy10_L2=tk.PhotoImage(file="enemy_game4_resized.gif")
    #####################################
    global shooter_L2
    shooter_L2=canvas.create_image(0, 650, image=img,anchor='nw',tags="shooter_L2")

    
    global Enemy1_L2
    Enemy1_L2=canvas.create_image(200, 220, image=enemy1,tags="enemy1_L2")
    global Enemy2_L2
    Enemy2_L2=canvas.create_image(500, 340, image=enemy2,tags="enemy2_L2")
    global Enemy3_L2
    Enemy3_L2=canvas.create_image(800, 500, image=enemy3,tags="enemy3_L2")
    global Enemy4_L2
    Enemy4_L2=canvas.create_image(1100, 650, image=enemy4,tags="enemy4_L2")

    
    global Enemy5_L2
    Enemy5_L2=canvas.create_image(1235, 450, image=enemy4,tags="enemy5_L2")
    global Enemy6_L2
    Enemy6_L2=canvas.create_image(1235, 600, image=enemy4,tags="enemy6_L2")
    global Enemy7_L2
    Enemy7_L2=canvas.create_image(350, 220, image=enemy4,tags="enemy7_L2")
    global Enemy8_L2
    Enemy8_L2=canvas.create_image(650, 220, image=enemy4,tags="enemy8_L2")
    global Enemy9_L2
    Enemy9_L2=canvas.create_image(950, 220, image=enemy4,tags="enemy9_L2")
    global Enemy10_L2
    Enemy10_L2=canvas.create_image(120, 650, image=enemy4,tags="enemy10_L2")

    ############################

    global eB1_L2
    eB1_L2=canvas.bbox("enemy1_L2")
    global eB2_L2
    eB2_L2=canvas.bbox("enemy2_L2")
    global eB3_L2
    eB3_L2=canvas.bbox("enemy3_L2")
    global eB4_L2
    eB4_L2=canvas.bbox("enemy4_L2")
    global eB5_L2
    eB5_L2=canvas.bbox("enemy5_L2")
    global eB6_L2
    eB6_L2=canvas.bbox("enemy6_L2")
    global eB7_L2
    eB7_L2=canvas.bbox("enemy7_L2")
    global eB8_L2
    eB8_L2=canvas.bbox("enemy8_L2")
    global eB9_L2
    eB9_L2=canvas.bbox("enemy9_L2")
    global eB10_L2
    eB10_L2=canvas.bbox("enemy10_L2")
    ##############################
    global en1
    en1='present'
    global en2
    en2='present'
    global en3
    en3='present'
    global en4
    en4='present'
    global en5
    en5='present'
    global en6
    en6='present'
    global en7
    en7='present'
    global en8
    en8='present'
    global en9
    en9='present'
    global en10
    en10='present'
    ###############################
    global points_on_shooting
    points_on_shooting=0
    
    
#destroy canvas and change score in score label in main menu if player wants to go bak to main menu
def two_commands():
    canvas.destroy()
    score_lbl=tk.Label(window,text="SCORE: "+str(points_L1+points_L2+points_on_shooting),padx=20,pady=15,fg="#800000",bg="#bffffb")
    score_lbl.config(font=('Helvetica ',15,'italic'))
    score_lbl.place(x=0,y=0)

#scoring mech for L2
def scoring_mechanism_L2():
    global points_L2
    points_L2 = 0
    points_L1 = scoring_mechanism_L1()
    if int(t2) in range(200000,500000):
        points_L2=3000
    if int(t2) in range(500000,800000):
        points_L2=2500
    elif int(t2) in range(800000,1200000):
        points_L2=2000
    elif int(t2) in range(1200000,2000000):
        points_L2=1500
    print(points_L2)
    global total_score
    total_score+=points_L2+points_on_shooting
    #creating a file in append mode to store high scores
    file = open("records.txt","a")
    file.write(str(points_L1+points_L2+points_on_shooting)+"\n")
    file.close()
    global txt
    txt="LEVEL CLEARED\nSCORE:"+str(points_L2+points_on_shooting)
    
    
#main game loop for level 2
def game_loopL2():
    global t2
    t2=timeit.default_timer()
    canvas_thingsL2()
    
    ################################
    #user defined movements of shooter
    def move_left_L2(temp):
        global sB_L2
        sB_L2=canvas.bbox("shooter_L2")
        if sB_L2[2]==1270 and sB_L2[1]==-10:
            scoring_mechanism_L2()
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=two_commands)
            btn_exit=tk.Button(lf1,text="EXIT",padx=50,pady=35,command=window.destroy)
            btn_mainmenu.grid(row=1,column=0)
            btn_exit(row=1,column=1)
            lf1.place(x=500,y=250)
            
        if(sB_L2[0]<=0):
            return
        else:
            if not stopped:
                canvas.move(shooter_L2,-15,0)
            collisiondetection_L2()


    ##########################
    def move_right_L2(temp):
        global sB_L2
        sB_L2=canvas.bbox("shooter_L2")
        if sB_L2[2]==1270 and sB_L2[1]==-10:
            scoring_mechanism_L2()
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=two_commands)
            btn_exit=tk.Button(lf1,text="EXIT",padx=50,pady=35,command=window.destroy)
            btn_mainmenu.grid(row=1,column=0)
            btn_exit.grid(row=1,column=1)
            lf1.place(x=500,y=250)
        if(sB_L2[2]>=canvas.winfo_width()-15):
            return
        else:
            if not stopped:
                canvas.move(shooter_L2,15,0)
            collisiondetection_L2()

    ##########################
    def move_up_L2(temp):
        global sB_L2
        sB_L2=canvas.bbox("shooter_L2")
        if sB_L2[2]==1270 and sB_L2[1]==-10:
            scoring_mechanism_L2()
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=two_commands)
            btn_exit=tk.Button(lf1,text="EXIT",padx=50,pady=35,command=window.destroy)
            btn_mainmenu.grid(row=1,column=0)
            btn_exit.grid(row=1,column=1)
            lf1.place(x=500,y=250)
        if(sB_L2[1]<=0):
            return
        else:
            if not stopped:
                canvas.move(shooter_L2,0,-15)
            collisiondetection_L2()

    ############################
    def move_down_L2(temp):
        global sB_L2
        sB_L2=canvas.bbox("shooter_L2")
        if sB_L2[2]==1270 and sB_L2[1]==-10:
            scoring_mechanism_L2()
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=two_commands)
            btn_exit=tk.Button(lf1,text="EXIT",padx=50,pady=35,command=window.destroy)
            btn_mainmenu.grid(row=1,column=0)
            btn_exit.grid(row=1,column=1)
            lf1.place(x=500,y=250)
        if(sB_L2[3]>=canvas.winfo_height()-15):
            return
        else:
            if not stopped:
                canvas.move(shooter_L2,0,15)
            collisiondetection_L2()
    #binding all keys 
    canvas.bind_all("<Left>",move_left_L2)
    canvas.bind_all("<Right>",move_right_L2)
    canvas.bind_all("<Up>",move_up_L2)
    canvas.bind_all("<Down>",move_down_L2)
    canvas.bind_all("<b>",bosskey)
    canvas.bind_all("<space>",shoot)
    canvas.bind_all("<p>",pause_play)

#destroy canvas and change main score if player wants to go back to main menu after clearing level 1
def TWO_COMMANDS():
    canvas.destroy()
    score_lbl=tk.Label(window,text="SCORE: "+str(points_L1),padx=20,pady=15,fg="#800000",bg="#bffffb")
    score_lbl.config(font=('Helvetica ',15,'italic'))
    score_lbl.place(x=0,y=0)
    
#scoring mech for level 1
def scoring_mechanism_L1():
    global points_L1
    points_L1 = 0
    if int(t1) in range(200000,500000):
        points_L1=3000
    if int(t1) in range(500000,800000):
        points_L1=2500
    elif int(t1) in range(800000,1200000):
        points_L1=2000
    elif int(t1) in range(1200000,2000000):
        points_L1=1500
    global total_score
    total_score=0
    total_score+=points_L1
    global txt
    txt="LEVEL CLEARED\nSCORE:"+str(total_score)
    return points_L1

#the main game loop of L1 goes here
#1)define the movement of shooter with arrow keys
#2)determine the bbox of shooter

def game_loopL1():
    PlaySound("file_example_WAV_10MG.wav",SND_FILENAME | SND_LOOP | SND_ASYNC )
    global t1
    t1=timeit.default_timer()
    canvas_thingsL1()

    #######################
    
    
    #user defined movements of shooter
    def move_left(temp):
        global sB
        sB=canvas.bbox("shooter")
        if sB[2]==1270 and sB[1]==-10:
            scoring_mechanism_L1()
            
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=TWO_COMMANDS)
            btn_L2=tk.Button(lf1,text="GO TO LEVEL 2",padx=50,pady=35,command=game_loopL2)
            btn_mainmenu.grid(row=1,column=0)
            btn_L2.grid(row=1,column=1)
            lf1.place(x=500,y=250)
            canvas.after(2500,lf1.destroy)
            
        if(sB[0]<=0):
            return
        else:
            if not stopped:
                canvas.move(shooter,-15,0)
            collisionDetection()


    ##########################
    def move_right(temp):
        global sB
        sB=canvas.bbox("shooter")
        if sB[2]==1270 and sB[1]==-10:
            scoring_mechanism_L1()
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=TWO_COMMANDS)
            btn_L2=tk.Button(lf1,text="GO TO LEVEL 2",padx=50,pady=35,command=game_loopL2)
            btn_mainmenu.grid(row=1,column=0)
            btn_L2.grid(row=1,column=1)
            lf1.place(x=500,y=250)
            canvas.after(2500,lf1.destroy)
        if(sB[2]>=canvas.winfo_width()-15):
            return
        else:
            if not stopped:
                canvas.move(shooter,15,0)
            collisionDetection()

    ##########################
    def move_up(temp):
        global sB
        sB=canvas.bbox("shooter")
        if sB[2]==1270 and sB[1]==-10:
            scoring_mechanism_L1()
            global lf1
            lf1=tk.LabelFrame(canvas,text="",bg="pink")
            
            winning_lbl=tk.Label(lf1,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=TWO_COMMANDS)
            btn_L2=tk.Button(lf1,text="GO TO LEVEL 2",padx=50,pady=35,command=game_loopL2)
            btn_mainmenu.grid(row=1,column=0)
            btn_L2.grid(row=1,column=1)
            lf1.place(x=500,y=250)
            canvas.after(2500,lf1.destroy)
        if(sB[1]<=0):
            return
        else:
            if not stopped:
                canvas.move(shooter,0,-15) 
            collisionDetection()

    ############################
    def move_down(temp):
        global sB
        sB=canvas.bbox("shooter")
        if sB[2]==1270 and sB[1]==-10:
            scoring_mechanism_L1()
            global lf1
            lf1=tk.LabelFrame(lf1,text="",bg="pink")
            
            winning_lbl=tk.Label(canvas,text=txt,bg="pink",padx=100,pady=50)

            winning_lbl.grid(row=0,column=0,columnspan=2)
            btn_mainmenu=tk.Button(lf1,text="GO TO MAIN MENU",padx=50,pady=35,command=TWO_COMMANDS)
            btn_L2=tk.Button(lf1,text="GO TO LEVEL 2",padx=50,pady=35,command=game_loopL2)
            btn_mainmenu.grid(row=1,column=0)
            btn_L2.grid(row=1,column=1)
            lf1.place(x=500,y=250)
            canvas.after(2500,lf1.destroy)
        if(sB[3]>=canvas.winfo_height()-15):
            return
        else:
            if not stopped:
                canvas.move(shooter,0,15)  
            collisionDetection()
    ##############################
    #my defined movements of enemy
            
    mov1=window.after(50,move_enemy1)
    mov2=window.after(50,move_enemy2)
    mov3=window.after(50,move_enemy3)
    mov4=window.after(50,move_enemy4)

    ###################################
    #all the user defined movements go here (of shooter)
    canvas.bind_all("<Left>",move_left)
    canvas.bind_all("<Right>",move_right)
    canvas.bind_all("<Up>",move_up)
    canvas.bind_all("<Down>",move_down)
    canvas.bind_all("<p>",pause_play)
    canvas.bind_all("<b>",bosskey)

    
    ###############################

#---------------------------------------------------------------------------------------
#canvas that would appear when help button clicked, gives game description
def showhelp():
    def close_canvas():
        help_canvas.destroy()

    
    
    help_canvas= tk.Canvas(window,width=650,height=650,bg="white",highlightthickness=0)
    help_canvas.create_text(1,5,fill="black",anchor="nw",font=("arial",12),text="The game features a character moving across the stage who has to reach end point \nof the stage while avoiding the wizards and killing them.\nThe game has two levels:\n1-In level the character has to avoid all wizards and reach goal.\n2-In level two the character has to kill wizards and as reaching goal.\nUser will get score based on his timely competion and by killing wizards")
    help_canvas.create_text(0,250,fill="black",anchor="nw",font=("arial",12),text="Following will be the controls of the game")
    help_canvas.create_image(300,450,image=arrow_img)
    help_canvas.create_image(600,350,image=p_button)
    help_canvas.create_line(540,290,570,330)
    help_canvas.create_text(520,270,fill="black",anchor="nw",text="pause button")
    help_canvas.create_line(300,320,300,375)

    
    help_canvas.create_text(275,305,fill="black",anchor="nw",text="move up")
    help_canvas.create_line(440,390,400,445)
    help_canvas.create_text(435,370,fill="black",anchor="nw",text="move right")
    help_canvas.create_line(300,520,300,575)
    help_canvas.create_text(275,580,fill="black",anchor="nw",text="move down")
    help_canvas.create_line(160,390,200,445)
    help_canvas.create_text(115,370,fill="black",anchor="nw",text="move left")

    
    help_canvas.create_image(600,470,image=b_button)
    help_canvas.create_line(540,540,570,500)
    help_canvas.create_text(520,540,fill="black",anchor="nw",text="boss key button")
    help_canvas.create_image(115,600,image=space)
    help_canvas.create_line(75,505,115,570)
    help_canvas.create_text(50,490,fill="black",anchor="nw",text="Shooting button")
    tk.Button(help_canvas,image=cross,command=close_canvas).place(x=580,y=0,anchor="nw")
    help_canvas.pack()

#----------------------------------------------------------------------------------------
def showscore():
    #initializing the list to store scores from text doc
    lst_scores=[]
    def close_board():
        new_canvas.destroy()
    new_canvas=tk.Canvas(window, width=300,height=300,bg="white")
    new_canvas.place(x=900,y=40)
    tk.Button(new_canvas,image=cross,command=close_board).place(x=200,y=0)
    file = open("records.txt","r")
    readthefile=file.readlines()

    ############################
    sortedscore = sorted(readthefile,reverse=True)
    for EACHSCORE in sortedscore:
        if EACHSCORE not in lst_scores:
            lst_scores.append(EACHSCORE)            


    ############################
    new_canvas.create_text(5,5,fill="black",anchor="nw",text="The top three scores")
    new_canvas.create_text(5,17,fill="black",anchor="nw",text="Position\t\tscore")
    for line in range(3):
        new_canvas.create_text(5,15+(line+1)*15,fill="black",anchor="nw",text=str(line+1)+"\t\t"+str(lst_scores[line]))



#----------------------------------------------------------------------------------------    
#creating the window

window=tk.Tk(className=" H U N T E R ' S   P A S S A G E")

#window.attributes('-fullscreen', True) # make main window full-screen
background=tk.PhotoImage(file="lightmode_bgResized.png")



#creating front window widgets:score board,start button,help button
lbl=tk.Label(window,image=background)
lbl.place(x=0,y=0,relwidth=1,relheight=1)
#initializing total score variable
total_score=0



###score
score_lbl=tk.Label(window,text="SCORE: "+str(total_score),padx=20,pady=15,fg="#800000",bg="#bffffb")
score_lbl.config(font=('Helvetica ',15,'italic'))
score_lbl.place(x=0,y=0)
###name canvas
name_canvas=tk.Canvas(window,width=500,height=200,bg="#077b8a")
name_canvas.create_text(250,25,text="\n\nHUNTER'S\nPASSAGE",fill="#e75874",font=('Helvetica 50 italic'))
name_canvas.place(x=385,y=150)

###start button
start_btn=tk.Button(window,text="START",padx=25,pady=10,fg="orange",bg="yellow",command=game_loopL1)
start_btn.config(font=('Helvetica ',40,'italic'))
start_btn.place(x=510,y=365)
#leaderboard button
ldrboard_btn=tk.Button(window,text="LEADERBOARD", padx=40,pady=10,fg="#800000",bg="#bffffb",command=showscore)
ldrboard_btn.config(font=('Helvetica ',15,'italic'))
ldrboard_btn.place(x=1040,y=0)


###frame
frame=tk.Frame(window,width=500,height=120)
frame.place(x=385,y=550)
###help button inside frame
arrow_img=tk.PhotoImage(file="arrow-keys (1).png")
p_button= tk.PhotoImage(file="p button.png")
cross = tk.PhotoImage(file="cross.png")
b_button = tk.PhotoImage(file="b button.png")
space = tk.PhotoImage(file="space_key_s.png")

help_btn=tk.Button(frame,text="HELP?",padx=25,pady=10,fg="orange",bg="yellow",command=showhelp)
help_btn.config(font=('Helvetica ',40,'italic'))
help_btn.place(x=0,y=0)
###mode button inside frame
mode_btn=tk.Button(frame,text="MODE",padx=25,pady=10,fg="orange",bg="yellow",command=mode_click)
mode_btn.config(font=('Helvetica ',40,'italic'))
mode_btn.place(x=250,y=0)


iconimage=tk.PhotoImage(file="shooter4_gif_resized.gif")
window.iconphoto(False,iconimage)

#configuring the window

window.geometry("1280x720")
window.resizable(False,False)

window.mainloop()



    
