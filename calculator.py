from ast import Global
import re
from tkinter import *
from math import *

i = 0
#creatio of the class 
class calculator:
    def __init__(self, root):
        self.wind = root
        self.wind.title('Calculator final')

        

        #creating the screen of the operations and numbers
        display = Entry(self.wind, width= 50, background = "gray64", foreground= "white", font=('Times New Romans', 15))
        display.grid(row= 0, columnspan= 6, sticky= W+E, ipady=30)
        display.focus()

        #Creating buttons and inserting in the app
        Button(self.wind, text="1", width= 9, height= 3, command=lambda:get_numbers(1)).grid(row=1, column=0, sticky= W+E)
        Button(self.wind, text="2", width= 9, height= 3, command=lambda:get_numbers(2)).grid(row=1, column=1, sticky= W+E)
        Button(self.wind, text="3", width= 9, height= 3, command=lambda:get_numbers(3)).grid(row=1, column=2, sticky= W+E)

        Button(self.wind, text="4", width= 9, height= 3, command=lambda:get_numbers(4)).grid(row=2, column=0, sticky= W+E)
        Button(self.wind, text="5", width= 9, height= 3, command=lambda:get_numbers(5)).grid(row=2, column=1, sticky= W+E)
        Button(self.wind, text="6", width= 9, height= 3, command=lambda:get_numbers(6)).grid(row=2, column=2, sticky= W+E)

        Button(self.wind, text="7", width= 9, height= 3, command=lambda:get_numbers(7)).grid(row=3, column=0, sticky= W+E)
        Button(self.wind, text="8", width= 9, height= 3, command=lambda:get_numbers(8)).grid(row=3, column=1, sticky= W+E)
        Button(self.wind, text="9", width= 9, height= 3, command=lambda:get_numbers(9)).grid(row=3, column=2, sticky= W+E)

        Button(self.wind, text="C", width= 9, height= 3).grid(row=4, column=0, sticky= W+E)
        Button(self.wind, text="0", width= 9, height= 3).grid(row=4, column=1, sticky= W+E)
        Button(self.wind, text="%", width= 9, height= 3).grid(row=4, column=2, sticky= W+E)
        
        #operations buttons
        Button(self.wind, text="+", width= 9, height= 3).grid(row=1, column=3, sticky= W+E)
        Button(self.wind, text="-", width= 9, height= 3).grid(row=2, column=3, sticky= W+E)
        Button(self.wind, text="*", width= 9, height= 3).grid(row=3, column=3, sticky= W+E)
        Button(self.wind, text="/", width= 9, height= 3).grid(row=4, column=3, sticky= W+E)

        Button(self.wind, text=u"\u232B", width= 9, height= 3).grid(row=1, column=4, sticky= W+E, columnspan= 2)
        Button(self.wind, text="EXP", width= 9, height= 3).grid(row=2, column=4, sticky= W+E)
        Button(self.wind, text="^2", width= 9, height= 3).grid(row=2, column=5, sticky= W+E)
        Button(self.wind, text="(", width= 9, height= 3).grid(row=3, column=4, sticky= W+E)
        Button(self.wind, text=")", width= 9, height= 3).grid(row=3, column=5, sticky= W+E)
        Button(self.wind, text="=", width= 9, height= 3).grid(row=4, column=4, sticky= W+E, columnspan= 2)

        def get_numbers(n):
            global i 
            display.insert(i, n)
            i+=1
        

        



        
    
 

        


if __name__ =='__main__':
    root = Tk()
    ventana = calculator(root)
    root.mainloop()