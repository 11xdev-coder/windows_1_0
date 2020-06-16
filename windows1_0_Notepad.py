from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

name = 0

def start_notepad(root):
    save_root = root
    def openfile():
        open_return = filedialog.askopenfile(initialdir='/',title='Select Text file to open',filetypes=(('Text Files','*.txt'),('Documents','*.doc'),('Document files','*.rtf')))
        try:
            for line in open_return:
                inserttext.insert(END,line)
        except:
            messagebox.showwarning('Opening file','Сould not open file')
    def save():
        def opensavefile():
            savefileroot = Tk()
            savefileroot.title(savebtn['text'])
            fopen = open('C:\\Users\\piash\\PycharmProjects\\Windows95\\windows\\%s.txt' % namefile,'r')
            m4042 = Menu(savefileroot)
            ni3 = Menu(m4042, tearoff=False)
            ni3.add_command(label='Delete this file', command=lambda: savebtn.grid_forget())
            ni3.add_separator()
            ni3.add_command(label='Exit', command=lambda: savefileroot.destroy())
            m4042.add_cascade(label='File',menu=ni3)
            savefileroot.config(menu=m4042)
            outputtext = Text(savefileroot)
            outputtext.insert(END,fopen.read())
            outputtext.grid(row=0,column=0)
            savefileroot.mainloop()
        global name
        savebtn = Button(save_root,text='TextFile%s.txt' % name,bg='yellow',activebackground='yellow',command=opensavefile)
        namefile = savebtn['text']
        f = open('C:\\Users\\piash\\PycharmProjects\\Windows95\\windows\\%s.txt' % namefile,'w')
        f.write(inserttext.get(1.0,END))
        savebtn.grid()
        name += 1

    def new():
        inserttext.delete(1.0,END)

    def copy():
        inserttext.clipboard_clear()
        inserttext.clipboard_append(inserttext.selection_get())

    def cut():
        inserttext.clipboard_clear()
        inserttext.clipboard_append(inserttext.selection_get())
        inserttext.delete('sel.first','sel.last')
        inserttext.clipboard_append(inserttext.selection_get())

    def paste():
        inserttext.insert(END,inserttext.clipboard_get())


    window = Tk()
    window.title('Notepad')
    inserttext = Text(window,undo=True)
    m404 = Menu(window)
    ni2 = Menu(m404,tearoff=False)
    ni2.add_command(label='New',command=new)
    ni2.add_command(label='Save', command=save)
    ni2.add_command(label='Open', command=openfile)
    ni2.add_separator()
    ni2.add_command(label='Exit', command=lambda: window.destroy())
    m404.add_cascade(label='File',menu=ni2)
    ni3 = Menu(m404, tearoff=False)
    ni3.add_command(label='Undo', command=lambda: inserttext.edit_undo())
    ni3.add_command(label='Redo', command=lambda: inserttext.edit_redo())
    ni3.add_separator()
    ni3.add_command(label='Copy', command=copy)
    ni3.add_command(label='Cut', command=cut)
    ni3.add_command(label='Paste', command=paste)
    m404.add_cascade(label='Edit', menu=ni3)
    window.config(menu=m404)
    inserttext.grid(row=0,column=0)
    window.mainloop()