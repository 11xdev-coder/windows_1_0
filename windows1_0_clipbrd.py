from tkinter import *

def start_clipbrd():
    root = Tk()
    root.title('Clipboard')
    entry = Entry(root,state='disable')
    lbl = Label(root,text='')
    try:
        lbl['text'] = entry.clipboard_get()
    except:
        lbl['text'] = 'Clipboard is empty'
    menu10 = Menu(root)
    ni10 = Menu(menu10,tearoff=False)
    ni10.add_command(label='Close',command=lambda: root.destroy())
    menu10.add_cascade(label='Menu',menu=ni10)
    lbl.grid(row=0,column=0)
    root.config(menu=menu10)
    root.mainloop()