from tkinter import *
from tkinter import messagebox

root = Tk()
root['bg'] = 'red'
root.title('Windows is locked!')

def inlock():
    if entry.get() == '_xX12084651611100958Xx_':
        root.destroy()
    else:
        entry.delete(0,END)
        messagebox.showerror('Error', 'Incorrect password!')

def noexit():
   messagebox.showerror('Error','Incorrect password!')

Label(root,text='Your windows is locked!',font=('Helvetica'),bg='purple').pack()
btn = Button(root,text='Inlock',bg='green',activebackground='green',command=inlock)
root.protocol('WM_delete_window',noexit)
entry = Entry(root)

entry.pack()
btn.pack()

root.mainloop()

