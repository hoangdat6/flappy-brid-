from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%a \n\t %D \n %H:%M:%S  <♥‿♥>  %r')
    
    label.config(anchor= CENTER,text=string) 
    label.after(1000, time)

label = Label(root, font=("ds-digital", 20),
              background= "black",
              foreground= "red")
label.pack(anchor='center')
time()

mainloop()