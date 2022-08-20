from tkinter import * 
from tkinter import ttk
import sqlite3

class anime_interface:
    def __init__(self, root):
        self.window = root
        self.window.title('Gestionar personajes')
        
        #creacion del contenedor
        frame1 = LabelFrame(self.window,text= 'Add a new character', )
        frame1.grid(row = 0, column= 0, columnspan=6, pady= 20)

        #data inputs
        #input for the name
        Label(frame1, text= "Name: ").grid(row= 1, column=0)
        self.name = Entry(frame1)
        self.name.focus()
        self.name.grid(row= 1, column=1)


        #for the last name
        Label(frame1, text= "LastName: ").grid(row= 2, column=0)
        self.last_name = Entry(frame1).grid(row= 2, column=1)

        #for the photo
        Label(frame1, text= "URL_Photo: ").grid(row= 3, column=0)
        self.photo = Entry(frame1).grid(row= 3, column=1)

        #Serie
        Label(frame1, text= "LastName: ").grid(row= 4, column=0)
        self.photo = Entry(frame1).grid(row= 4, column=1)

        #Birth 
        Label(frame1, text= "Birth Date: ").grid(row= 5, column=0)
        self.birth = Entry(frame1).grid(row= 5, column=1)

        #button add characters
        ttk.Button(frame1, text="Save character").grid(row= 6, columnspan=2, sticky= W + E)

        #creating a table to view the data 
        columns = ('name', 'last name', 'url photo', 'datebirth')

        self.table = ttk.Treeview(height =10, columns= columns)
        self.table.grid(row= 7, column= 0, columnspan=  5)

        #creating the headings of the data
        self.table.heading('#0', text = 'Name', anchor= CENTER)
        self.table.heading('#1', text = 'Last Name', anchor= CENTER)
        self.table.heading('#2', text = 'Url photo', anchor= CENTER)
        self.table.heading('#3', text = 'Series', anchor= CENTER)
        self.table.heading('#4', text = 'Date birth', anchor= CENTER)







if __name__=='__main__':
    root = Tk()
    open_app = anime_interface(root)  
    root.mainloop()