from tkinter import *

root = Tk()
root.title("Tkinter Menu")
root.minsize(300, 300)

def hello():
    print('hello')

def showFrame1():
    frame2.grid_remove()
    frame1.grid()

def showFrame2():
    frame1.grid_remove()
    frame2.grid()

def radioSelected():
    print(myVar.get())

mainMenu = Menu(root)

dropDown = Menu(mainMenu, tearoff = 0)
dropDown.add_command(
    label = 'Frame 1',
    command = showFrame1
)
dropDown.add_command(
    label = 'Frame 2',
    command = showFrame2
)
dropDown.add_separator()
dropDown.add_command(
    label = 'Exit',
    command = root.quit
)

mainMenu.add_command(
    label = 'Item',
    command = hello
)
mainMenu.add_cascade(
    label = 'Dropdown',
    menu = dropDown
)
mainMenu.add_command(
    label = 'Quit',
    command = root.quit
)
root.config(menu=mainMenu)

frame1 = Frame(root)
frame1.grid(column = 0, row = 0)

label1 = Label(frame1,
    text = 'Frame1',
    fg = '#007',
    font = 'Arial 30 bold italic'
)
label1.pack(side = "top")

frame2 = Frame(root)
frame2.grid(column = 0, row = 0) 

label2 = Label(frame2,
    text = 'Frame2',
    fg = '#b0b',
    font = 'Arial 20 bold italic'
)
label2.pack(side = "top")

Label(frame2,
    text = "Choose a color",
    padx = 20,
).pack(anchor = W)

myVar = StringVar(value = 'GREEN')

Radiobutton(frame2,
    text = "Red",
    padx = 20,
    variable = myVar,
    value = "RED",
    command = radioSelected
).pack(anchor = W)
Radiobutton(frame2,
    text = "Green",
    padx = 20,
    variable = myVar,
    value = 'GREEN',
    command = radioSelected
).pack(anchor = W)
Radiobutton(frame2,
    text = "Blue",
    padx = 20,
    variable = myVar,
    value = 'BLUE',
    command = radioSelected
).pack(anchor = W)

showFrame1()
root.mainloop()