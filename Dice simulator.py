import random
from tkinter import *
from tokenize import Number

root=Tk()
root.geometry("400x400")

l1=Label(root,font=("times",200))

def roll():
    number=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'{random.choice(number)}')
    l1.pack()


b1=Button(root,text="click to roll the dice", width=50, command=roll)
root.configure(bg='royalblue')
b1.place(x=25,y=10)
l1.configure(bg='royalblue')


root.mainloop()