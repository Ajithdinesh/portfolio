from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox,Progressbar
from tkinter import messagebox    
window=Tk()
window.geometry('300x500')
window.configure(bg="red")
window.title("CALCULATOR")
window.iconbitmap("icons8_calculator_50_LCw_icon.ico")
window.attributes("-alpha",1)
l1=Label(text="NAME:",bg="green")
l1.grid(row=0,column=0)
l2=Entry(bg="blue")
l2.grid(row=0,column=1)
b=Button(text="click",bg="yellow",fg="black")
b.grid(row=1,column=0)
l2=Label(text="GENDER")
l2.grid(row=2,column=0)
r1=Radiobutton(text="MALE",value="MALE")
r1.grid(row=3,column=0)
r1=Radiobutton(text="FEMALE",value="FEMALE")
r1.grid(row=4,column=0)
r1=Radiobutton(text="OTHERS",value="OTHERS")
r1.grid(row=5,column=0)
l1=Label(text="Select Favourite Language")
l1.grid(row=6,column=0)
c1=Checkbutton(text="ENGLISH")
c1.grid(row=7,column=0)
s=Spinbox(from_=1,to=20)
s.grid(row=8,column=0)
s=scrolledtext.ScrolledText(width=20,height=20)
s.grid(row=9,column=0)
c=Combobox()
c['values']=("Kerala","Karnataka","Tamilnadu")
c.current(0)
c.grid(row=10,column=0)
p=Progressbar(length=200)
p['value']=70
p.grid(row=11,column=0)
window.mainloop()