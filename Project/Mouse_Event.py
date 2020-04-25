from tkinter import *
def left (event):
  print("left button")
def right (event):
  print("right button")
def middle (event):
  print("middle button")
root=Tk()
mf=Frame(root, width=300, height=250)
mf.bind("<Button-1>",left)
mf.bind("<Button-2>",middle)
mf.bind("<Button-3>",right)
mf.pack()
root.mainloop()

