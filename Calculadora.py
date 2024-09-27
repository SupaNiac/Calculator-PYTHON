from tkinter import *
import tkinter as ttk
import tkinter as tk
import math


#colors
color1 = "#202020" #black
color2 = "#ffffff" #white
color3 = "#323232" #dark grey
color4 = "#3c3c3c" #dark grey2
color5 = "#006e7f" #blue
color6 = "#128c9f" #blue2
color7 = "#000000" #black2
color8 = "#f8bc2e" #yellow 
color9 = "#f8c449" #yellow2
color10= "#b22727" #red 
color11= "#c83a3a" #red2
color12= "#21bd14" #green 
color13= "#2ad41c" #green2

#window
window = Tk()
window.title("Calculadora")
window.geometry("323x395")
window.config(bg=color1)


#functios
showValue = StringVar()
values = ''

def inputValue(event):
    global values
    values = values + str(event)
    showValue.set(values)

def calculate():
    global values
    try:
       
        result = eval(values)
        showValue.set(str(result))
        values = str(result)  
    except ZeroDivisionError:
        showValue.set("Undefined result")  
        values = ""  
    except Exception as e:
        showValue.set("Error")  
        values = ""  

def clean():
    global values
    values = ''
    showValue.set('')


#frames
frameDisplay = Frame(window, width=323, height=120, bg=color2)
frameDisplay.grid(row=0, column= 0)

frameKeyboard = Frame(window, width=323, height=250, bg=color1)
frameKeyboard.grid(row=1, column=0)

frameFooter = Frame(window, width=323, height=15, bg=color1)
frameFooter.grid(row=2, column= 0)


#icon
icon = PhotoImage(file="C:/Users/Luiz Henrique/Desktop/Projetos/Python/Projetos/Calculadora/calculator.png")
window.iconphoto(False, icon)


#label 
labelScreen = Label(frameDisplay, textvariable=showValue, bg=color1, fg= color2, font=("ivy 24 bold"), width=16, padx=8, pady=40, justify="right", anchor='e', relief='flat')
labelScreen.pack()

labelFooter= Label(frameFooter, text="V.: 1.3.2", bg=color1, fg=color2, font=("ivy 9 bold"), width=44, padx=8, justify="right", anchor="e")
labelFooter.pack()

#buttons 
btn1 = Button(frameKeyboard, command= clean, text="C", width=17, height=2, bg=color10, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color11, activeforeground=color7, highlightthickness=0, borderwidth=0)
btn1.place(x=0, y=0)

btn2 = Button(frameKeyboard, command= lambda: inputValue('%'), text='%', width=8, height=2, bg=color8, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color9, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn2.place(x=162, y=0)

btn3 = Button(frameKeyboard, command= lambda: inputValue('/'), text='/', width=8, height=2, bg=color8, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color9, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn3.place(x=241.5, y=0)

btn4 = Button(frameKeyboard, command= lambda: inputValue('7'), text='7', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn4.place(x=0, y=49)

btn4 = Button(frameKeyboard, command= lambda: inputValue('8'), text='8', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn4.place(x=80, y=49)

btn5 = Button(frameKeyboard, command= lambda: inputValue('9'), text='9', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn5.place(x=161, y=49)

btn6 = Button(frameKeyboard, command= lambda: inputValue('*'), text='X', width=8, height=2, bg=color8, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color9, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn6.place(x=241, y=49)

btn7 = Button(frameKeyboard, command= lambda: inputValue('4'), text='4', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn7.place(x=0, y=98)

btn8 = Button(frameKeyboard, command= lambda: inputValue('5'), text='5', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn8.place(x=80, y=98)

btn9 = Button(frameKeyboard, command= lambda: inputValue('6'), text='6', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn9.place(x=161, y=98)

btn10 = Button(frameKeyboard, command= lambda: inputValue('-'), text='-', width=8, height=2, bg=color8, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color9, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn10.place(x=241, y=98)

btn11 = Button(frameKeyboard, command= lambda: inputValue('1'), text='1', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn11.place(x=0, y=147)

btn12 = Button(frameKeyboard, command= lambda: inputValue('2'), text='2', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn12.place(x=80, y=147)

btn13 = Button(frameKeyboard, command= lambda: inputValue('3'), text='3', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn13.place(x=161, y=147)

btn14 = Button(frameKeyboard, command= lambda: inputValue('+'), text='+', width=8, height=2, bg=color8, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color9, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn14.place(x=241, y=147)

btn15 = Button(frameKeyboard, command= lambda: inputValue('0'), text='0', width=17, height=2, bg=color12, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color13, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn15.place(x=0, y=195)

btn16 = Button(frameKeyboard, command= lambda: inputValue('.'), text='.', width=8, height=2, bg=color3, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color4, activeforeground=color2, highlightthickness=0, borderwidth=0 )
btn16.place(x=161, y=195)

btn17 = Button(frameKeyboard, command= calculate, text='=', width=8, height=2, bg=color5, fg=color2, font=("ivy 11 bold"), relief="flat", overrelief="raised", activebackground=color6, activeforeground=color7, highlightthickness=0, borderwidth=0 )
btn17.place(x=241, y=195)


window.mainloop()
