
from tkinter import *

nyanroot = Tk()
nyanroot.geometry('1920x1080')
nyan = Canvas(nyanroot,bg='black')
image = PhotoImage(file='C:\\Users\\piash\\Downloads\\index.png')
nyan.create_image(50,50,image=image)
nyan.pack(expand=1,fill=BOTH)
nyanroot.mainloop()


