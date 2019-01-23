from tkinter import *

class Aplication:
    def __init__(self, master=None):
        l1=Label(window,text = "Número de Iterações")
        l1.grid(row =0,column=0)

        l1= Label(window,text = "Dim")
        l1.grid(row =1,column=0)

        l1=Label(window,text = "CR")
        l1.grid(row =2,column=0)

        l1=Label(window,text = "F")
        l1.grid(row =3,column=0)

        l1=Label(window,text = "Polupation Size")
        l1.grid(row =4,column=0)

        l1=Label(window,text = "Upper Limit")
        l1.grid(row =5,column=0)

        l1=Label(window,text = "Lower Limit")
        l1.grid(row =6,column=0)

        l1=Label(window,text = "Print Status")
        l1.grid(row =7,column=0)

        l1=Label(window,text = "Function")
        l1.grid(row =8,column=0)  

        #Define as entradas
        title_text = StringVar()
        e1 = Entry(window,textvariable = "NumIteration")
        e1.grid(row =0,column=1)

        title_text = StringVar()
        e2 = Entry(window,textvariable = "Dim")
        e2.grid(row =1,column=1)

        title_text = StringVar()
        e3 = Entry(window,textvariable = "CR")
        e3.grid(row =2,column=1)

        title_text = StringVar()
        e4 = Entry(window,textvariable = "F")
        e4.grid(row =3,column=1)

        title_text = StringVar()
        e5 = Entry(window,textvariable = "PolupationSize")
        e5.grid(row =4,column=1)

        title_text = StringVar()
        e6 = Entry(window,textvariable = "UpperLimit")
        e6.grid(row =5,column=1)

        title_text = StringVar()
        e7 = Entry(window,textvariable = "LowerLimit")
        e7.grid(row =6,column=1)

        title_text = StringVar()
        e8 = Entry(window,textvariable = "Print Status")
        e8.grid(row =7,column=1)

        title_text = StringVar()
        e9 = Entry(window,textvariable = "Function")
        e9.grid(row =8,column=1)


root = Tk()
Aplication(root)
root.mainloop()