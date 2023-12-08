from tkinter import *
window=Tk()
m=Menu()

item1=Menu(m,tearoff=False)
item1.add_command(label="New Text File")
item1.add_command(label="New File")
item1.add_command(label="New Window")
item1.add_separator()
item1.add_command(label="New File")
item1.add_command(label="New Window")
m.add_cascade(label="File",m=item1)

item2=Menu(m,tearoff=False)
item2.add_command(label="New Text File")
item2.add_command(label="New File")
item2.add_command(label="New Window")
m.add_cascade(label="Edit",m=item2)

window.configure(m=m)
window.mainloop()
