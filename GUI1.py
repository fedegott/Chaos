from tkinter import *
from tkinter import ttk

a = int(input("please enter a number:"))

try:
    root1 = Tk()
    root1.title('this is a program')
    ttk.Button(root1, text = "Hello World").grid()
    ttk.Button(root1, text = "I'm happy ").grid()
    ttk.Label(root1, text = 'hi my name is glory').grid()
    ttk.Checkbutton(root1, text = 'kawawonga').grid()
    ttk.Radiobutton(root1, text = 'kawawonga', value = 'jota').grid()

    b = ttk.Entry(root1, text ='jose').grid(column =1, row = 1)

except :
    pass


root1.mainloop()

print('hello')


