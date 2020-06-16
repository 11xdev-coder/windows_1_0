from tkinter import *

def startABC():
    def CloseABC():
        Abc.destroy()


    Abc = Tk()
    Abc.title('ABC.txt')
    text = Text(Abc)
    menu2 = Menu(Abc)
    text.insert(INSERT, 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
    new_item4 = Menu(menu2, tearoff=0)
    new_item4.add_command(label='Close', command=CloseABC)
    menu2.add_cascade(label='Menu', menu=new_item4)
    Abc.config(menu=menu2)
    text.grid()
    Abc.mainloop()