from tkinter import *
from math import *
root = Tk()
root.geometry('544x345')
value = StringVar()
def opt():
    # global value

    # print(f'The result is {eval(value.get())}')
    Label(root,text=f'The result is {eval(value.get())}',font='a 30').pack()
    # exit()
Entry(root,bg='black',fg='white',textvariable=value ,font='a 50').pack()
#click on the button to get the output
Button(text='Submit',fg='red',command=opt, font='a 14').pack()
root.configure(bg='lightgreen')
mainloop()

