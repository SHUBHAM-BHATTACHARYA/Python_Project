from tkinter import*
from tkinter import messagebox
root=Tk()
def clear_n():
  e1.delete(first=0,last='end')
  e2.delete(first=0,last='end')
  e3.delete(first=0,last='end')
  e1.focus()
def add_n():
  try:
    x=float(e1.get())
    y=float(e2.get())
    s=x+y
    e3.insert(0,s)
  except ValueError:

    messagebox.showinfo('Wrong input', 'enter only number')
l1=Label(root,text="enter the value")
l2=Label(root,text="enter the value")
l3=Label(root,text="output")
e1=Entry(root)
e1.focus()
e2=Entry(root)
e3=Entry(root)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
b1=Button(root,text="add",command=add_n)
b2=Button(root,text="clear",command=clear_n)
b3=Button(root,text="exit",command=root.destroy)
b1.grid(row=4,column=1)
b2.grid(row=4,column=3)
b3.grid(row=4,column=0)
root.mainloop()
