from tkinter import *

root = Tk()
root.title("Калькулятор")
root.geometry('380x550+200+100')

def enterNumber(x):
    if entry_box.get() == '0':
        entry_box.delete(0,'end')
        entry_box.insert(0,str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length,str(x))

entry_box = Entry(font='verdana 14 bold',width=22,bd=6,justify=RIGHT)
entry_box.insert(0,'0')
entry_box.place(x=30,y=10)

btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(width=4,text=str(i), bd=6,command=lambda x=i: enterNumber(x)))

btn_text = 1
for i in range(0,3):
    for j in range(0,3):
        btn_numbers[btn_text].place(x=30+j*90,y=70+i*70)
        btn_text += 1






root.mainloop()