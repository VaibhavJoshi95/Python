from tkinter import *

root = Tk()

e = Entry(root, width=35, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=30)

def number_input(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def clear_values():
    e.delete(0, END)

n1 = []

def sum_values():
    num1 = e.get()
    n1.append(int(num1))
    e.delete(0, END)

def diff_values():
    num1=e.get()
    n1.append(int(num1))
    e.delete(0,END)

def equals():
    if
    num1 = e.get()
    n1.append(int(num1))
    e.delete(0, END)

    s = 0
    for i in n1:
        s += i
    e.insert(0, s)

# Buttons
bttn9 = Button(root, text='9', padx=40, pady=20, command=lambda: number_input(9))
bttn8 = Button(root, text='8', padx=40, pady=20, command=lambda: number_input(8))
bttn7 = Button(root, text='7', padx=40, pady=20, command=lambda: number_input(7))

bttn6 = Button(root, text='6', padx=40, pady=20, command=lambda: number_input(6))
bttn5 = Button(root, text='5', padx=40, pady=20, command=lambda: number_input(5))
bttn4 = Button(root, text='4', padx=40, pady=20, command=lambda: number_input(4))

bttn3 = Button(root, text='3', padx=40, pady=20, command=lambda: number_input(3))
bttn2 = Button(root, text='2', padx=40, pady=20, command=lambda: number_input(2))
bttn1 = Button(root, text='1', padx=40, pady=20, command=lambda: number_input(1))

bttn0 = Button(root, text='0', padx=40, pady=20, command=lambda: number_input(0))

butt_add = Button(root, text='+', padx=40, pady=20, command=sum_values)
btnn_clear = Button(root, text='cls', padx=40, pady=20, command=clear_values)
btnn_equals = Button(root, text='=', padx=40, pady=20, command=equals)

# Grid placement
bttn9.grid(row=1, column=0)
bttn8.grid(row=1, column=1)
bttn7.grid(row=1, column=2)

bttn6.grid(row=2, column=0)
bttn5.grid(row=2, column=1)
bttn4.grid(row=2, column=2)

bttn3.grid(row=3, column=0)
bttn2.grid(row=3, column=1)
bttn1.grid(row=3, column=2)

bttn0.grid(row=4, column=0)

butt_add.grid(row=4, column=1, columnspan=2)
btnn_clear.grid(row=5, column=0)
btnn_equals.grid(row=5, column=1, columnspan=2)

root.mainloop()
