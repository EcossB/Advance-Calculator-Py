from ast import Raise
from cProfile import label
from optparse import Values
from tkinter import * 
from tkinter import ttk
import sqlite3
from tokenize import String

class anime_interface:
    database = 'Anime_prog1.db'

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
        self.last_name = Entry(frame1)
        self.last_name.grid(row= 2, column=1)

        #for the photo
        Label(frame1, text= "URL_Photo: ").grid(row= 3, column=0)
        self.photo = Entry(frame1)
        self.photo.grid(row= 3, column=1)

        #Serie
        Label(frame1, text= "Serie: ").grid(row= 4, column=0)
        self.serie = Entry(frame1)
        self.serie.grid(row= 4, column=1)

        #Birth 
        Label(frame1, text= "Birth Date: ").grid(row= 5, column=0)
        self.birth = Entry(frame1)
        self.birth.grid(row= 5, column=1)

        #Power
        Label(frame1, text= "Power: ").grid(row= 6, column=0)
        self.power = Entry(frame1)
        self.power.grid(row= 6, column=1)

        #phrase
        Label(frame1, text= "Favorite Phrase: ").grid(row= 7, column=0)
        self.phrase = Entry(frame1)
        self.phrase.grid(row= 7, column=1)

        #age
        Label(frame1, text= "Age: ").grid(row= 8, column=0)
        self.age = Entry(frame1)
        self.age.grid(row= 8, column=1)

        #sex
        Label(frame1, text= "Sex: ").grid(row= 9, column=0)
        self.sex = Entry(frame1)
        self.sex.grid(row= 9, column=1)

        #state
        Label(frame1, text= "State: ").grid(row= 10, column=0)
        self.state = Entry(frame1)
        self.state.grid(row= 10, column=1)

        #Adress
        Label(frame1, text= "Adress: ").grid(row= 11, column=0)
        self.adress = Entry(frame1)
        self.adress.grid(row= 11, column=1)

        Label(frame1, text= "Latitude: ").grid(row= 12, column=0)
        self.lati = Entry(frame1)
        self.lati.grid(row= 12, column=1)

        Label(frame1, text= "Length: ").grid(row= 13, column=0)
        self.lenght = Entry(frame1)
        self.lenght.grid(row= 13, column=1)



        #button add characters
        ttk.Button(frame1, text="Save character", command= self.insert_characters).grid(row= 14, columnspan=2, sticky= W + E)
        ttk.Button( text="Delete ROW" , command= self.delete_characters).grid(row= 17, column = 0, columnspan= 2, sticky= W + E)
        ttk.Button( text="Edit ROW", command= self.edit_characters).grid(row= 17, column =3, columnspan= 3, sticky= W + E)

        #Output to notificate the add user
        self.ms = Label(text= "", fg='black')
        self.ms.grid(row = 15, column = 0, columnspan= 6, sticky = W + E)

        #creating a table to view the data 
        columns = ('id','name', 'last name', 'url photo', 'datebirth', 'p','ph','a','s','st','ad','lat','lon')

        self.table = ttk.Treeview(height =10, columns= columns)
        self.table.grid(row= 16, column= 0, columnspan=  5)

        #creating the headings of the data
        self.table.heading('#0', text = 'Id', anchor= CENTER)
        self.table.heading('#1', text = 'Name', anchor= CENTER)
        self.table.heading('#2', text = 'Last Name', anchor= CENTER)
        self.table.heading('#3', text = 'Url photo', anchor= CENTER)
        self.table.heading('#4', text = 'Series', anchor= CENTER)
        self.table.heading('#5', text = 'Date birth', anchor= CENTER)
        self.table.heading('#6', text = 'Power', anchor= CENTER)
        self.table.heading('#7', text = 'Favorite Phrase', anchor= CENTER)
        self.table.heading('#8', text = 'Age', anchor= CENTER)
        self.table.heading('#9', text = 'Sex', anchor= CENTER)
        self.table.heading('#10', text = 'State', anchor= CENTER)
        self.table.heading('#11', text = 'Adress', anchor= CENTER)
        self.table.heading('#12', text = 'lat', anchor= CENTER)
        self.table.heading('#13', text = 'lent', anchor= CENTER)
         
        #Setting the width of the columns of th treeview
        self.table.column('#0', minwidth=0, width=0, stretch= YES)
        self.table.column('#1', minwidth=0, width=100, stretch= YES)
        self.table.column('#2', minwidth=0, width=100, stretch= YES)
        self.table.column('#3', minwidth=0, width=100, stretch= YES)
        self.table.column('#4', minwidth=0, width=100, stretch= YES)
        self.table.column('#5', minwidth=0, width=100, stretch= YES)
        self.table.column('#6', minwidth=0, width=100, stretch= YES)
        self.table.column('#7', minwidth=0, width=100, stretch= YES)
        self.table.column('#8', minwidth=0, width=100, stretch= YES)
        self.table.column('#9', minwidth=0, width=100, stretch= YES)
        self.table.column('#10', minwidth=0, width=100, stretch= YES)
        self.table.column('#11', minwidth=0, width=100, stretch= YES)
        self.table.column('#12', minwidth=0, width=100, stretch= YES)
        self.table.column('#13', minwidth=0, width=100, stretch= YES)

        self.get_data()

    #THis function takes three parameters, the first one is the self because we need to manipulate the properties of the class
    #the second one is the query a query like "select * from blah blahj" and the third one is the parameters itself
    #because the second its just a query but the third has what is going to be retrieved
    def get_query(self,query,parameters = ()):
        with sqlite3.connect(self.database) as c:
            cursor = c.cursor()
            result = cursor.execute(query, parameters)
            c.commit()
        return result

    def get_data(self):
        #this three line of codes are made to clean the table and then running the new query
        record = self.table.get_children()
        for e in record:
            self.table.delete(e)

        #here quering the data o retreiving the data
        self.table.get_children()
        querys = 'SELECT * FROM personajess ORDER BY ID'
        data_row = self.get_query(querys)

        #and here we are filling the table with the data
        for row in data_row:
            self.table.insert('',0, text = row[0], values =(row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]))
    
    def validate(self):
       return len(self.name.get()) != 0 and len(self.last_name.get()) != 0 #and len(self.serie.get()) != 0 and len(self.sex.get()) != 0 and len(self.state.get()) != 0
    
    #function to insert data in the table
    def insert_characters(self):
        if self.validate():
            query = 'INSERT INTO personajess VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parar = (self.name.get(), self.last_name.get(),self.photo.get(), self.serie.get(), self.birth.get(), self.power.get(), self.phrase.get(), self.age.get(), self.sex.get(), self.state.get(), self.adress.get(), self.lati.get(),self.lenght.get())
            self.get_query(query, parar)
            #esta linea de codigo es para que el format agregue el nombre del personaje en las llaves
            self.ms['text'] = 'Character {} added succesfully'.format(self.name.get())
            self.name.delete(0,END)
            self.last_name.delete(0,END)
            self.photo.delete(0,END)
            self.serie.delete(0,END)
            self.birth.delete(0,END)
            self.power.delete(0,END)
            self.phrase.delete(0,END)
            self.age.delete(0,END)
            self.sex.delete(0,END)
            self.state.delete(0,END)
            self.adress.delete(0,END)
            self.lati.delete(0,END)
            self.lenght.delete(0,END)
        else:
            self.ms['text'] = 'name, last name, series, sex and state are required'
        self.get_data()


    def delete_characters(self):
        self.ms['text'] = ''
        try:
            self.table.item(self.table.selection())['values'][0]
        except IndexError as e:
            self.ms['text'] = 'Please select a row'
            return 
        self.ms['text'] = ''
        id = self.table.item(self.table.selection())['values'][0]
        delete_query = 'DELETE FROM personajess WHERE name = ?'
        self.get_query(delete_query, (id, ))
        if self.get_query(delete_query, (id, )) != 0:
            self.ms['text'] = 'row {} deleted succesfully'.format(id)
            self.get_data()
        else:
            self.ms['text'] = 'Please select a row'
            self.get_data()

    def edit_characters(self):
        self.ms['text'] = ''
        try:
            self.table.item(self.table.selection())['values'][0]
        except IndexError as e:
            self.ms['text'] = 'Please select a row'
            return 
        name = self.table.item(self.table.selection())['values'][0]
        lastname = self.table.item(self.table.selection())['values'][1]
        url = self.table.item(self.table.selection())['values'][2]
        ser = self.table.item(self.table.selection())['values'][3]
        bir = self.table.item(self.table.selection())['values'][4]
        power = self.table.item(self.table.selection())['values'][5]
        phr = self.table.item(self.table.selection())['values'][6]
        age = self.table.item(self.table.selection())['values'][7]
        sex = self.table.item(self.table.selection())['values'][8]
        state = self.table.item(self.table.selection())['values'][9]
        ad = self.table.item(self.table.selection())['values'][10]

        self.edit_wind = Toplevel()
        self.edit_wind.title = "Edit character"

        #old name
        Label(self.edit_wind, text = "Old name: ").grid(row= 0, column=1)
        Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value= name), state = 'readonly').grid(row = 0, column= 2)
        #new name
        Label(self.edit_wind, text = "New name: ").grid(row= 1, column=1)
        self.new_name = Entry(self.edit_wind).grid(row= 1, column = 2)

        #Old last name
        ttk.Label(self.edit_wind, text = "Old Last Name: ").grid(row= 2, column=1)
        Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value= lastname), state = 'readonly').grid(row = 2, column= 2)
        #new last_name
        Label(self.edit_wind, text = "New Last name: ").grid(row= 3, column=1)
        self.new_last = Entry(self.edit_wind).grid(row= 3, column = 2)
    
        #Old url
        Label(self.edit_wind, text = "Old URL: ").grid(row= 4, column=1)
        Entry(self.edit_wind, textvariable= StringVar(self.edit_wind, value= url), state = 'readonly').grid(row = 4, column= 2)
        #New url
        Label(self.edit_wind, text = "New URL: ").grid(row= 5, column=1)
        self.new_url = Entry(self.edit_wind).grid(row= 5, column = 2)

        

if __name__=='__main__':
    root = Tk()
    open_app = anime_interface(root)  
    root.mainloop()