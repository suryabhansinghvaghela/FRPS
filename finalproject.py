#!/usr/bin/env python3

import guifunctions as gfx
import sqlsetup as sql
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageDraw, ImageTk, ImageFont

#######################################################

  
class Store(ttk.Frame):
    
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        ttk.overrideredirect(True)
        ttk.overrideredirect(False)
		
        self.pack()
        data_status = sql.createInventory()
        gfx.initGui(self,data_status)
 #######################################################     
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Store")
    root.geometry("900x600")
    root.iconbitmap('icons\shop.ico')
    Store(root)
    root.mainloop()
    
    
