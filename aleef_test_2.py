import tkinter as tk
from tkinter import font
from main import *

# Vars init
cylinder = charger_cylindre("cylinderWiki.txt")
clickedItems = []
row = 0
finished = False

# Creating main tkinter window/toplevel 
root = tk.Tk() 

# Font
arial = font.Font(family='Arial', size=48, weight='bold')

def displayCylinder(frame, cylinder, i):
    global row
    for j in range(len(cylinder[i])):
        text = tk.Label(frame, text=cylinder[i][j], font=arial)
        text.grid(row=j, column=row)

def displayCylinders(frame, cylinder):
    global row
    if len(clickedItems) != len(cylinder):
        for i in range(len(cylinder)): # Change made here
            row += 1
            displayCylinder(frame, cylinder, i)
    else:
        for i in clickedItems:
            row += 1
            displayCylinder(frame, cylinder, i)

def rotateCylinder(cylinder,i,up):
    cylinder[clickedItems[i]] = cylinder[clickedItems[i]][1:] + cylinder[clickedItems[i]][0] if up else cylinder[clickedItems[i]][-1] + cylinder[clickedItems[i]][:-1]

def rotateCylinders(frame, cylinder):
    global clickedItems
    for i in range(len(cylinder)):
        up_button = tk.Button(frame, text='\u2191', command=lambda i=i: rotateCylinder(cylinder, i, True))
        up_button.grid(row=10, column=i) # adjust row and column as per your need
        down_button = tk.Button(frame, text='\u2193', command=lambda i=i: rotateCylinder(cylinder, i, False))
        down_button.grid(row=11, column=i) # adjust row and column as per your need

def displayAll():
    frame = tk.Frame(root)
    frame.pack()
    displayCylinders(frame, cylinder)
    rotateCylinders(frame, cylinder)
    root.mainloop()

# Call main loop
displayAll()
