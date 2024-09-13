from tkinter import *
import tkinter as tk


#functios
def buttonInput(button_name):
    current_text = display_var.get()
    new_text = current_text + button_name
    display_var.set(new_text)

def clean():
    display_var.set("")

def calculator():
    try:
        result = eval(display_var.get())
        display_var.set(str(result))
    except:
        display_var.set("Error")


#window 
root = Tk()
root.title("Calculator")
root.configure(background="#202020")
root.minsize(320,500)
root.geometry("320x500+500+100") 

#icon
icon = PhotoImage(file="C:/Users/Luiz Henrique/Desktop/Projetos/Python/Projetos/Calculadora/calculator.png")
root.iconphoto(False, icon)

#diplay variable
display_var = tk.StringVar()

#display
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 10), bg="#202020", fg="white", anchor ="w")
display_label.grid(row=0, column=0,columnspan=4,sticky="nsew", padx=10, pady=10) 

#buttons 

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)


buttons = [
    ('7', 1, 0),  ('8', 1, 1),  ('9', 1, 2), ('/', 1, 3),
     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    (',',4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3), ('Del', 4, 4)   
]

for (text, row, coll) in buttons:
    if text == '=' :
        button = tk.Button(root, text=text, padx=10, pady=10, command=calculator)
    elif text == 'Del':
        button = tk.Button(root, text=text, padx=10, pady=10, command=clean)
    else:
        button = tk.Button(root, text=text, padx=10, pady=10, command= lambda t=text: buttonInput(t))
    button.grid(row=row, column=coll, sticky="nsew")



root.mainloop()



