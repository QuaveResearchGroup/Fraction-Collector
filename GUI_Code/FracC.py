#!/usr/bin/env python
# coding: utf-8

# In[4]:


### Dependencies 
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import *
import customtkinter as ctk
import pandas as pd
import csv as csv
from datetime import datetime as dt
import os

### Defining root Window 
root = tk.Tk()
root.title('Fraction Collector Method Generator')
root.geometry('800x690')
root.resizable(False, False)

### Window Customization - Frames - Exit button - Version number ##########

### Frame and overall grey back ground

frame1 = ctk.CTkFrame(root,
                    width=800,
                    height=690,
                    corner_radius=12,
                    fg_color = "#363636",
                    bg_color = "#F1F1F1"
                    )
frame1.pack(padx=5, pady=5)

### White banner at top

box1 = ctk.CTkFrame(root,
                    width=770,
                    height=90,
                    corner_radius=10,
                    fg_color = "#F1F1F1",
                    bg_color = "#363636"
                    )
box1.place(relx=0.5, rely=.085, anchor=tk.CENTER)

### Back ground for number of bottles

bkg1 = ctk.CTkFrame(root,
                    width=205,
                    height=85,
                    corner_radius=10,
                    fg_color = "#363636",
                    bg_color = "#F1F1F1"
                    )
bkg1.place(relx=0.15, rely=.085, anchor=tk.CENTER)

### Back ground for timeslice

bkg2 = ctk.CTkFrame(root,
                    width=150,
                    height=85,
                    corner_radius=10,
                    fg_color = "#363636",
                    bg_color = "#F1F1F1"
                    )
bkg2.place(relx=0.378, rely=.085, anchor=tk.CENTER)


### Background for initial Pause time

bkg3 = ctk.CTkFrame(root,
                    width=120,
                    height=85,
                    corner_radius=10,
                    fg_color = "#363636",
                    bg_color = "#F1F1F1"
                    )
bkg3.place(relx=0.553, rely=.085, anchor=tk.CENTER)

### Background for total time

bkg4 = ctk.CTkFrame(root,
                    width=145,
                    height=85,
                    corner_radius=10,
                    fg_color = "#363636",
                    bg_color = "#F1F1F1"
                    )
bkg4.place(relx=0.722, rely=.085, anchor=tk.CENTER)

### Background for path and generate

bkg4 = ctk.CTkFrame(root,
                    width=127,
                    height=85,
                    corner_radius=10,
                    fg_color = "#363636",
                    bg_color = "#F1F1F1"
                    )
bkg4.place(relx=0.898, rely=.085, anchor=tk.CENTER)


### Bottom black band

bottom_band = ctk.CTkFrame(root,
                    width=800,
                    height=40,
                    corner_radius=10,
                    fg_color = "black",
                    bg_color = "black"
                    )
bottom_band.place(relx=0.5, rely=0.965, anchor=tk.CENTER)

###Exit button

def close():
    
    root.destroy()
    root.quit()
                             
close_button = ctk.CTkButton(
    root,
    width=54,
    height=32,
    corner_radius=8,
    fg_color = "#BC4242",
    bg_color = "black",
    text_color = ("black"),
    text_font = ("Arial", 12),
    hover = True,
    text = 'Exit',
    command=close
)

close_button.place(relx=0.933, rely=0.965, anchor=tk.CENTER)

###Version label/ instructions(if any)

version_label = tk.StringVar(value="V1.0")

version_label = ctk.CTkLabel(root,
                               textvariable=version_label,
                               width=100,
                               height=30,
                               fg_color = "black",
                               bg_color = "black",
                               text_font = ("Arial", 10),
                               text_color = "white",
                               corner_radius=8)

version_label.place(relx=0.1, rely=0.965, anchor=tk.CENTER)

instructions = tk.StringVar(value="") #insert intruction label at bottom

instructions = ctk.CTkLabel(root,
                               textvariable=instructions,
                               width=300,
                               height=30,
                               fg_color = "black",
                               bg_color = "black",
                               text_font = ("Block", 8),
                               text_color = "white",
                               corner_radius=8)

instructions.place(relx=0.52, rely=0.961, anchor=tk.CENTER)

### Define Entry Menu - (Number of Bottles) label - entry - output path ##########

###Label - number of bottles

nbottles = tk.StringVar(value="Number of bottles:")

nbottles = ctk.CTkLabel(root,
                               textvariable=nbottles,
                               width=0,
                               height=0,
                               fg_color = "#363636",
                               bg_color = "#363636",
                               text_font = ("Arial BOLD", 12),
                               text_color = "white",
                               corner_radius=8)

nbottles.place(relx=0.123, rely=0.055, anchor=tk.CENTER)

### Entry number of bottles

entrybottles = tk.IntVar()
    
entryb = ctk.CTkEntry(root,
                         textvariable = entrybottles,
                         width=42,
                         height=32,
                         border_width=2,
                         fg_color = "#F1F1F1",
                         bg_color = "#363636",
                         text_font = ("Arial", 11),
                         text_color = "black",
                         corner_radius=8)

entryb.place(relx=0.245, rely=0.06, anchor=tk.CENTER)

### Choose output path button

def select_output():
    
    global path
    path = fd.askdirectory()
                             
pathb = ctk.CTkButton(
    root,
    width=90,
    height=32,
    corner_radius=8,
    text_color = ("black"),
    text_font = ("Arial", 12),
    fg_color = "#548FB9",
    bg_color = "#363636",
    hover = True,
    text = 'Choose Path',
    command=select_output
)

pathb.place(relx=0.899, rely=0.06, anchor=tk.CENTER)

### Wait on Waste bottle entry before going to first bottle? chops off front of chromatogram

### Waste text option

towaste = tk.StringVar(value="Initial Pause:")

towaste = ctk.CTkLabel(root,
                               textvariable=towaste,
                               width=0,
                               height=0,
                               fg_color = "#363636",
                               bg_color = "#363636",
                               text_font = ("Arial Bold", 12),
                               text_color = "white",
                               corner_radius=8)

towaste.place(relx=0.555, rely=0.055, anchor=tk.CENTER)

### Secondary text

optional = tk.StringVar(value="(min)")

optional = ctk.CTkLabel(root,
                               textvariable=optional,
                               width=50,
                               height=30,
                               fg_color = "#363636",
                               bg_color = "#363636",
                               text_font = ("Arial Bold", 12),
                               text_color = "white",
                               corner_radius=8)

optional.place(relx=0.516, rely=0.109, anchor=tk.CENTER)

### optional waste pause entry

global wastetime

wastetime = tk.DoubleVar()

entrywastetime = ctk.CTkEntry(root,
                         textvariable = wastetime,
                         width=50,
                         height=30,
                         border_width=2,
                         fg_color = "#F1F1F1",
                         bg_color = "#363636",
                         text_font = ("Arial", 11),
                         text_color = "black",
                         corner_radius=8)

entrywastetime.place(relx=0.585, rely=0.11, anchor=tk.CENTER)

### Update all bottle entries function - label - entry ###########################################

### Label

alltime = tk.StringVar(value="Timeslices (min):")

alltime = ctk.CTkLabel(root,
                               textvariable=alltime,
                               width=0,
                               height=0,
                               fg_color = "#363636",
                               bg_color = "#363636",
                               text_font = ("Arial Bold", 12),
                               text_color = "white",
                               corner_radius=8)

alltime.place(relx=0.375, rely=0.055, anchor=tk.CENTER)

### Entry updates all bottles with time in minutes

global entryalltime

entryalltime = tk.DoubleVar()

entryalltime = ctk.CTkEntry(root,
                         textvariable = entryalltime,
                         width=55,
                         height=30,
                         border_width=2,
                         fg_color = "#F1F1F1",
                         bg_color = "#363636",
                         text_font = ("Arial", 11),
                         text_color = "black",
                         corner_radius=8)

entryalltime.place(relx=0.43, rely=0.11, anchor=tk.CENTER)

### Total run time - adds all bottle time entries in minutes and gets their variable to use for code generation #####################################

totaltime = tk.StringVar(value="Total time (min):")

totaltime = ctk.CTkLabel(root,
                               textvariable=totaltime,
                               width=0,
                               height=0,
                               fg_color = "#363636",
                               bg_color = "#363636",
                               text_font = ("Arial Bold", 12),
                               text_color = "white",
                               corner_radius=8)

totaltime.place(relx=0.723, rely=0.055, anchor=tk.CENTER)

### Creates Frame - sets definitions, Defines population of workspace with correct number of bottles - defines clear function ###############################

def clearframe():
            
    global framebot
            
    framebot.destroy()
    
    entryalltime = None
    
Label_Positions = pd.read_csv("Label_Positions.csv")

def bottles():
    
    global framebot
    
    try:
        framebot.destroy()
    except:
        arbitrary = 1
        
    
    nbot = int(entrybottles.get())

    framebot = ctk.CTkFrame(frame1,
                width=800,
                height=630,
                corner_radius=12,
                fg_color = "#F1F1F1",
                bg_color = "#F1F1F1"
                )
    framebot.pack(padx=10, pady=20)
    
### Dark band separating entries from bottles

    top_band = ctk.CTkFrame(framebot,
                        width=770,
                        height=10,
                        corner_radius=10,
                        fg_color = "#363636",
                        bg_color = "#363636"
                        )
    top_band.place(relx=0.5, rely=0.129, anchor=tk.CENTER)

    counter = 1
    
    while counter <= nbot:

        p = counter - 1
        q = counter
        
        Tposx = Label_Positions.loc[p]['textx']
        Tposy = Label_Positions.loc[p]['texty']
        Eposx = Label_Positions.loc[p]['ex']
        Eposy = Label_Positions.loc[p]['ey']

###Texts


        (globals()['text%s' % q]) = tk.StringVar(value = (counter))

        globals()['tbot%s' % q] = ctk.CTkLabel(framebot,
                               textvariable= (globals()['text%s' % q]),
                               width=30,
                               height=30,
                               fg_color = "#F1F1F1",
                               bg_color = "#F1F1F1",
                               text_font = ("Arial", 11),
                               text_color = "black",
                               corner_radius=8)

        (globals()['tbot%s' % q]).place(x=Tposx, y=Tposy)

###Entries

        (globals()['bot%s' % q]) = tk.DoubleVar()


        (globals()['ebot%s' % q]) = ctk.CTkEntry(framebot,
                         textvariable = (globals()['bot%s' % q]),
                         width=45,
                         height=45,
                         border_width=2,
                         fg_color = "#F1F1F1",
                         bg_color = "#F1F1F1",
                         text_font = ("Arial", 10),
                         text_color = "black",
                         corner_radius=8)

        (globals()['ebot%s' % q]).place(x=Eposx, y=Eposy)
        

        counter = int(counter)
        counter = counter + 1
        
##Clear Frame button

        def clear():
            
            framebot.destroy()
        
        clear_button = ctk.CTkButton(
            root,
            width=65,
            height=30,
            corner_radius=8,
            text_color = ("black"),
            text_font = ("Arial", 12),
            fg_color = "#BC4242",
            bg_color = "#363636",
            hover = True,
            text = 'Clear',
            command=clear
        )

        clear_button.place(relx=0.17, rely=0.11, anchor=tk.CENTER)
        
###Populate workspace button with correct number of bottles - enter/clear button - Update the entries with alltime slices - update/reset #####################

### Enter button

enter_button = ctk.CTkButton(
    root,
    width=68,
    height=30,
    corner_radius=8,
    text_color = ("black"),
    text_font = ("Arial", 12),
    fg_color = "#8FC983",
    bg_color = "#363636",
    hover = True,
    text = 'Enter',
    command=bottles
)

enter_button.place(relx=0.075, rely=0.11, anchor=tk.CENTER)

### Update all time slices button - exceptions - update #######################################

def updatebot ():
    nbot = int(entrybottles.get())
    counter2 = 1
    while counter2 <= nbot:
        try:
            (globals()['ebot%s' % counter2]).delete(0,END)
            (globals()['ebot%s' % counter2]).insert(0,(str(entryalltime.get())))
        except (NameError, TclError) as error:
            arbitrary = 1
        counter2 = counter2 + 1
    
### Apply button ################################################
apply_button = ctk.CTkButton(
    root,
    width=68,
    height=30,
    corner_radius=8,
    text_font = ("Arial", 12),
    text_color = ("black"),
    fg_color = "#8FC983",
    bg_color = "#363636",
    hover = True,
    text = 'Apply',
    command=updatebot
)

apply_button.place(relx=0.34, rely=0.11, anchor=tk.CENTER)

### Check button - grabs all bottle on screen variables and their time #############################

def check ():
        
    nbot = (entrybottles.get())
    botsum = 0
    botdict = {}
    botdict.clear()
    counter3 = 1
    
    while counter3 <= nbot:
        
        (globals()['bval%s' % counter3])= (globals()['bot%s' % counter3]).get()
        globals()['b%s' % counter3] = 'b'+str(counter3)
        botdict[str(globals()['b%s' % counter3])] = (globals()['bval%s' % counter3])
        counter3 = counter3 + 1

    botsum = sum(botdict.values())
    wt = float(wastetime.get())
    botsum = round((botsum + wt) ,2)
    
    placeholder = tk.DoubleVar()
    
    timecheck = ctk.CTkEntry(root,
                         textvariable = placeholder,
                         width=56,
                         height=32,
                         border_width=2,
                         fg_color = "#F1F1F1",
                         bg_color = "#363636",
                         text_font = ("Arial", 11),
                         text_color = "black",
                         corner_radius=8)
        
    timecheck.place(relx = 0.77, rely=0.112, anchor = tk.CENTER)
    
    timecheck.delete(0,END)
    timecheck.insert(0,(str(botsum)))
    
check_button = ctk.CTkButton(
    root,
    width=52,
    height=32,
    corner_radius=8,
    text_font = ("Arial", 12),
    text_color = ("black"),
    fg_color = "#8FC983",
    bg_color = "#363636",
    hover = True,
    text = 'Check',
    command=check
)

check_button.place(relx=0.685, rely=0.111, anchor=tk.CENTER)

### Clicking gnerate opens window to input filename text ###################

def generatefilename ():
        
    global name
    
    global root2
    
    root2 = Toplevel(root)
    root2.title('File Namer')
    root2.geometry('300x100')
    root2.resizable(False, False)
    
    
    ###Frame
    
    framename = ctk.CTkFrame(root2,
                    width=300,
                    height=100,
                    corner_radius=12,
                    fg_color = "#363636",
                    bg_color = "#F0F0F0"
                    )
    framename.pack(padx=20, pady=20)
    
    ###Button
    
    enter2 = ctk.CTkButton(
        framename,
        width=30,
        height=30,
        corner_radius=8,
        text_font = ("Arial", 11),
        text_color = ("black"),
        fg_color = "#8FC983",
        bg_color = "#363636",
        hover = True,
        text = 'Enter',
        command= generate
        )

    enter2.place(relx=0.84, rely=0.5, anchor=tk.CENTER)
    
    ### Text entry for file name
    
    global filename
    
    filename = StringVar()
    
    nameentry = ctk.CTkEntry(framename,
             textvariable = filename,
             width=160,
             height=30,
             border_width=2,
             fg_color = "#F1F1F1",
             bg_color = "#363636",
             text_font = ("Arial", 11),
             text_color = "black",
             corner_radius=8,
             placeholder_text = ("Enter Filename")
    )
                             
    nameentry.place(relx=0.35, rely=0.5, anchor=tk.CENTER)
    
### Defines the gnerate code function - grabs all varialbles as is for reduncay if check button is not clicked again after minor changes are made ##########

### defining code generator

def generate():
    
    ### Makes dictionary again in case the check button is not clicked (redundancy)
    nbot = (entrybottles.get())
    botsum = 0
    botdict = {}
    botdict.clear()
    counter3 = 1
    
    while counter3 <= nbot:
        
        (globals()['bval%s' % counter3])= (globals()['bot%s' % counter3]).get()
        globals()['b%s' % counter3] = 'b'+str(counter3)
        botdict[str(globals()['b%s' % counter3])] = (globals()['bval%s' % counter3])
        counter3 = counter3 + 1

### Reads the positions of bottle labels and sets index to 'positions' to refence the bottle position (bp) - grabst time for file naming

    dtime = dt.now()
    dtime = dtime.strftime('%Y-%m-%d_%H%M%S')
    dtime = str(dtime)
    df = pd.read_csv("FC_Bottle_Positions_80.csv")
    df=df.set_index('position') 
    wt = float(wastetime.get())
    n = str(filename.get())
    
### Sets initial Gcode commands makes file if not already made - names it as entry + _datetime so two files cannot have the same name

    f = open(path+"/"+n+"_"+dtime+".gcode", 'a')
    f.write(";Flavor:Marlin" + "\n")
    f.write("G28" +"\n")
    f.write("G21" + "\n")
    f.write("M203 X300 Y300" + "\n") #Sets max feedrate to 200 mm/sec (or 12,000 mm/min for "G0 F" commands)
    f.write("M201 X2000 Y2000" + "\n") #Sets Max acceleration to 2000 mm/sec^2
    f.write("M204 X2000 Y2000" + "\n") #Acceleration setting
    f.write("M205 X20 Y20" + "\n") #Jerk setting 
    f.write("G92 X0 Y0" + "\n")

### Move to 0, setting initial speed F10,000 mm/min to be followed by subsequent lines

    f.write("G0 F18000 X0" + "\n") 

### Pause until you click to inject

    f.write("M0 Click When Injecting" + "\n")

### Optional pause at waste bottle for x number of seconds of method beofore moving to bottle 1
    
    if wt > 0:
        
        wt = round(wt*60, 2)
        wt = str(wt)
        f.write("G04 S"+ wt + "\n")

###begin bottle 1 and loop
    
    c = 1
    
    while 1 <= c <= nbot:
    
        c = str(c)
        px = df.loc['bp'+c]['x']
        py = df.loc['bp'+c]['y']
        px = str(px)
        py = str(py)
        f.write("G0 X"+px+" Y"+py+"\n")
        t = float(botdict['b'+c])
        t = round(((t*60) - 0.622), 3) ### subtraction of time reduces each pause to compensate for the lag in command read time and acceleration of nozzle.
        t = str(t)
        f.write("G04 S"+ t + "\n")
        c = int(c)
        c = c + 1
        
### End of run homing path -

    if (2 <= nbot <= 10) or (22 <= nbot <= 30) or (42 <= nbot <= 50) or (62 <= nbot <= 70):  
        py = float(py) + 68
        py = str(py)
        f.write("G0 Y"+py+"\n")
        f.write ("G0 F18000 X1"+"\n")
        f.write ("G0 F6000 Y1"+"\n")
    else:
        f.write ("G0 F18000 X1"+"\n")
        f.write ("G0 F6000 Y1"+"\n")
    
### Homes to funnel

    f.write("G28" +"\n")

### Close file

    f.close()
    root2.destroy()
    
### Generate Gcode button ##########

generatebutton = ctk.CTkButton(
    root,
    width=112,
    height=32,
    corner_radius=8,
    text_font = ("Arial", 13),
    text_color = ("black"),
    fg_color = "#8FC983",
    bg_color = "#363636",
    hover = True,
    text = '  Generate  ',
    command=generatefilename
)

generatebutton.place(relx=0.899, rely=0.115, anchor=tk.CENTER)

root.mainloop()


# In[ ]:




