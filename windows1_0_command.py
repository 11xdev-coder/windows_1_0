from tkinter import *
import time,sys

def start_command():
    def pr(event):
        if comen.get() == 'exit':
            comen.config(state='disable')
            root.title('(Command)')
            menu9 = Menu(root)
            new_item9 = Menu(menu9, tearoff=0)
            new_item9.add_command(label='Close', command=lambda: root.destroy())
            menu9.add_cascade(label='Menu', menu=new_item9)
            root.config(menu=menu9)
        elif comen.get() == 'C:>':
            comen.delete(0,END)
            worklbl['text'] = 'C:>'
        elif comen.get() == 'cd windows' and worklbl['text'] == 'C:>':
            comen.delete(0, END)
            worklbl['text'] = 'C:>windows'
        elif comen.get() == 'del System32' and worklbl['text'] == 'C:>windows':
            comen.delete(0, END)
            worklbl['text'] = 'C:>windows\del System32'
            time.sleep(2)
            print('There is a problem on your PC')
            print('She needed to be eliminated')
            print('And so your OS was destroyed')
            sys.exit()
        else:
            comen.delete(0,END)
            comen.insert(END,'Invalid your input')
    root = Tk()
    root.title('Command')
    lbl = Label(root,text='Microsoft(R)    MS-DOS(R)     Version 3.30 \n                                                (C)Copyright Microsoft Corp 1981-1987')
    worklbl = Label(root,text='A:> ')
    comen = Entry(root)
    lbl.grid(row=0,column=0)
    worklbl.grid(row=1,column=0)
    comen.grid(row=2,column=0)
    root.bind('<KeyPress-Return>',pr)
    root.mainloop()