from tkinter import *
window=Tk()
window.title("CALCULATOR")
e=Entry(bd=5,width=40)
e.grid(row=0,column=0,columnspan=6)
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)  

def button_add():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global m
    m="addition"
    e.delete(0,END)

def button_sub():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global m
    m="substraction"
    e.delete(0,END)

def button_mul():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global m
    m="multiplication"
    e.delete(0,END)

def button_div():
    first_number=e.get()
    global f_num
    f_num=int(first_number)
    global m
    m="divition"
    e.delete(0,END)        

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if m=="addition":
        e.insert(0,f_num + int(second_number))
    if m=="substraction":
        e.insert(0,f_num - int(second_number))    
    if m=="multiplication":
        e.insert(0,f_num * int(second_number))
    if m=="division":
        e.insert(0,f_num / int(second_number))

zero=Button(text="0",command=lambda:button_click(0))
one=Button(text="1",command=lambda:button_click(1))
two=Button(text="2",command=lambda:button_click(2))
three=Button(text="3",command=lambda:button_click(3))
four=Button(text="4",command=lambda:button_click(4))
five=Button(text="5",command=lambda:button_click(5))
six=Button(text="6",command=lambda:button_click(6))
seven=Button(text="7",command=lambda:button_click(7))
eight=Button(text="8",command=lambda:button_click(8))
nine=Button(text="9",command=lambda:button_click(9))
add=Button(text="+",command=button_add)
sub=Button(text="-",command=button_sub)
mul=Button(text="*",command=button_mul)
div=Button(text="/",command=button_div)
equal=Button(text="=",command=button_equal)
clear=Button(text="c",command=button_clear)

zero.grid(row=4,column=0,ipadx=30,ipady=20)
one.grid(row=1,column=0,ipadx=30,ipady=20)
two.grid(row=1,column=1,ipadx=30,ipady=20)
three.grid(row=1,column=2,ipadx=30,ipady=20)
four.grid(row=2,column=0,ipadx=30,ipady=20)
five.grid(row=2,column=1,ipadx=30,ipady=20)
six.grid(row=2,column=2,ipadx=30,ipady=20)
seven.grid(row=3,column=0,ipadx=30,ipady=20)
eight.grid(row=3,column=1,ipadx=30,ipady=20)
nine.grid(row=3,column=2,ipadx=30,ipady=20)
add.grid(row=1,column=3,ipadx=30,ipady=20)
sub.grid(row=2,column=3,ipadx=30,ipady=20)
mul.grid(row=3,column=3,ipadx=30,ipady=20)
div.grid(row=4,column=2,ipadx=30,ipady=20)
equal.grid(row=4,column=3,ipadx=30,ipady=20)
clear.grid(row=4,column=1,ipadx=30,ipady=20)

window.mainloop()