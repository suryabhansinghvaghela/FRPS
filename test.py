import guifunctions as gfx
import sqlsetup as sql
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageTk, ImageFont

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

#!/usr/bin/env python3

import product
from product import Product
import tkinter as tk
from tkinter import ttk, messagebox
import sqlsetup as sql
from PIL import Image, ImageDraw, ImageTk, ImageFont





  
class Store(ttk.Frame):
	def __init__(self, parent):
		ttk.Frame.__init__(self, parent, padding="0 0 0 0")
		#style=ttk.Style()
		#style.configure()
		self.pack()
		data_status = sql.createInventory()
		gfx.initGui(self,data_status)
		
		
		
 #######################################################     
if __name__ == "__main__":
    mainWindow = tk.Tk()
    mainWindow.title("Store")
    


#image_file = io.BytesIO(base64.b64decode(BASE64_BACKGROUND))
    image = Image.open("menu.png")
    mainWindow.overrideredirect(True)
    mainWindow.overrideredirect(False)
    mainWindow.attributes('-fullscreen',True)
    draw = ImageDraw.Draw(image)
    mainFrame = Frame(mainWindow)
    photoimage = ImageTk.PhotoImage(image)
    Label(mainWindow, image=photoimage).place(x=-1,y=-1)
    Store(mainWindow)
    mainWindow.mainloop()

