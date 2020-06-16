from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
import sys
from windows import windows1_0_calc
from windows import windows1_0_load
from windows import windows1_0_ABC
from windows import windows1_0_calendar
from windows import windows1_0_cardfile
from windows import windows1_0_command
from windows import windows1_0_clipbrd
from windows import windows1_0_control
from windows import windows1_0_Notepad
from windows import windows1_0_paint
from windows import windows1_0_tictactoe
from windows import windows1_0_spooler
from windows import windows1_0_write

# iconify / deiconify - свернуть / развернуть окно
#    title - заголовок окна
#    overrideredirect - указание оконному менеджеру игнорировать это окно. Аргументом является True или False. В случае, если аргумент не указан - получаем текущее значение. Если аргумент равен True, то такое окно будет показано оконным менеджером без обрамления (без заголовка и бордюра). Может быть использовано, например, для создания splashscreen при старте программы.
#    iconify / deiconify - свернуть / развернуть окно
#   withdraw - "спрятать" (сделать невидимым) окно. Для того, чтобы снова показать его, надо использовать метод deiconify.
#    minsize и maxsize - минимальный / максимальный размер окна. Методы принимают два аргумента - ширина и высота окна. Если аргументы не указаны - возвращают текущее значение.
#    state - получить текущее значение состояния окна. Может возвращать следующие значения: normal (нормальное состояние), icon (показано в виде иконки), iconic (свёрнуто), withdrawn (не показано), zoomed (развёрнуто на полный экран, только для Windows и Mac OS X)
#    resizable - может ли пользователь изменять размер окна. Принимает два аргумента - возможность изменения размера по горизонтали и по вертикали. Без аргументов возвращает текущее значение.
#    geometry - устанавливает геометрию окна в формате ширинаxвысота+x+y (пример: geometry("600x400+40+80") - поместить окно в точку с координатам 40,80 и установить размер в 600x400). Размер или координаты могут быть опущены (geometry("600x400") - только изменить размер, geometry("+40+80") - только переместить окно).
#   transient - сделать окно зависимым от другого окна, указанного в аргументе. Будет сворачиваться вместе с указанным окном. Без аргументов возвращает текущее значение.
#    protocol - получает два аргумента: название события и функцию, которая будет вызываться при наступлении указанного события. События могут называться WM_TAKE_FOCUS (получение фокуса), WM_SAVE_YOURSELF (необходимо сохраниться, в настоящий момент является устаревшим), WM_DELETE_WINDOW (удаление окна).
#    tkraise (синоним lift) и lower - поднимает (размещает поверх всех других окон) или опускает окно. Методы могут принимать один необязательный аргумент: над/под каким окном разместить текущее.
#    grab_set - устанавливает фокус на окно, даже при наличии открытых других окон
#    grab_release - снимает монопольное владение фокусом ввода с окна

root = Tk()
root['bg'] = 'green'
root.geometry('1900x1200+0+0')
root.title('Windows 1.0')
root.resizable(False, False)
Run_Entry = Entry
pb = ttk.Progressbar(root, length=2000)
pb.pack()
pb.grid(column=0, row=0)


# defSaveCal ():
#     SaveAs = Tk()
#     nameask = Entry(SaveAs)
#     labelask = Label(SaveAs, text='Name:')
#     labelask.grid(row=0, column=0)
#     nameask.grid(row=0, column=1)
#     SaveAs.mainloop()


def start():
    root.config(cursor='watch red')
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    pb.step(10)
    time.sleep(1)
    root.update()
    root.config(cursor='')

    def controlstart():
        windows1_0_control.start_control(root,MS_DOS_start)

    def clipbrdstart():
        windows1_0_clipbrd.start_clipbrd()

    def commandstart():
        windows1_0_command.start_command()

    def cardstart():
        windows1_0_cardfile.start_cardfile(MS_DOS_start)

    def calendarstart():
        windows1_0_calendar.start_calendar(MS_DOS_start)

    def caalculatorstart():
        windows1_0_calc.start_calc()

    def abc():
        windows1_0_ABC.startABC()

    def about():
        messagebox.showinfo('About Windows 1.0',
                            'Microsoft Windows \n MS-DOS Executive \n Version 1.01 \n Copyright @ 1985, \n Microsoft Corp.')

    def close():
        MS_DOS_start.destroy()

    def zoom():
        def zoomno():
            MS_DOS_start.deiconify()
            Ms_dos_deiconify.grid_forget()

        MS_DOS_start.iconify()
        Ms_dos_deiconify = Button(root, text='Deiconify MS_DOS', command=zoomno,bg='green',activebackground='green')
        Ms_dos_deiconify.grid(row=2, column=0)

    def set_name():
        set_vn = Tk()
        set_vn.title('Set volume name')

        def OKsett():
            disk['text'] = 'A:' + str(entry.get()) + '/'

        def Cancelsett():
            set_vn.destroy()

        label = Label(set_vn, text='Set volume name:')
        entry = Entry(set_vn, width=20)
        Okset = Button(set_vn, text='Ok', command=OKsett)
        Cancelset = Button(set_vn, text='Cancel', command=Cancelsett)

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        Okset.grid(row=1, column=1)
        Cancelset.grid(row=1, column=2)

        set_vn.mainloop()

    def load():
        windows1_0_load.start_load()

    def run():
        def OK():
            if Run_Entry.get() == "Close":
                MS_DOS_start.destroy()
                runTk.destroy()

        def Cancel():
            runTk.destroy()

        runTk = Tk()
        runTk.title('Run')
        runTk.geometry('700x200')
        Run_Entry = Entry(runTk)
        Run_label = Label(runTk, text='Run:')
        OK = Button(runTk, text='OK', command=OK)
        Cancelbtn = Button(runTk, text='Cancel', command=Cancel)
        OK.grid(row=1, column=1)
        Run_Entry.grid(row=0, columnspan=4, column=1)
        Cancelbtn.grid(row=1, column=3)
        Run_label.grid(row=0, column=0)

    def Ends():
        MS_DOS_start.destroy()
        root.config(cursor='watch')
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        pb.step(10)
        time.sleep(1)
        root.update()
        root.config(cursor='')
        root.destroy()
        sys.exit()

    MS_DOS_start = Tk()
    MS_DOS_start['bg'] = 'yellow'
    MS_DOS_start.title('MS-DOS Executive')
    MS_DOS_start.geometry('1000x800')
    disk = Label(MS_DOS_start, text='A:WIN101/', font=('Helvetica', 15, 'bold'),bg='yellow')
    ABC = Button(MS_DOS_start, text='ABC.txt', command=abc,bg='yellow',activebackground='yellow')
    Calculator = Button(MS_DOS_start, text='Calc.exe', command=caalculatorstart,bg='yellow',activebackground='yellow')
    Calendar = Button(MS_DOS_start, text='Calendar.exe', command=calendarstart,bg='yellow',activebackground='yellow')
    Card = Button(MS_DOS_start, text='Cardfile.exe', command=cardstart,bg='yellow',activebackground='yellow')
    Command = Button(MS_DOS_start, text='Command.com', command=commandstart, bg='yellow', activebackground='yellow')
    Clipbrd = Button(MS_DOS_start, text='Clipbrd.exe', command=clipbrdstart, bg='yellow', activebackground='yellow')
    Control = Button(MS_DOS_start, text='Control.exe', command=controlstart, bg='yellow', activebackground='yellow')
    MS_DOS_btn = Button(MS_DOS_start, text='MSDOS.exe', command=start, bg='yellow', activebackground='yellow')
    MS_DOSD_btn = Button(MS_DOS_start, text='MSDOSD.exe', command=None, bg='yellow', activebackground='yellow')
    Notepad = Button(MS_DOS_start, text='Notepad.exe', command=lambda: windows1_0_Notepad.start_notepad(MS_DOS_start), bg='yellow', activebackground='yellow')
    Paint = Button(MS_DOS_start, text='Paint.exe', command=lambda: windows1_0_paint.start_mspaint(MS_DOS_start),bg='yellow', activebackground='yellow')
    Tictactoe = Button(MS_DOS_start, text='Revesi.exe', command=lambda: windows1_0_tictactoe.start_tictactoe(),bg='yellow', activebackground='yellow')
    Spooler = Button(MS_DOS_start, text='Spooler.exe', command=lambda: windows1_0_spooler.start_spooler(),bg='yellow', activebackground='yellow')
    Write = Button(MS_DOS_start, text='Write.exe', command=lambda: windows1_0_write.start_write(MS_DOS_start), bg='yellow',activebackground='yellow')


    menu = Menu(MS_DOS_start)
    new_item = Menu(menu, tearoff=0)
    new_item.add_command(label='Run', command=run)
    new_item.add_command(label='Load', command=load)
    menu.add_cascade(label='File', menu=new_item)
    MS_DOS_start.config(menu=menu)

    new_item2 = Menu(menu, tearoff=0)
    new_item2.add_command(label='End Session', command=Ends)
    new_item2.add_command(label='Set volume name', command=set_name)
    menu.add_cascade(label='Special', menu=new_item2)
    MS_DOS_start.config(menu=menu)
    disk.grid(row=0, column=0)
    ABC.grid(row=1, column=0)
    Calculator.grid(row=2, column=0)
    Calendar.grid(row=3, column=0)
    Card.grid(row=4, column=0)
    Command.grid(row=5, column=0)
    Clipbrd.grid(row=6, column=0)
    Control.grid(row=7, column=0)
    MS_DOS_btn.grid(row=8, column=0)
    MS_DOSD_btn.grid(row=9, column=0)
    Notepad.grid(row=10, column=0)
    Paint.grid(row=11, column=0)
    Tictactoe.grid(row=12, column=0)
    Spooler.grid(row=13, column=0)
    Write.grid(row=14, column=0)

    new_item3 = Menu(menu, tearoff=0)
    new_item3.add_command(label='Zoom', command=zoom)
    new_item3.add_command(label='Close', command=close)
    new_item3.add_separator()
    new_item3.add_command(label='About...', command=about)
    menu.add_cascade(label='Menu', menu=new_item3)
    MS_DOS_start.config(menu=menu)

    MS_DOS_start.mainloop()

MS_DOS_EXECUTIVE_IMAGE = PhotoImage(file='Screenshot_1.png')
MS_DOS_Executive = Button(root, text='MS-DOS Executive', command=start,bg='green',activebackground='green',image=MS_DOS_EXECUTIVE_IMAGE)

MS_DOS_Executive.grid(row=1, column=0)
root.mainloop()

