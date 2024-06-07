from tkinter import *

window = Tk()
window.geometry("800x450")
window.title("helloTest")
icon = PhotoImage(file='img.png')
window.iconphoto(True, icon)
window.config(background="lightblue")


listbox = Listbox(window,
                  bg = 'skyBlue',
                  font= ("Impact",20),
                  width=20,
                  selectmode=MULTIPLE
                  )
listbox.pack(pady =10)
listbox.insert(1, "pizza")
listbox.insert(2, "burger")
listbox.insert(3, "pasta")
listbox.insert(4, "rice")
listbox.insert(5, "chicken")
listbox.config(height=(listbox.size()))

def sumbit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered:")
    for index in food:
        print(index)



sumbitList = Button(window,
                    text="Sumbit",
                    font=("Impact", 20),
                    command=sumbit
                    )

sumbitList.pack(pady =10)

addentry = Entry(window,
                 background='lightBlue',
                 font=("Impact", 20),
                 )
addentry.pack(pady = 10,)

def addFunction():
    try:
        listbox.insert(listbox.size(), addentry.get())
        listbox.config(height=(listbox.size()))
    except:
        "Enter something"

addButton = Button(window,
                   text="Add",
                   command = addFunction,
                   font=("Impact", 20),
                   )
addButton.pack(pady=5)


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=(listbox.size()))


deleteButton = Button(window,
                      text="Delete",
                      command=delete,
                      font=("Impact", 20),
                      )
deleteButton.pack(pady = 10)

window.mainloop()