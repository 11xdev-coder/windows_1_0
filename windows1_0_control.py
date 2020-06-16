from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import time

def start_control(rootForColor,MSDOSForColor):
    ROOTFORCOLOUR = rootForColor
    MSDOS = MSDOSForColor
    root = Tk()
    root.title('Control')
    lbltime = Label(root,text='Time:')
    seconds = Spinbox(root, from_=1, to=60, width=3)
    seconds.grid(column=2, row=1)
    minutes = Spinbox(root, from_=1, to=60, width=3)
    minutes.grid(column=1, row=1)
    hours = Spinbox(root, from_=1, to=24, width=3)
    lbltime.grid(column=0,row=0)
    hours.grid(column=0, row=1)

    def colors():
        def Okcolor():
            if rootslist.get() == 'Screen Background' and entrycolor.get().rstrip() != '':
                try:
                    ROOTFORCOLOUR['bg'] = entrycolor.get()
                except:
                    messagebox.showwarning(title='Colors',message='Unknown color. Please enter other color')
            elif rootslist.get() == 'MS-DOS Background' and entrycolor.get().rstrip() != '':
                try:
                    MSDOS['bg'] = entrycolor.get()
                except:
                    messagebox.showwarning(title='Colors',message='Unknown color. Please enter other color')
        colorroot = Tk()
        colorroot.title('Screen colors')
        varcolor = IntVar()
        rootslist = Combobox(colorroot,values=('Screen Background','MS-DOS Background'),textvariable=varcolor)
        rootslist.current(0)
        rootslist.grid(row=0,column=0)
        lblcolor = Label(colorroot,text='Enter the color')
        lblcolor.grid(row=1,column=0)
        entrycolor = Entry(colorroot)
        entrycolor.grid(row=1,column=1)
        Okbtncolor = Button(colorroot,text='Ok',command=Okcolor)
        Okbtncolor.grid(row=2,column=0)
        Cancelbtncolor = Button(colorroot,text='Cancel',command=lambda: colorroot.destroy())
        Cancelbtncolor.grid(row=2,column=1)


    def port():
        def OKport():
            if e.get().rstrip() == '':
                messagebox.showwarning(title='Settings',message='Settings could not be set. Check if the data is entered correctly')
            else:
                port.destroy()
                messagebox.showinfo(title='Settings',message='Settings set successfully!')
        port = Tk()
        port.title('Communications Settings')
        lblport = Label(port,text='Port')
        lblport.grid(row=0,column=0)
        coms = IntVar()
        com1 = Radiobutton(port,text='COM1:',value=1,variable=coms)
        com1.grid(row=0,column=1)
        com2 = Radiobutton(port, text='COM2:', value=2, variable=coms)
        com2.grid(row=0, column=2)
        lblbaudrate = Label(port,text='Baud Rate:')
        lblbaudrate.grid(row=1,column=0)
        e = Entry(port)
        e.insert(END,'1200')
        e.grid(row=1,column=1)
        lblword = Label(port,text='Word Length')
        lblword.grid(row=2,column=0)
        lengths = IntVar()
        wordlength1 = Radiobutton(port,text='4',value=1,variable=lengths)
        wordlength1.grid(row=2,column=1)
        wordlength2 = Radiobutton(port, text='5', value=2, variable=lengths)
        wordlength2.grid(row=2, column=2)
        wordlength3 = Radiobutton(port, text='6', value=3, variable=lengths)
        wordlength3.grid(row=2, column=3)
        wordlength4 = Radiobutton(port, text='7', value=4, variable=lengths)
        wordlength4.grid(row=2, column=4)
        wordlength5 = Radiobutton(port, text='8', value=5, variable=lengths)
        wordlength5.grid(row=2, column=5)
        lblparity = Label(port,text='Parity')
        lblparity.grid(row=3,column=0)
        parities = IntVar()
        parityEven = Radiobutton(port,text='Even',value=1,variable=parities)
        parityEven.grid(row=3,column=1)
        parityOdd = Radiobutton(port, text='Odd', value=2, variable=parities)
        parityOdd.grid(row=3, column=2)
        parityNone = Radiobutton(port, text='None', value=3, variable=parities)
        parityNone.grid(row=3, column=3)
        lblStopBits = Label(port,text='Stop Bits')
        lblStopBits.grid(row=4,column=0)
        StopBits = IntVar()
        stopbit1 = Radiobutton(port,text='1',value=1,variable=StopBits)
        stopbit1.grid(row=4,column=1)
        stopbit1_5 = Radiobutton(port,text='1.5',value=2,variable=StopBits)
        stopbit1_5.grid(row=4,column=2)
        stopbit2 = Radiobutton(port,text='2',value=3,variable=StopBits)
        stopbit2.grid(row=4,column=3)
        lblhandshake = Label(port,text='Handshake')
        lblhandshake.grid(row=5,column=0)
        handshakes = IntVar()
        Hardware = Radiobutton(port,text='Hardware',value=1,variable=handshakes)
        Hardware.grid(row=5,column=1)
        Noneware = Radiobutton(port,text='None',value=2,variable=handshakes)
        Noneware.grid(row=5,column=2)
        Okbtnport = Button(port,text='OK',command=OKport)
        Okbtnport.grid(row=6,column=0)
        Cancelbtnport = Button(port,text='Cancel',command=lambda: port.destroy())
        Cancelbtnport.grid(row=6,column=2)



    def printer():
        def OKdefault():
            def destroyyy():
                connectionforprinter.destroy()
                pri.destroy()
            connectionforprinter = Tk()
            connectionforprinter.title('HP LaserJet: Output Mode')
            lbl303 = Label(connectionforprinter,text='Orientation')
            lbl303.grid(row=0,column=0)
            Orientation = IntVar()
            portrait = Radiobutton(connectionforprinter,value=1,text='Portrait',variable=Orientation)
            portrait.grid(row=1,column=0)
            landscape = Radiobutton(connectionforprinter,value=2,text='Landscape',variable=Orientation)
            landscape.grid(row=2,column=0)
            lbl3032 = Label(connectionforprinter,text='Font Cartridge')
            lbl3032.grid(row=0,column=1)
            Font_Cartridge = IntVar()
            noneport = Radiobutton(connectionforprinter, value=1, text='None', variable=Font_Cartridge)
            noneport.grid(row=1, column=1)
            Aport = Radiobutton(connectionforprinter, value=2, text='92286 A', variable=Font_Cartridge)
            Aport.grid(row=2, column=1)
            Bport = Radiobutton(connectionforprinter, value=3, text='92286 B', variable=Font_Cartridge)
            Bport.grid(row=3, column=1)
            Fport = Radiobutton(connectionforprinter, value=4, text='92286 F', variable=Font_Cartridge)
            Fport.grid(row=4, column=1)
            Okbtndefault2 = Button(connectionforprinter,text='Ok',command=destroyyy)
            Okbtndefault2.grid(row=5,column=0)
            Cancelbtndefault2 = Button(connectionforprinter,text='Cancel',command=lambda: connectionforprinter.destroy())
            Cancelbtndefault2.grid(row=5,column=1)

        pri = Tk()
        pri.title('Printer')
        lbl404 = Label(pri,text='Default printer')
        lbl404.grid(row=0,column=0)
        printerslistfordefault = Combobox(pri,values=('HP_LaserJet'))
        printerslistfordefault.current(0)
        printerslistfordefault.grid(row=1,column=0)
        Okbtndefault = Button(pri,text='OK',command=OKdefault)
        Okbtndefault.grid(row=0,column=1)
        Cancelbtndefault = Button(pri,text='Cancel',command=lambda: pri.destroy())
        Cancelbtndefault.grid(row=1,column=1)

    def connections():
        def OKcon():
            printerscon = Combobox(con, values=('HP_LaserJet_on_%s' % (connectionslist.get())))
            printerscon.current(0)
            printerscon.grid(row=1, column=0)
        con = Tk()
        con.title('Connections')
        lbl505 = Label(con,text='Printers')
        lbl505.grid(row=0,column=0)
        lbl5052 = Label(con,text='Connections')
        lbl5052.grid(row=0,column=1)
        connectionslist = Combobox(con, values=('None','LPT1','LPT2','LPT3','COM1','COM2'))
        connectionslist.current(1)
        connectionslist.grid(row=1,column=1)
        printerscon = Combobox(con, values=('HP_LaserJet_on_%s' % (connectionslist.get())))
        printerscon.current(0)
        printerscon.grid(row=1, column=0)
        OKbtncon = Button(con,text='OK',command=OKcon)
        OKbtncon.grid(row=2,column=0)
        Cancelbtncon = Button(con,text='Cancel',command=lambda: con.destroy())
        Cancelbtncon.grid(row=2,column=1)

    def deletefont():
        def deletefontv2():
            if entrywithfont.get() == 'Courier 8,10,12 (Set#2)' and fonts.get() == 'Courier 8,10,12 (Set#2)' or entrywithfont.get() == 'Courier 8,10,12 (Set#3)' and fonts.get() == 'Courier 8,10,12 (Set#3)' or entrywithfont.get() == 'Helv 8,10,12 (Set#2)' and fonts.get() == 'Helv 8,10,12 (Set#2)' or entrywithfont.get() == 'Helv 8,10,12 (Set#3)' and fonts.get() == 'Helv 8,10,12 (Set#3)' or entrywithfont.get() == 'System,terminal 8,10,12 (Set#2)' and fonts.get() == 'System,terminal 8,10,12 (Set#2)' or entrywithfont.get() == 'System,terminal 8,10,12 (Set#3)' and fonts.get() == 'System,terminal 8,10,12 (Set#3)' or entrywithfont.get() == 'Modern 8,10,12 (Set#1)' and fonts.get() == 'Modern 8,10,12 (Set#1)' or entrywithfont.get() == 'Roman 8,10,12 (Set#1)' and fonts.get() == 'Roman 8,10,12 (Set#1)' or entrywithfont.get() == 'Script 8,10,12 (Set#1)' and fonts.get() == 'Script 8,10,12 (Set#1)' or entrywithfont.get() == 'Tms Rmn 8,10,12 (Set#2)' and fonts.get() == 'Tms Rmn 8,10,12 (Set#2)' or entrywithfont.get() == 'Tms Rmn 8,10,12 (Set#3)' and fonts.get() == 'Tms Rmn 8,10,12 (Set#3)':
                def yes():
                    if entrydeletefont.get() == 'A:/' or entrydeletefont.get() == 'D:/' or entrydeletefont.get() == 'C:/' or entrydeletefont.get() == 'Z:/':
                        delete3.destroy()
                        delete4.destroy()
                        messagebox.showwarning(title='Remove',message='Font removed successfully!')
                    else:
                        pass
                def no():
                    delete3.destroy()
                    delete4.destroy()
                delete4 = Tk()
                delete4.title('Delete font')
                lbl6 = Label(delete4, text='Delete associated font file %s.fon\n from drive/directory' % (fonts.get()))
                lbl6.grid(row=0, column=0)
                entrydeletefont = Entry(delete4)
                entrydeletefont.grid(row=1, column=0)
                yesbtndelete = Button(delete4, text='Yes', command=yes)
                yesbtndelete.grid(row=2, column=0)
                nobtndelete = Button(delete4, text='No', command=no)
                nobtndelete.grid(row=2, column=1)
                cancelbtncopydelete = Button(delete4, text='Cancel', command=lambda: delete4.destroy())
                cancelbtncopydelete.grid(row=2, column=2)
            else:
                print(fonts.get())
                print(entrywithfont.get())

        delete3 = Tk()
        delete3.title('Delete font')
        lbl4 = Label(delete3, text='Delete font')
        lbl4.grid(row=0, column=0)
        fonts = Combobox(delete3)
        fonts['values'] = ('Courier 8,10,12 (Set#2)','Courier 8,10,12 (Set#3)','Helv 8,10,12 (Set#2)','Helv 8,10,12 (Set#3)','System,terminal 8,10,12 (Set#2)','System,terminal 8,10,12 (Set#3)','Modern 8,10,12 (Set#1)','Roman 8,10,12 (Set#1)','Script 8,10,12 (Set#1)','Tms Rmn 8,10,12 (Set#2)','Tms Rmn 8,10,12 (Set#3)')
        fonts.current(0)
        fonts.grid(row=1, column=0)
        lbl5 = Label(delete3, text='Font File:')
        lbl5.grid(row=0, column=1)
        entrywithfont = Entry(delete3)
        entrywithfont.grid(row=0, column=2)
        deletebtn = Button(delete3, text='Delete', command=deletefontv2)
        deletebtn.grid(row=2, column=1)
        Cancelbtn = Button(delete3, text='Cancel', command=lambda: delete3.destroy())
        Cancelbtn.grid(row=2, column=2)

    def deleteprinter():
        def deleteprinterv2():
            if entrywithprinter.get() == 'HP_LaserJet_on_LPT1':
                def yes():
                    if entrydeleteprinter.get() == 'A:/' or entrydeleteprinter.get() == 'D:/' or entrydeleteprinter.get() == 'C:/' or entrydeleteprinter.get() == 'Z:/':
                        delete1.destroy()
                        delete2.destroy()
                        messagebox.showwarning(title='Remove',message='Printer removed successfully!')
                    else:
                        pass
                def no():
                    delete1.destroy()
                    delete2.destroy()
                delete2 = Tk()
                delete2.title('Delete printer')
                lbl6 = Label(delete2, text='Delete associated printer file HP_LaserJet_on_LPT1.drv\n from drive/directory')
                lbl6.grid(row=0, column=0)
                entrydeleteprinter = Entry(delete2)
                entrydeleteprinter.grid(row=1, column=0)
                yesbtndelete = Button(delete2, text='Yes', command=yes)
                yesbtndelete.grid(row=2, column=0)
                nobtndelete = Button(delete2, text='No', command=no)
                nobtndelete.grid(row=2, column=1)
                cancelbtncopydelete = Button(delete2, text='Cancel', command=lambda: delete2.destroy())
                cancelbtncopydelete.grid(row=2, column=2)
            else:
                pass

        delete1 = Tk()
        delete1.title('Delete printer')
        lbl4 = Label(delete1, text='Delete printer')
        lbl4.grid(row=0, column=0)
        printers = Combobox(delete1)
        printers['values'] = ('HP_LaserJet_on_LPT1')
        printers.current(0)
        printers.grid(row=1, column=0)
        lbl5 = Label(delete1, text='Printer File:')
        lbl5.grid(row=0, column=1)
        entrywithprinter = Entry(delete1)
        entrywithprinter.grid(row=0, column=2)
        deletebtn = Button(delete1, text='Delete', command=deleteprinterv2)
        deletebtn.grid(row=2, column=1)
        Cancelbtn = Button(delete1, text='Cancel', command=lambda: delete1.destroy())
        Cancelbtn.grid(row=2, column=2)

    def addnewfont():
        def OK():
            def add():
                if entrywithfont.get() == 'Courier 8,10,12 (Set#2)' and fonts.get() == 'Courier 8,10,12 (Set#2)' or entrywithfont.get() == 'Courier 8,10,12 (Set#3)' and fonts.get() == 'Courier 8,10,12 (Set#3)' or entrywithfont.get() == 'Helv 8,10,12 (Set#2)' and fonts.get() == 'Helv 8,10,12 (Set#2)' or entrywithfont.get() == 'Helv 8,10,12 (Set#3)' and fonts.get() == 'Helv 8,10,12 (Set#3)' or entrywithfont.get() == 'System,terminal 8,10,12 (Set#2)' and fonts.get() == 'System,terminal 8,10,12 (Set#2)' or entrywithfont.get() == 'System,terminal 8,10,12 (Set#3)' and fonts.get() == 'System,terminal 8,10,12 (Set#3)' or entrywithfont.get() == 'Modern 8,10,12 (Set#1)' and fonts.get() == 'Modern 8,10,12 (Set#1)' or entrywithfont.get() == 'Roman 8,10,12 (Set#1)' and fonts.get() == 'Roman 8,10,12 (Set#1)' or entrywithfont.get() == 'Script 8,10,12 (Set#1)' and fonts.get() == 'Script 8,10,12 (Set#1)' or entrywithfont.get() == 'Tms Rmn 8,10,12 (Set#2)' and fonts.get() == 'Tms Rmn 8,10,12 (Set#2)' or entrywithfont.get() == 'Tms Rmn 8,10,12 (Set#3)' and fonts.get() == 'Tms Rmn 8,10,12 (Set#3)':
                    def yes():
                        messagebox.showwarning(title='Control Panel',message='Cannot copy file to itself.')
                    def no():
                        add4.destroy()
                        add5.destroy()
                    add5 = Tk()
                    add5.title('Add font')
                    lbl3 = Label(add5,text='Copy associated font file %s.fon\nto drive/directory' % (fonts.get()))
                    lbl3.grid(row=0,column=0)
                    entrywithdrivetocopy = Entry(add5)
                    entrywithdrivetocopy.grid(row=1,column=0)
                    yesbtn = Button(add5,text='Yes',command=yes)
                    yesbtn.grid(row=2,column=0)
                    nobtn = Button(add5,text='No',command=no)
                    nobtn.grid(row=2,column=1)
                    cancelbtncopy = Button(add5,text='Cancel',command=lambda: add5.destroy())
                    cancelbtncopy.grid(row=2,column=2)
            if entrywithdrive2.get() == 'A:/' or entrywithdrive2.get() == 'C:/' or entrywithdrive2.get() == 'Z:/' or entrywithdrive2.get() == 'D:/':
                add3.destroy()
                add4 = Tk()
                add4.title('Add font')
                lbl1 = Label(add4,text='Available fonts')
                lbl1.grid(row=0,column=0)
                var2 = IntVar()
                fonts = Combobox(add4,textvariable=var2)
                fonts['values'] = ('Courier 8,10,12 (Set#2)','Courier 8,10,12 (Set#3)','Helv 8,10,12 (Set#2)','Helv 8,10,12 (Set#3)','System,terminal 8,10,12 (Set#2)','System,terminal 8,10,12 (Set#3)','Modern 8,10,12 (Set#1)','Roman 8,10,12 (Set#1)','Script 8,10,12 (Set#1)','Tms Rmn 8,10,12 (Set#2)','Tms Rmn 8,10,12 (Set#3)')
                fonts.current(0)
                fonts.grid(row=1,column=0)
                lbl2 = Label(add4,text='Font File:')
                lbl2.grid(row=0,column=1)
                entrywithfont = Entry(add4)
                entrywithfont.grid(row=0,column=2)
                addbtn = Button(add4,text='Add',command=add)
                addbtn.grid(row=2,column=1)
                Cancelbtn = Button(add4,text='Cancel',command=lambda: add4.destroy())
                Cancelbtn.grid(row=2,column=2)
            else:
                messagebox.showwarning(title='Wrong name of drive!', message='Wrong name of driver! Enter other drives')
        add3 = Tk()
        add3.title('Add font')
        lblfont = Label(add3,text='Insert the disk with the font file\nyou wish to add into drive A, or choose\nan alternative drive/directory:')
        entrywithdrive2 = Entry(add3)
        Okbtn = Button(add3,text='OK',command=OK)
        Cancelbtn = Button(add3, text='Cancel', command=lambda: add3.destroy())
        Okbtn.grid(row=2,column=0)
        Cancelbtn.grid(row=2,column=1)
        lblfont.grid(row=0,column=0)
        entrywithdrive2.grid(row=1,column=0)

    def addnewprinter():
        def OK():
            def add():
                if entrywithprinter.get() == 'HP_LaserJet':
                    def yes():
                        messagebox.showwarning(title='Control Panel',message='Cannot copy file to itself.')
                    def no():
                        add2.destroy()
                        add3.destroy()
                    add3 = Tk()
                    add3.title('Add printer')
                    lbl3 = Label(add3,text='Copy associated printer file HP_LaserJet.drv\nto drive/directory')
                    lbl3.grid(row=0,column=0)
                    entrywithdrivetocopy = Entry(add3)
                    entrywithdrivetocopy.grid(row=1,column=0)
                    yesbtn = Button(add3,text='Yes',command=yes)
                    yesbtn.grid(row=2,column=0)
                    nobtn = Button(add3,text='No',command=no)
                    nobtn.grid(row=2,column=1)
                    cancelbtncopy = Button(add3,text='Cancel',command=lambda: add3.destroy())
                    cancelbtncopy.grid(row=2,column=2)
            if entrywithdrive.get() == 'A:/' or entrywithdrive.get() == 'C:/' or entrywithdrive.get() == 'Z:/' or entrywithdrive.get() == 'D:/':
                add1.destroy()
                add2 = Tk()
                add2.title('Add printer')
                lbl1 = Label(add2,text='Available printers')
                lbl1.grid(row=0,column=0)
                printers = Combobox(add2)
                printers['values'] = ('HP_LaserJet')
                printers.current(0)
                printers.grid(row=1,column=0)
                lbl2 = Label(add2,text='Printer File:')
                lbl2.grid(row=0,column=1)
                entrywithprinter = Entry(add2)
                entrywithprinter.grid(row=0,column=2)
                addbtn = Button(add2,text='Add',command=add)
                addbtn.grid(row=2,column=1)
                Cancelbtn = Button(add2,text='Cancel',command=lambda: add2.destroy())
                Cancelbtn.grid(row=2,column=2)
            else:
                messagebox.showwarning(title='Wrong name of drive!', message='Wrong name of driver! Enter other drives')
        add1 = Tk()
        add1.title('Add printer')
        lblprint = Label(add1,text='Insert the disk with printer file\nyou wish to add into drive A, or choose\nan alternative drive/directory:')
        entrywithdrive = Entry(add1)
        Okbtn = Button(add1,text='OK',command=OK)
        Cancelbtn = Button(add1, text='Cancel', command=lambda: add1.destroy())
        Okbtn.grid(row=2,column=0)
        Cancelbtn.grid(row=2,column=1)
        lblprint.grid(row=0,column=0)
        entrywithdrive.grid(row=1,column=0)


    lbldate = Label(root, text='Date:')
    years = Spinbox(root, from_=1500, to=5000, width=5)
    years.grid(column=3, row=1)
    monthes = Spinbox(root, from_=1, to=12, width=3)
    monthes.grid(column=4, row=1)
    days = Spinbox(root, from_=1, to=31, width=3)
    lbldate.grid(column=3, row=0)
    days.grid(column=5, row=1)
    menu9 = Menu(root)
    new_item9 = Menu(menu9, tearoff=0)
    new_item9.add_command(label='Close', command=lambda: root.destroy())
    menu9.add_cascade(label='Menu', menu=new_item9)
    root.config(menu=menu9)
    new_item10 = Menu(menu9,tearoff=False)
    new_item10.add_command(label='Add new printer...', command=addnewprinter)
    new_item10.add_command(label='Delete printer...', command=deleteprinter)
    new_item10.add_command(label='Add new font...', command=addnewfont)
    new_item10.add_command(label='Delete font...', command=deletefont)
    menu9.add_cascade(label='Installation',menu=new_item10)
    new_item11 = Menu(menu9, tearoff=False)
    new_item11.add_command(label='Connections...', command=connections)
    new_item11.add_command(label='Printer...', command=printer)
    new_item11.add_command(label='Communications port...', command=port)
    menu9.add_cascade(label='Setup', menu=new_item11)

    new_item12 = Menu(menu9, tearoff=False)
    new_item12.add_command(label='Screen colors...', command=colors)
    menu9.add_cascade(label='Preferences', menu=new_item12)

    root.config(menu=menu9)

    def test(event):
        testbutton['state'] = 'disable'
        testbutton['bg'] = 'black'
        root.update()
        root.update_idletasks()
        time.sleep(0.5)
        testbutton['state'] = 'active'
        testbutton['bg'] = 'white'
        root.update()
        root.update_idletasks()

    lbldoubc = Label(root,text='Double click')
    lbldoubc.grid(row=2,column=3)
    doublecspeed = Spinbox(root,from_=1,to=5,width=5)
    testbutton = Button(root,text='TEST')
    doublecspeed.grid(row=3,column=3)
    testbutton.grid(row=4,column=3)
    testbutton.bind('<Double-Button-1>',test)

    lblblick = Label(root, text='Cursor blink')
    lblblick.grid(row=2,column=0)
    var = IntVar()
    var.set(6)
    blinkspeed = Spinbox(root, from_=1, to=7, width=5,textvariable=var)
    blinkcursor = Label(root,text='|')
    blinkspeed.grid(row=3,column=0)
    blinkcursor.grid(row=4,column=0)
    while True:
        if var.get() == 1:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(2)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(2)
        elif var.get() == 2:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(1.5)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(1.5)
        elif var.get() == 3:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(1)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(1)
        elif var.get() == 4:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(0.9)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(0.9)
        elif var.get() == 5:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(0.5)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(0.5)
        elif var.get() == 6:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(0.1)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(0.1)
        elif var.get() == 7:
            blinkcursor['text'] = ''
            root.update()
            root.update_idletasks()
            time.sleep(0.05)
            blinkcursor['text'] = '|'
            root.update()
            root.update_idletasks()
            time.sleep(0.05)
        else:
            root.update()
            root.update_idletasks()