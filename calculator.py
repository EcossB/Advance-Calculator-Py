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

        #Creating buttons and inserting in the app
        Button(self.wind, text="1", width= 9, height= 1).grid(row=1, column=0, sticky= W+E)
        Button(self.wind, text="2", width= 9, height= 1).grid(row=1, column=1, sticky= W+E)
        Button(self.wind, text="3", width= 9, height= 1).grid(row=1, column=2, sticky= W+E)

        Button(self.wind, text="4", width= 9, height= 1).grid(row=2, column=0, sticky= W+E)
        Button(self.wind, text="5", width= 9, height= 1).grid(row=2, column=1, sticky= W+E)
        Button(self.wind, text="6", width= 9, height= 1).grid(row=2, column=2, sticky= W+E)

        Button(self.wind, text="7", width= 9, height= 1).grid(row=3, column=0, sticky= W+E)
        Button(self.wind, text="8", width= 9, height= 1).grid(row=3, column=1, sticky= W+E)
        Button(self.wind, text="9", width= 9, height= 1).grid(row=3, column=2, sticky= W+E)


        
        #Button(self.wind, text="0", width= 9, height= 1).grid(row=1, column=0, sticky= W+E)



        



        
    
 

        


if __name__ =='__main__':
    root = Tk()
    ventana = calculator(root)
    root.mainloop()