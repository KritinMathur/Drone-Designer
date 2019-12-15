from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.title("UAV Designer")
root.wm_iconbitmap('icon.ico')

def callback(url):
    webbrowser.open_new(url)

def func():
    mtlb = Label(root,text = "Motor:- 800-1100 KV (brushless dc motor)").grid(row=1,column=2)
    esclb = Label(root,text = "ESC: 15A – 40A").grid(row=2,column=2)
    btlb = Label(root,text = "Battery: 3S LiPo (1800 – 3600mAh)").grid(row=3,column=2)
    prlb = Label(root,text = "Propeller: “1045″ OR “8045” Propeller (CW & CCW)").grid(row=4,column=2)
    fclb = Label(root,text = "Also requires Flight-Controller,Transmitter,Reciver").grid(row=5,column=2)
    kmlb = Label(root,text = "To know more details contact: Team UAS Nmims").grid(row=6,column=2)
    chslb = Label(root,text = "Chosen config:- QuadCopter 450mm").grid(row=0,column=4)
    sllb = Label(root,image = slim_resized).grid(row=2,column=4,rowspan = 6)
    abtus.grid(row = 8,column = 4)
    
    

inpt = Label(root,text = "Input:-",font = "Helvetica 18 bold").grid(row=0,column=0,columnspan = 2)
oupt = Label(root,text = "Output:-",font = "Helvetica 18 bold").grid(row=0,column=2) 
pplb = Label(root,text = "Purpose").grid(row=1,column=0)
pllb = Label(root,text = "Payload (Kg)").grid(row=3,column=0)
ftlb = Label(root,text = "Flight-Time (Min)").grid(row=5,column=0)
btn = Button(root,text = "Proceed",command = func).grid(row=6,column=0,columnspan = 2)

compare = PhotoImage(file = 'comp.png')
compare_resized = compare.zoom(1)
compare_resized = compare_resized.subsample(2)
cmlb = Label(root,image = compare_resized).grid(row=7,column=0,columnspan = 3)

slim = PhotoImage(file = 'quad.png')
slim_resized = slim.zoom(1)
slim_resized = slim_resized.subsample(2)

cb=ttk.Combobox(root,values=["Air-Delivery","Agriculture","Defence","Surveillance","Service","Survey-Mapping","Other"], width = 17)
cb.grid(column=1,row=1)
cb.current(0)
plen = Entry(root).grid(row=3,column=1)
ften = Entry(root).grid(row=5,column=1)

abtus = Label(root,text = "http://uasnmims.co.in/",fg="blue", cursor="hand2")
abtus.bind("<Button-1>", lambda e: callback("http://uasnmims.co.in/"))

root.mainloop()
