from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

root=Tk()
root.title('image')
root.geometry('400x400')

upload=Image.open('python module 3 files/class 5/garden.jpg')
image=ImageTk.PhotoImage(upload)

label=Label(root, image=image , height=400 , width =400)
label.place(x=50,y=26)
label2=Label(root, text="How to add image using tkinter")
label2.place(x=47,y=0)

def scanning():
   messagebox.showwarning("Alert","stop no virus detected")

button=Button(root, text="scan for virus" , command=scanning)
button.place(x=50,y=26)


def topwindow():
   top=Toplevel()
   top.geometry=("4000x4000")
   top.title=("new window")
   
   label=Label(top,text="this is my topwindow")
   label.pack()
   button=Button(top,text="click to go to another window", command=topwindow )
   button.pack()
   top.mainloop()

button=Button(root,text="click to go to another window", command=topwindow )
button.pack()


root.mainloop()