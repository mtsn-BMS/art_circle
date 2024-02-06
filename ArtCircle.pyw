# ArtCircle - Circle Moving Art
#Terrible English Sorry plz

### Module Import ###
import pygame           #DRAW & MOVE
import random           #Circle Random
import time             #Capture FileName
import tkinter as tk    #GUI
from tkinter import ttk

### Important Value ###
running=True            #Exit Check

### Function ###
def capture():                                                          #Capture Screen
    getscreen = pygame.display.get_surface()                            #Get Screen
    stamptime=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())      #Get Time for Filename
    pygame.image.save(getscreen, "./%s.png"%stamptime)                  #Capture & Save
        
def draw(winx,winy,ballnum,fps,getfont,fntsize,word):                                   #Core
    pygame.init()                                                       #Initialize
    screen = pygame.display.set_mode([winx, winy],pygame.RESIZABLE)     #SetWindow(Resizable Now)
    ## Set Values
    keep_going = True   #Draw Circulation
    BLACK = (0,0,0)     #Black Color
    CapReady=0          #Space Key Check

    # Colors,Positions,Sizes and Speeds randomlist create
    colors = [0]*ballnum
    locations = [0]*ballnum
    sizes = [0]*ballnum
    speeds = [0]*ballnum

    timer=pygame.time.Clock()   #For FPS Limit

    #Colors,Positions,Sizes and Speeds randomize
    for n in range(ballnum):
        colors[n] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        locations[n] = (random.randint(0,winx), random.randint(0,winy))
        sizes[n] = random.randint(10, 200)
        speeds[n] = random.uniform(30/fps,180/fps)

    while keep_going:                       #Core Circulation
        info=pygame.display.Info()          #Get Realtime Window Size
        infox=info.current_w
        infoy=info.current_h
        
        for event in pygame.event.get():    #Core Exit Check
            if event.type == pygame.QUIT: 
                keep_going = False
        
        for n in range(ballnum):            #Circle Move
            pygame.draw.circle(screen, colors[n], locations[n], sizes[n])
            new_x = locations[n][0] + speeds[n]
            new_y = locations[n][1] + speeds[n]
            if new_x - sizes[n] > infox:            #Edge Check
                new_x -= infox + (sizes[n]) * 2
                new_y = random.randint(0,infoy)   #random y
            if new_y - sizes[n] > infoy:
                new_y -= infoy + (sizes[n]) * 2
                new_x = random.randint(0,infox)   #random x
            locations[n] = (new_x, new_y)           #Refresh Locations
            
        #Text Show
        font=pygame.font.SysFont(getfont,fntsize)    #Get Fontlist
        text=font.render(word,True,(255,255,255))    #Write Word
        text_w,text_h=text.get_size()                #Get Word Size
        screen.blit(text,(infox/2-text_w/2,infoy/2-text_h/2))    #Put Word in Center
        
        #Key Check
        key_tuple=pygame.key.get_pressed()  #Get Pressed Key
        if key_tuple[pygame.K_SPACE]:       #Scaned Space Key Down
            CapReady=1                      #SIGN OF SPACE PRESSED
        else:                               #Space Not Pressed
            if CapReady == 1:               #Check Statue
                    capture()               #Start Capture
                    CapReady=0              #Reset KeyPress Status
            
        pygame.display.update()             #Update Draw
        screen.fill(BLACK)                  #Clean Trails
        timer.tick(fps)                     #fps
   
    pygame.quit()                           #Exit Core
    window.deiconify()                      #Show Control Window
def start():                                #Start Button
    winx=int(entry1.get())                  #Set Get Values
    winy=int(entry2.get())
    ballnum=int(entry3.get())
    fps=int(entry4.get())
    getfont=entry5.get()
    fntsize=int(entry6.get())
    word=entry7.get()
    window.withdraw()                       #Hide Control Window
    draw(winx,winy,ballnum,fps,getfont,fntsize,word)        #Startup Core
    
### Control Window & Main Circulation ###

while running:    #Exit Check
    #get font
    FontList=pygame.font.get_fonts()
    
    ##init
    window=tk.Tk()  #Main Window
    window.title('Art Circle v0.1 (powered by MatrixSunny)')
    window.resizable(0,0)   #unresizable
    ##Line
    
    ##Label Area
    lab1=tk.Label(window,text="Width:")
    lab2=tk.Label(window,text="Height:")
    lab3=tk.Label(window,text="Number of Ball:")
    lab4=tk.Label(window,text="FPS Limit:")
    lab5=tk.Label(window,text="Font:")
    lab6=tk.Label(window,text="Font Size:")
    lab7=tk.Label(window,text="Text:")
    labX=tk.Label(window,text="(You can capture it by Press Space Key!)")
    labZ=tk.Label(window,text="My GUI design is very terrible,sorry.") 
    lab1_=tk.Label(window,text="(NOT RECOMMENDED BIGGER THAN YOU SCREEN RESOLUTION)")
    lab2_=tk.Label(window,text="(NOT RECOMMENDED BIGGER THAN YOU SCREEN RESOLUTION)")
    lab4_=tk.Label(window,text="(DON'T TOO HIGH)")
    ##label grid
    lab1.grid(row=0,sticky='e')    #Width
    lab2.grid(row=1,sticky='e')    #Height
    lab3.grid(row=2,sticky='e')    #Ball
    lab4.grid(row=3,sticky='e')    #FPS
    lab5.grid(row=4,sticky='e')    #Font
    lab6.grid(row=5,sticky='e')    #FontSize
    lab7.grid(row=6,sticky='e')    #Text
    labX.grid(row=9,column=2,sticky='w')    #tip1
    labZ.grid(row=99,column=2,sticky='w')    #tip2
    lab1_.grid(row=0,column=2,sticky='w')
    lab2_.grid(row=1,column=2,sticky='w')
    lab4_.grid(row=3,column=2,sticky='w')
    ##InputBox Default Value
    def1=tk.StringVar(window)
    def2=tk.StringVar(window)
    def3=tk.StringVar(window)
    def4=tk.StringVar(window)
    def5=tk.StringVar()
    def6=tk.StringVar(window)
    def1.set('1280')
    def2.set('720')
    def3.set('100')
    def4.set('60')
    def6.set('60')
    ##Inputbox area
    entry1=tk.Spinbox(window,from_=0,to=999999,textvariable=def1)
    entry2=tk.Spinbox(window,from_=0,to=999999,textvariable=def2)
    entry3=tk.Spinbox(window,from_=0,to=1000,textvariable=def3)
    entry4=tk.Spinbox(window,from_=1,to=1000,textvariable=def4)
    entry5=ttk.Combobox(window,textvariable=def5)
    entry5["values"]=FontList
    entry5["state"]="readonly"
    entry5.current(0)
    entry6=tk.Spinbox(window,from_=1,to=512,textvariable=def6)
    entry7=tk.Entry(window)
    ##grid
    entry1.grid(row=0,column=1)
    entry2.grid(row=1,column=1)
    entry3.grid(row=2,column=1)
    entry4.grid(row=3,column=1)
    entry5.grid(row=4,column=1)
    entry6.grid(row=5,column=1)
    entry7.grid(row=6,column=1)
    ##button area
    button1=tk.Button(window,text='Start!',command=start)
    button1.grid(row=9,column=1)
    #Message Loop
    window.mainloop()
    running=False       #Control Window Exit, Circulation End, Program Exit
