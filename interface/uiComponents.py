#interface/uiComponents

import tkinter as tk

#Global styles
FONTHEADER = ("Arial", 16, "bold")
FONTLABEL = ("Arial", 13)
FONTBUTTON = ("Arial", 12, "bold")
BGCOLOR = "#F8F8F8"
BUTTONCOLOR = "#64A2E9"
BUTTONTEXTCOLOR = "#F8F8F8" 

#Defualt Padding
PADX = 5
PADY = 5

#Reusable Components 
def createLabel(parent, text, font=FONTLABEL, padx=PADX, pady=PADY):
    return tk.Label(parent, text=text, font=font, padx=padx, pady=pady)

def createEntry(parent, show=None, width=20, font=FONTLABEL):
    return tk.Entry(parent, show=show, width=width, font=font)

def createButton(parent, text, font=FONTBUTTON, command=None, bg=BGCOLOR, fg=BUTTONTEXTCOLOR, width=15):
    return tk.Button(parent, text=text, font=font, command=command, bg=bg, fg=fg, width=width)
