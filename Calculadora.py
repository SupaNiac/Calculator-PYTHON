from tkinter import *
import tkinter as ttk
import tkinter as tk
import math


#colors
color1 = "#202020"
color2 = "#ffffff"
color3 = "#323232"
color4 = "#3c3c3c"
color5 = "#4cc2ff"
color6 = "#47b1e8"
color7 = "#000000"


#functios
showValue = StringVar()
values = ''

def inputValue(event):
    global value
    values = values + str(event)
    showValue.set(values)

def calculate():
    global values
    result = eval(values)
    showValue.set(str(result))
    values = str(result)

def clean():
    global values
    values = ''
    showValue.set('')


#window
window = Tk()
window.title("Calculadora")
window.geometry("320x500")
window.config(bg=color1)

#frames
frameDisplay = Frame(window, width=320, height=130, bg=color2)
frameDisplay.grid(row=0, column= 0)

frameKeyboard = Frame(window, width=320, height=0, bg=color1)
frameKeyboard.grid(row=1, column=0)

frameFooter = Frame(window, width=320, height=0, bg=color1)
frameFooter.grid(row=2, column= 0)


#icon
icon = PhotoImage(file="C:/Users/Luiz Henrique/Desktop/Projetos/Python/Projetos/Calculadora/calculator.png")
window.iconphoto(False, icon)


window.mainloop()



