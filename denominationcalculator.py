from tkinter import *
from  PIL import Image,ImageTk
from tkinter import messagebox

calculator=Tk()
calculator.title('Caculator')
calculator.geometry("500x600")

def msg():
    box=messagebox.showinfo("click to go to Denominations")
    if box=='ok':
     Topwin()

def Topwin():
    Topwin=Tk()
    Topwin.title('Caculator')
    Topwin.geometry("900x900")   

    l1= Label(Topwin,text="please enter the amount",bg="lghtgrey",fg="black")
    l1.place(x=100,y=450)
 
    l1.pack()
    l2= Label(Topwin,text=" note of 2000",bg="lghtgrey",fg="black")
    l2.place(x=250,y=450)

    l2.pack()
    l3= Label(Topwin,text="note of 500",bg="lghtgrey",fg="black")
    l3.place(x=450,y=450)
 
    l3.pack()
    l4= Label(Topwin,text="note of 100",bg="lghtgrey",fg="black")
    l4.place(x=100,y=450)
 
    l4.pack()
    
    t1=Entry(Topwin)
    t2=Entry(Topwin)
    t3=Entry(Topwin)
    t4=Entry(Topwin)
    

button1=Button(calculator,
              text="Lets get started",
              command=msg,
              bg="black",
              fg="white"
              )
button1.place(x=230,y=450)
button1.pack()

calculator.mainloop


