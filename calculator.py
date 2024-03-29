from tkinter import *
from math import *
import parser
import sqlite3


i = 0
#creatio of the class 
class calculator:
    def __init__(self, root):
        self.wind = root
        self.wind.title('Calculator final')

        database = 'calculator.db'

        #creating the screen of the operations and numbers
        display = Entry(self.wind, width= 50, background = "#add8e6", foreground= "white", font=('Times New Romans', 15))
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

        Button(self.wind, text="C", width= 9, height= 3, command=lambda:clear()).grid(row=4, column=0, sticky= W+E)
        Button(self.wind, text="0", width= 9, height= 3, command=lambda:get_numbers(0)).grid(row=4, column=1, sticky= W+E)
        Button(self.wind, text="%", width= 9, height= 3, command=lambda:get_operations("%")).grid(row=4, column=2, sticky= W+E)
        
        #operations buttons
        Button(self.wind, text="+", width= 9, height= 3, command=lambda:get_operations("+")).grid(row=1, column=3, sticky= W+E)
        Button(self.wind, text="-", width= 9, height= 3, command=lambda:get_operations("-")).grid(row=2, column=3, sticky= W+E)
        Button(self.wind, text="x", width= 9, height= 3, command=lambda:get_operations("*")).grid(row=3, column=3, sticky= W+E)
        Button(self.wind, text=u"\u00f7", width= 9, height= 3, command=lambda:get_operations("/")).grid(row=4, column=3, sticky= W+E)

        Button(self.wind, text=u"\u232B", width= 9, height= 3, command=lambda:Undo()).grid(row=1, column=4, sticky= W+E, columnspan= 1)
        Button(self.wind, text="√", width= 9, height= 3, command=lambda:get_operations("**0.5")).grid(row=1, column=5, sticky= W+E, columnspan= 1)
        Button(self.wind, text="EXP", width= 9, height= 3, command=lambda:get_operations("**")).grid(row=2, column=4, sticky= W+E)
        Button(self.wind, text="^2", width= 9, height= 3, command=lambda:get_operations("**2")).grid(row=2, column=5, sticky= W+E)
        Button(self.wind, text="(", width= 9, height= 3, command=lambda:get_operations("(")).grid(row=3, column=4, sticky= W+E)
        Button(self.wind, text=")", width= 9, height= 3, command=lambda:get_operations(")")).grid(row=3, column=5, sticky= W+E)
        Button(self.wind, text="=", width= 9, height= 3, command=lambda:calculate()).grid(row=4, column=4, sticky= W+E, columnspan= 1)
        Button(self.wind, text="↻", width= 9, height= 3, command=lambda:history()).grid(row=4, column=5, sticky= W+E)
    

        #method that takes an index and number
        def get_numbers(n):
            global i 
            display.insert(i, n)
            i+=1

        def get_operations(operator):
            global i
            op_lenght = len(operator)   
            display.insert(i, operator)
            i+=op_lenght

        def clear():
            display.delete(0, END)

        def Undo():
            display_state = display.get()
            if len(display_state):
                display_new_state = display_state[:-1]
                clear()
                display.insert(0, display_new_state)
            else:
                clear()        
                display.insert(0, 'error')

        def calculate():
            display_state = display.get()
            try:
                math_expr =parser.expr(display_state).compile()
                result=  eval(math_expr)
                clear()
                display.insert(0, result)


            except:
                clear()
                display.insert(0, 'Error')
                        
            query ='INSERT INTO procesos VALUES(NULL, ?, ?)'
            parar = (display_state, str(result))
            get_query(query, parar)
            print(display_state, result)


        def get_query( query, parameters = ()):
            with sqlite3.connect(database) as c:
                cursor = c.cursor()
                result = cursor.execute(query, parameters)
                c.commit()
            return result
        

        def history():
            history_wind = Toplevel()
            history_wind.title("History")

            screen2= Text(history_wind,state= "disabled", width= 50, height= 5, background="#add8e6", foreground="white", font=("Times New Romans", 15))
            screen2.grid(row= 0, column= 0, columnspan=4, padx = 5, pady = 5)

            Button(history_wind, width= 9, height=3, text="Back", command=lambda:destroy()).grid(row = 1, column= 0, columnspan=4,sticky= W+E)

            #def get_data():
            query = 'SELECT * FROM procesos ORDER BY ID DESC'
            data = get_query(query)
            tup1 = tuple('=')
            tup = tuple('|')

            for row in data:
                op = row[1:2]
                re = row[2:3]
                screen2.configure(state= "normal")
                #screen2.insert(END, tup + op + tup1)
                #screen2.insert(END,  re + tup)
                print(row[1:3],'\n')
                mess = '''
                        Operation {op} Result {re}
                        '''
                mess = mess.replace("{op}", str(op))
                mess = mess.replace("{re}",str(re))
                screen2.insert(END, mess)
                screen2.configure(state="disabled")

            def destroy():
                history_wind.destroy()



        
            

                

      



        



        
    
 

        


if __name__ =='__main__':
    root = Tk()
    ventana = calculator(root)
    root.mainloop()