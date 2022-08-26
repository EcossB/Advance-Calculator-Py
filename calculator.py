import re
from tkinter import *
from math import *

#creatio of the class 
class calculator:
    def __init__(self, root):
        self.wind = root
        self.wind.title('Calculator final')

        #creating the screen of the operations and numbers
        self.display = Entry(self.wind, width= 50, background = "gray64", foreground= "white", font=('Times New Romans', 15))
        self.display.grid(row= 0, columnspan= 4, sticky= W+E, ipady=30)
        self.display.focus()


        



        
    
 

        


if __name__ =='__main__':
    root = Tk()
    ventana = calculator(root)
    root.mainloop()