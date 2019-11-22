from tkinter import *
import cv2
import numpy as np
import os
import _thread
import tkinter as tk
mainWindow = Tk()
mainWindow.title('Machine')

mainWindow.overrideredirect(True)
mainWindow.overrideredirect(False)
mainWindow.attributes('-fullscreen',True)


tk.insert("Hello this is enrol part!!!")


closeButton = Button(mainWindow, text = "CLOSE")
closeButton.configure(command= lambda: mainWindow.destroy())
closeButton.place(x=90,y=530)


mainWindow.mainloop()



