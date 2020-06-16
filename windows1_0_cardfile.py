from tkinter import *
from tkinter import filedialog

s = 0

def start_cardfile(root):
    def opencardfilefromotherOS():
        open_return = filedialog.askopenfile(initialdir='/',title='Select Card file to open',filetypes=(('Card Files','*.txt'),('Text Files','*.txt')))
        for line in open_return:
            textinput.insert(END,line)
    def deletecard():
        cardfileroot.destroy()
    def addcard():
        start_cardfile(cardfile)
    def indexline():
       def OKindex():
            indexlinelbl['text'] = ent.get()
       indexlinetk = Tk()
       indexlinetk.title('Index Line')
       lbl = Label(indexlinetk,text='Index line: ')
       ent = Entry(indexlinetk)
       btnOk = Button(indexlinetk,command=OKindex,text='OK')
       btnCancel = Button(indexlinetk,text='Cancel',command=lambda: indexlinetk.destroy())
       lbl.grid(row=0,column=0)
       ent.grid(row=0,column=1)
       btnOk.grid(row=1,column=0)
       btnCancel.grid(row=1,column=1)
       indexlinetk.mainloop()
    cardfile = root
    def savecardfile():
        def OK():
            global s
            global a
            a = textinput.get(1.0,END)
            def opencardfile():
                OpenTk = Tk()
                OpenTk.title(cardFilebtn['text'])
                textopen = Text(OpenTk)
                m2 = Menu(OpenTk)
                ni2 = Menu(m2, tearoff=0)
                ni2.add_command(label='Close', command=lambda: OpenTk.destroy())
                ni2.add_command(label='Delete this file', command=lambda: cardFilebtn.grid_forget())
                m2.add_cascade(menu=ni2, label='Menu')
                OpenTk.config(menu=m2)
                textopen.insert(END,a)
                textopen.grid(row=0,column=0)
                OpenTk.mainloop()

            cardFilebtn = Button(cardfile, text='CardFile%s.crd' % s, command=opencardfile, bg='yellow',
                                 activebackground='yellow')
            cardFilebtn.grid()
            namefile = cardFilebtn['text']
            c = open('C:\\Users\\piash\\PycharmProjects\\Windows95\\windows\\%s.txt' % namefile, 'w')
            c.write(a)
            s += 1
            SaveAs.destroy()

        SaveAs = Tk()
        labelask = Label(SaveAs,text='Are you sure you want to save the file, or does it need improvements?')
        Okbtn = Button(SaveAs, text='OK', command=OK)
        Cancelbtn = Button(SaveAs, text='Cancel', command=lambda: SaveAs.destroy())
        labelask.grid(row=0, column=0)
        Okbtn.grid(row=1, column=1)
        Cancelbtn.grid(row=1, column=2)
        SaveAs.mainloop()
    cardfileroot = Tk()
    m = Menu(cardfileroot)
    ni = Menu(m,tearoff=0)
    ni.add_command(label='Close',command=lambda: cardfileroot.destroy())
    ni.add_command(label='Save', command=savecardfile)
    ni.add_command(label='Open', command=opencardfilefromotherOS)
    ni3 = Menu(m,tearoff=0)
    ni3.add_command(label='Index Line',command=indexline)
    m.add_cascade(menu=ni,label='Menu')
    m.add_cascade(menu=ni3, label='Edit')
    ni4 = Menu(m,tearoff=0)
    ni4.add_command(label='Add',command=addcard)
    ni4.add_command(label='Delete', command=deletecard)
    m.add_cascade(menu=ni4,label='Card')
    cardfileroot.config(menu=m)
    cardfileroot.title('Cardfile.exe')
    textinput = Text(cardfileroot)
    indexlinelbl = Label(cardfileroot,text='')
    textinput.grid(row=1,column=0)
    indexlinelbl.grid(row=0,column=0)
    cardfileroot.mainloop()