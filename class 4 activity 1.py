from tkinter import *
window=Tk()
window.title("my first window")
window.geometry("300x300")
greeting=Label(text="hello user" , fg="blue" , bg="yellow")
button=Button (text="click me" , fg="pink" , bg="green")
entry=Entry(text="click me",  fg="pink", bg="green")
greeting.pack()
button.pack()
entry.pack()
frame=Frame(master=window , borderwidth=5 , relief=RIDGE)
frame.pack()
window.mainloop()