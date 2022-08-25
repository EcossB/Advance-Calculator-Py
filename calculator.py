import collections
from tkinter import *
from tkinter import ttk

#creatio of the class 
class calculator:
    def __init__(self, root):
        self.wind = root
        self.wind.title('Calculator final')

        #creating the screen of the operations and numbers
        self.screen = Text(self.wind, state= "disabled", 
        width= 50, height= 5, background= "gray64", 
        fg="white", font =("Times New Romans", 15))

        self.screen.grid(row = 0, column= 0, columnspan= 4, padx= 5, pady = 5)

        b1= self.create_buttons(7)
        b2 = self.create_buttons(8)
        b3 = self.create_buttons(9)
        b4 = self.create_buttons("DEL", write= False)
        b5 = self.create_buttons(4)
        b6 = self.create_buttons(5)
        b7 = self.create_buttons(6)
        b8 = self.create_buttons(u"\u00f7") 
        b9 = self.create_buttons(1)
        b10 = self.create_buttons(2)
        b11 = self.create_buttons(3)
        b12 = self.create_buttons("x")
        b13 = self.create_buttons(".")
        b14 = self.create_buttons(0)
        b15 = self.create_buttons("+")
        b16 = self.create_buttons("-")
        b17 = self.create_buttons("=", write = False, w= 25, h = 2 )

        #inserting the buttons on the grid
        button = [b1, b2, b3, b4 , b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]
        cont = 0
        for row in range(1,5):
            for column in range(4):
                button[cont].grid(row = row, column = column)
                cont += 1

        button[16].grid(row = 5, column = 0, columnspan = 5)


        #method which create the buttons of the calculator
    def create_buttons(self, value, write = True, w = 9, h = 1):
        return Button(self.wind, text= value, width= w, height= h, font= ("Times New Romans", 15 ))

        


if __name__ =='__main__':
    root = Tk()
    ventana = calculator(root)
    root.mainloop()