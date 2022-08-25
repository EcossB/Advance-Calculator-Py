from tkinter import *

#creatio of the class 
class calculator:
    def __init__(self, root):
        self.wind = root
        self.wind.title('Calculator final')

        #creating the screen of the operations and numbers
        self.screen = Text(self.wind, state= "disabled", 
        width= 50, height= 5, background= "gray64", 
        fg="white", font =("Times New Romans", 15))

        self.screen.grid(row = 0, column= 0, sticky= W + E)


        #method which create the buttons of the calculator
        def create_buttons(self, value, write = True, w = 9, h = 1):
            return Button(self.wind, text= value, width= w, height= h, font= ("Times New Romans", 15 ))


if __name__ =='__main__':
    root = Tk()
    ventana = calculator(root)
    root.mainloop()