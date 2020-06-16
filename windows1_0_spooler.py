from tkinter import *


def start_spooler():
    root = Toplevel()
    root.geometry('900x900')
    root['bg'] = 'white'
    menu = Menu(root)
    ni1 = Menu(menu, tearoff=False)
    ni1.add_radiobutton(label='Low', command=None)
    ni1.add_radiobutton(label='High', command=None)
    ni1.add_separator()
    ni1.add_command(label='Exit', command=lambda: root.destroy())
    menu.add_cascade(menu=ni1, label='Priority')
    ni2 = Menu(menu, tearoff=False)
    ni2.add_command(label='Pause', command=None)
    ni2.add_command(label='Resume', command=None)
    ni2.add_separator()
    ni2.add_command(label='Terminal', command=None)
    menu.add_cascade(menu=ni2, label='Controls')
    root.config(menu=menu)
    root.title('Spooler')
    lbl = Label(root,text='     LPT1 [Active]: HP LaserJet                                                                                                                                                                                                                                                                                                    ',bg='black',fg='white')
    lbl.grid(row=0,column=0)
    root.mainloop()
