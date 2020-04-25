from tkinter import *
def show_data():
  txt.delete(0.0,'end')
  txtname=ent.get()
  gender=var_chk.get()
  if gender==1:
    gender="sir"
  else:
    gender="mam"
  s="hello,"+str(txtname)+"\nhow are you "+gender+"?"
  txt.insert(0.0,s)
root=Tk()
root.geometry("200x250")
l1=Label(root,text="name")
l2=Label(root,text="gender")
ent= Entry(root)
var_chk=IntVar()
rd1=Radiobutton(root,text="Male", variable=var_chk,value=1)
rd2=Radiobutton(root,text="FEMale", variable=var_chk,value=2)
l1.grid(row=0)
l2.grid(row=1)
ent.grid(row=0,column=1)
rd1.grid(row=1,column=1,sticky=W)
rd2.grid(row=1,column=1,sticky=E)
btn=Button(root,text="register",bg="purple", fg="white",command=show_data)
btn.grid(row=2,column=1)
txt=Text(root, width=25,height=10,wrap=WORD)
txt.grid(row=3,column=1)
