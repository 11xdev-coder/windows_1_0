from tkinter import *
import time
from tkinter import filedialog
from tkinter import messagebox


n = 0



def start_calendar(root):
    def openncalf():
        a = filedialog.askopenfile(initialdir='/',title='Select calendar file to open',filetypes=(('Calendar Files','*.txt'),('Text Files','*.txt')))
        CalOpenTk = Tk()
        for line in a:
            if '' in line:
                line2 = line
                break
        for line in a:
            if '' in line:
                line3 = line
                break
        for line in a:
            if '' in line:
                line4 = line
                break
        for line in a:
            if '' in line:
                line5 = line
                break
        for line in a:
            if '' in line:
                line6 = line
                break
        for line in a:
            if '' in line:
                line7 = line
                break
        for line in a:
            if '' in line:
                line8 = line
                break
        for line in a:
            if '' in line:
                line9 = line
                break
        for line in a:
            if '' in line:
                line10 = line
                break
        for line in a:
            if '' in line:
                line11 = line
                break
        for line in a:
            if '' in line:
                line12 = line
                break
        for line in a:
            if '' in line:
                line13 = line
                break
        for line in a:
            if '' in line:
                line14 = line
                break
        for line in a:
            if '' in line:
                line15 = line
                break
        for line in a:
            if '' in line:
                line16 = line
                break
        for line in a:
            if '' in line:
                line17 = line
                break
        for line in a:
            if '' in line:
                line18 = line
                break
        try:
            mixedline = line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10 + line11 + line12 + line13 + line14 + line15 + line16 + line17 + line18
            label = Label(CalOpenTk, text=mixedline)
            label.grid(row=0, column=0)
        except:
            messagebox.showwarning(title='Opening file',message='This file is not calendar file. Open other files.')
        menu5 = Menu(CalOpenTk)
        new_item7 = Menu(menu5, tearoff=0)
        new_item7.add_command(label='Close', command=lambda: CalOpenTk.destroy())
        menu5.add_cascade(label='Menu', menu=new_item7)
        CalOpenTk.config(menu=menu5)
        CalOpenTk.title('Calendar.exe - Open file')
        CalOpenTk.mainloop()
    def save():
        def OK():
            def opencalendarfile():
                def delete():
                    Calendarfile.grid_forget()
                CalTk = Tk()
                title = str('Calendar - ') + str(Calendarfile['text'])
                CalTk.title(title)
                menu3 = Menu(CalTk)
                new_item5 = Menu(menu3, tearoff=0)
                new_item5.add_command(label='Close', command=lambda: CalTk.destroy())
                new_item5.add_command(label='Delete this file', command=delete)
                menu3.add_cascade(label='Menu', menu=new_item5)
                CalTk.config(menu=menu3)
                eightsave = Label(CalTk,text=w)
                eightsave.grid(row=0,column=0)
                CalTk.mainloop()
            global n
            SaveAs.destroy()

            n += 1
            textbtn = 'calendarFile%s.cal' % n
            Calendarfile = Button(root_calendar, text=textbtn, command=opencalendarfile, bg='yellow',
                                  activebackground='yellow')
            Calendarfile.grid()
            w = '''8:00 %s
9:00 %s
10:00 %s
11:00 %s
12:00 %s
13:00 %s
14:00 %s
15:00 %s
16:00 %s
17:00 %s
18:00 %s
19:00 %s
20:00 %s
21:00 %s
22:00 %s
23:00 %s
00:00 %s''' % (eighte.get(), ninee.get(),tene.get(),elevene.get(),twelvee.get(),thirteene.get(),fourteene.get(),fifteene.get(),sixteene.get(),seventeene.get(),eighteene.get(),nineteene.get(),twentye.get(),twentyonee.get(),twentytwoe.get(),twentythreee.get(),zerozeroe.get())
            namefile2 = Calendarfile['text']
            ooo = open('C:\\Users\\piash\\PycharmProjects\\Windows95\\windows\\%s.txt' % namefile2, 'w')
            ooo.write(w)


        SaveAs = Tk()
        labelask = Label(SaveAs,text='Are you sure you want to save the file, or does it need improvements?')
        Okbtn = Button(SaveAs, text='OK',command=OK)
        labelask.grid(row=0, column=0)
        Okbtn.grid(row=1, column=1)
        SaveAs.mainloop()
    root_calendar = root
    def CloseCal():
        Cal.destroy()

    Cal = Tk()
    Cal.title('Calendar.exe')
    lblt = Label(Cal, text=time.asctime())
    eight = Label(Cal, text='8:00')
    nine = Label(Cal, text='9:00')
    ten = Label(Cal, text='10:00')
    eleven = Label(Cal, text='11:00')
    twelve = Label(Cal, text='12:00')
    thirteen = Label(Cal, text='13:00')
    fourteen = Label(Cal, text='14:00')
    fifteen = Label(Cal, text='15:00')
    sixteen = Label(Cal, text='16:00')
    seventeen = Label(Cal, text='17:00')
    eighteen = Label(Cal, text='18:00')
    nineteen = Label(Cal, text='19:00')
    twenty = Label(Cal, text='20:00')
    twentyone = Label(Cal, text='21:00')
    twentytwo = Label(Cal, text='22:00')
    twentythree = Label(Cal, text='23:00')
    zerozero = Label(Cal, text='00:00')

    thirteene = Entry(Cal)
    fourteene = Entry(Cal)
    fifteene = Entry(Cal)
    sixteene = Entry(Cal)
    seventeene = Entry(Cal)
    eighteene = Entry(Cal)
    nineteene = Entry(Cal)
    twentye = Entry(Cal)
    twentyonee = Entry(Cal)
    twentytwoe = Entry(Cal)
    twentythreee = Entry(Cal)
    zerozeroe = Entry(Cal)
    eighte = Entry(Cal)
    ninee = Entry(Cal)
    tene = Entry(Cal)
    elevene = Entry(Cal)
    twelvee = Entry(Cal)
    menu2 = Menu(Cal)
    new_item4 = Menu(menu2, tearoff=0)
    new_item4.add_command(label='Close', command=CloseCal)
    new_item4.add_command(label='Save', command=save)
    new_item4.add_command(label='Open', command=openncalf)
    menu2.add_cascade(label='Menu', menu=new_item4)
    Cal.config(menu=menu2)

    lblt.grid(row=0, column=0)
    eight.grid(row=1, column=0)
    nine.grid(row=2, column=0)
    ten.grid(row=3, column=0)
    eleven.grid(row=4, column=0)
    twelve.grid(row=5, column=0)
    eighte.grid(row=1, column=1)
    ninee.grid(row=2, column=1)
    tene.grid(row=3, column=1)
    elevene.grid(row=4, column=1)
    twelvee.grid(row=5, column=1)
    thirteen.grid(row=6, column=0)
    fourteen.grid(row=7, column=0)
    fifteen.grid(row=8, column=0)
    sixteen.grid(row=9, column=0)
    seventeen.grid(row=10, column=0)
    eighteen.grid(row=11, column=0)
    nineteen.grid(row=12, column=0)
    twenty.grid(row=13, column=0)
    twentyone.grid(row=14, column=0)
    twentytwo.grid(row=15, column=0)
    twentythree.grid(row=16, column=0)
    zerozero.grid(row=17, column=0)
    thirteene.grid(row=6, column=1)
    fourteene.grid(row=7, column=1)
    fifteene.grid(row=8, column=1)
    sixteene.grid(row=9, column=1)
    seventeene.grid(row=10, column=1)
    eighteene.grid(row=11, column=1)
    nineteene.grid(row=12, column=1)
    twentye.grid(row=13, column=1)
    twentyonee.grid(row=14, column=1)
    twentytwoe.grid(row=15, column=1)
    twentythreee.grid(row=16, column=1)
    zerozeroe.grid(row=17, column=1)
    while True:
        Cal.update()
        Cal.update_idletasks()
        lblt['text'] = time.asctime()
