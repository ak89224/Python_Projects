from tkinter import *
import Backend


def get_selected_row(event):
    global selected_row
    try:
        index=list1.curselection()[0]
        selected_row=list1.get(index)

        e1.delete(0,END)
        e1.insert(END,selected_row[1])
        e2.delete(0, END)
        e2.insert(END,selected_row[2])
        e3.delete(0, END)
        e3.insert(END,selected_row[3])
        e4.delete(0, END)
        e4.insert(END,selected_row[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in Backend.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in Backend.search(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()):
        list1.insert(END,row)

def insert_command():
    Backend.insert(title_val.get(),author_val.get(),year_val.get(),isbn_val.get())
    list1.delete(0,END)
    list1.insert(END,(title_val.get(),author_val.get(),year_val.get(),isbn_val.get()))

def delete_command():
#    print(selected_row[0])
    Backend.delete(selected_row[0])

def update_command():
    Backend.update(selected_row[0],title_val.get(),author_val.get(),year_val.get(),isbn_val.get())




window = Tk()
window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
title_val = StringVar()
e1 = Entry(window, textvariable=title_val)
e1.grid(row=0, column=1)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
author_val = StringVar()
e2 = Entry(window, textvariable=author_val)
e2.grid(row=0, column=3)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
year_val = StringVar()
e3 = Entry(window, textvariable=year_val)
e3.grid(row=1, column=1)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
isbn_val = StringVar()
e4 = Entry(window, textvariable=isbn_val)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=10, width=50)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>',get_selected_row)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3, columnspan=2)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12,command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update Selected", width=12,command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete Selected", width=12,command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12,command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
