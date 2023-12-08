from tkinter import *
from tkinter import messagebox
window=Tk()
def btnclick():
    print("clicked")
    b1.configure(text="clicked")
    messagebox.showinfo("info","Button clicked!")
    messagebox.showwarning("info","Button clicked!")
    messagebox.showerror("info","Button clicked!")
b1=Button(text="click",command=btnclick)
b1.pack()
window.mainloop()