'''PROJECT DESCRIPTION

In this project, the five motivational lines which we wanna speak to ourself every morning is being displayed and these were the lines of Dr.A.P.J Abdul Kalam. With
the help of some basic concepts of tkinter and labels I have done this task.'''

from tkinter import *
from tkinter.font import Font
window=Tk()
window.geometry("500x500")
window.title("Practice")
window['background']="#0a3d62"
window.resizable(height="false",width="false")
myfont=Font(family="times",size=35,weight="bold",slant="italic",underline=1)
lab=Label(window,text="Happy morning!",font=myfont,bg="#856ff8",fg="pink",padx=32,pady=16,relief="raised")
lab.pack()
myfont=Font(family="times",size=10,weight="bold",slant="italic",underline=1)
lab1=Label(window,text="Speak these 5 lines to yourself every morning",font=myfont,bg="grey",padx=10,pady=20,relief="raised")
lab1.pack()
myfont=Font(family="times",size=15,weight="bold")
lab2=Label(window,text="1.I AM THE BEST",font=myfont,bg="red",fg="yellow",padx=5,pady=5,relief="raised")
lab2.pack()
myfont=Font(family="times",size=20,weight="bold")
lab3=Label(window,text="2.I CAN DO IT",font=myfont,bg="yellow",padx=7,pady=7,relief="raised")
lab3.pack()
myfont=Font(family="times",size=15,weight="bold")
lab4=Label(window,text="3.GOD IS ALWAYS WITH ME",font=myfont,bg="green",padx=10,pady=10,relief="raised")
lab4.pack()
myfont=Font(family="times",size=25,weight="bold")
lab5=Label(window,text="4.I AM A WINNER",font=myfont,bg="violet",fg="blue",padx=15,pady=15,relief="raised")
lab5.pack()
myfont=Font(family="times",size=30,weight="bold")
lab6=Label(window,text="5.TODAY IS MY DAY",font=myfont,bg="orange",fg="brown",padx=20,pady=20,relief="raised")
lab6.pack()
window.mainloop()

