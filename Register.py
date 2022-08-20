from tkinter import * 
from tkinter import ttk
import sqlite3

class anime_interface:
    def __init__(self, root):
        self.window = root
        self.window.title('Gestionar personajes')
        
        #creacion del contenedor
        frame1 = LabelFrame(self.window,text= 'Add a new character')
        frame1.grid(row = 0, column= 0, columnspan=3, pady= 20)

if __name__=='__main__':
    root = Tk()
    open_app = anime_interface(root)  
    root.mainloop()