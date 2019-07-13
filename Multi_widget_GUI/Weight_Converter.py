from tkinter import *

window=Tk()
window.title('Weight Converter')


def from_kg():
    grams=float(e1_val.get())*1000
    pounds=float(e1_val.get())*2.20462
    ounces=float(e1_val.get())*35.274

    t1.delete(1.0,END)
    t1.insert(END,grams)

    t2.delete(1.0,END)
    t2.insert(END,pounds)

    t3.delete(1.0,END)
    t3.insert(END,ounces)

l1=Label(window,text="KG")
l1.grid(row=0,column=0)

e1_val=StringVar()
e1=Entry(window,textvariable=e1_val)
e1.grid(row=0,column=1)

b1=Button(window,text="Convert",command=from_kg)
b1.grid(row=0,column=2)

l2=Label(window,text="Grams")
l2.grid(row=1,column=0)
t1=Text(window,height=1,width=20)
t1.grid(row=1,column=1)

l3=Label(window,text="Pounds")
l3.grid(row=1,column=2)
t2=Text(window,height=1,width=20)
t2.grid(row=1,column=3)

l4=Label(window,text="Ounces")
l4.grid(row=1,column=4)
t3=Text(window,height=1,width=20)
t3.grid(row=1,column=5)

window.mainloop()
