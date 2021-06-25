from tkinter import *
import sqlite3

app = Tk()
app.title('Buguette')
app.geometry('400x400')

def bonjour():
	bonjour = Label(app, text = "Bonjour, " + textBox.get())
	bonjour.pack()

text = Label(app, text="Bonjour! Comment tu t'appelles?")
text.pack()

textBox = Entry(app, width=15)
textBox.pack()

button = Button(app, text="On y va!", command = bonjour)
button.pack()

app.mainloop()