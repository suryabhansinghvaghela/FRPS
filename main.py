#main file containing main interface
import io
import base64
import cv2, os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
import pickle
import sqlite3
import matplotlib.pyplot as plt
import numpy as np

try:
    from Tkinter import Tk, Label, Entry, Toplevel, Canvas
except ImportError:
    from tkinter import Tk, Label, Entry, Toplevel, Canvas

from PIL import Image, ImageDraw, ImageTk, ImageFont


mainWindow = tk.Tk()

#image_file = io.BytesIO(base64.b64decode(BASE64_BACKGROUND))
image = Image.open("full.png")



#width, height = 800,600

# prevent window resizing, the size of the window is the same as size of the background image
#mainWindow.resizable(width=False, height=False)
#mainWindow.geometry("%sx%s"%(width, height))

mainWindow.overrideredirect(True)
mainWindow.overrideredirect(False)
mainWindow.attributes('-fullscreen',True)


draw = ImageDraw.Draw(image)

#text_x = 100
#text_y = 200


text = "Face Recognition Payment System"




white = "#ffffff"
cream = "#fffdd0"
maxWidth = 1000
maxHeight = 600

# Graphics window
#mainWindow = tk.Tk()
#mainWindow.configure(bg=cream)
#mainWindow.geometry('%dx%d+%d+%d' % (maxWidth, maxHeight, 0, 0))
#mainWindow.resizable(0, 0)
# mainWindow.overrideredirect(1)



mainFrame = Frame(mainWindow)
#mainFrame.place(x=0, y=0)
#mainFrame.grid()


def enrol():
	
	os.system('python detect_face.py')
	#os.system('python enrol.py')

def starter():
	
	#os.system('python recognition.py')
	os.system('python recognition.py')





# Use here a nice ttf font
font = ImageFont.truetype("arial.ttf",32)
width_text, height_text = font.getsize(text)
draw.text((480, 30), text, fill="white", font=font)





#line="---------------------------------------------"
#draw.text((600, 100), line, fill="white", font=font)



#width_text, height_text = draw.textsize(text)
#draw.text((684 , 100), text, fill="black")



photoimage = ImageTk.PhotoImage(image)
Label(mainWindow, image=photoimage).place(x=-2,y=-2)

#Instanciating buttons

# load = Image.open("linev.png")
# render = ImageTk.PhotoImage(load)
# img = Label(mainWindow, image=render)
# img.image = render
# img.place(x=-2, y=2)


# load = Image.open("linev.png")
# render = ImageTk.PhotoImage(load)
# img = Label(mainWindow, image=render)
# img.image = render
# img.place(x=2, y=75)


# load = Image.open("linev.png")
# render = ImageTk.PhotoImage(load)
# img = Label(mainWindow, image=render)
# img.image = render
# img.place(x=-2, y=750)

# load = Image.open("lineh.png")
# render = ImageTk.PhotoImage(load)
# img = Label(mainWindow, image=render)
# img.image = render
# img.place(x=2, y=-2)

# load = Image.open("lineh.png")
# render = ImageTk.PhotoImage(load)
# img = Label(mainWindow, image=render)
# img.image = render
# img.place(x=1346, y=-2)



load = Image.open("dpn.jpg")
render = ImageTk.PhotoImage(load)
img = Label(mainWindow, image=render)
img.image = render
img.place(x=483, y=130)




entry_pady = 100
b1=Button(mainWindow, text = "Close",command= lambda: mainWindow.destroy())
b1.place(x=800, y=450 + 0 +0)



b2=Button(mainWindow, text = "Enroll", command=enrol)
b2.place(x=683, y=450 + 0 +0)

b3=Button(mainWindow, text = "Login", command= starter)
b3.place(x=566, y=450 + 0 +0)





mainWindow.mainloop()

