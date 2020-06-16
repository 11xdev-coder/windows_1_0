from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PIL
from PIL import ImageGrab,Image

name = 0
mode = 'pencil'
brush_size = 3
color = 'black'

def start_mspaint(root):
    save_root = root

    def selectrubber():
        global mode
        global color
        color = 'white'
        mode = 'rubber'
        btnbrush['image'] = imgbrush
        btnpencil['image'] = imgpencil
        btnrubber['image'] = imgselectedrubber


    def selectbrush():
        global mode
        global color
        mode = 'brush'
        color = 'black'
        btnbrush['image'] = imgselectedbrush
        btnpencil['image'] = imgpencil
        btnrubber['image'] = imgrubber


    def selectpencil():
        global mode
        global brush_size
        global color
        brush_size = 3
        mode = 'pencil'
        color = 'black'
        btnbrush['image'] = imgbrush
        btnpencil['image'] = imgselectedpencil
        btnrubber['image'] = imgrubber

    def selectwidth():
        global brush_size
        global mode
        if mode == 'brush' or mode == 'rubber':
            def changeW(e):
                global brush_size
                brush_size = int(e)
                widthroot.destroy()
            widthroot = Tk()
            slider = Scale(widthroot,from_=1,to=100,orient=HORIZONTAL)
            slider.grid(row=0,column=1)
            okbtn = Button(widthroot,command=lambda: changeW(slider.get()),text='OK')
            okbtn.grid(row=0,column=0)
            widthroot.mainloop()
        else:
            messagebox.showinfo('Paint','To change the width of the brush, you need to choose not a pencil but a brush')


    def paint(event):
        x1 = event.x + brush_size
        y1 = event.y + brush_size
        x2 = event.x - brush_size
        y2 = event.y - brush_size
        c.create_oval(x1,y1,x2,y2,fill=color,outline=color)

    def openfile():
        open_return = filedialog.askopenfile(initialdir='/',title='Select Text file to open',filetypes=(('Portable Network Graphics','*.png'),('Graphics Interchange Format','*.gif'),('Joint Photographic Experts Group','*.jpeg')))
        img = Image.open(open_return.name)
        img.show()

    def savefile():
        def openmenu(event):
            def delete():
                savebtn.grid_forget()
                menudelete.destroy()
            menudelete = Toplevel()
            menudelete.title('Deleting menu')
            menudelete.geometry('+{}+{}'.format(event.x,event.y))
            btndelete = Button(menudelete,command=delete,text='Delete this file')
            btndelete.grid(row=0,column=0)
            menudelete.mainloop()

        def opensavefile():
            img = Image.open('C:\\Users\\piash\\PycharmProjects\\Windows95\\windows\\%s.gif' % (namefile))
            img.show()

        global name
        savebtn = Button(save_root, text='MSPaintFile%s.msp' % name, bg='yellow', activebackground='yellow',command=opensavefile)
        savebtn.bind('<Button-3>',openmenu)
        savebtn.grid()
        namefile = savebtn['text']
        x1 = mspaintroot.winfo_rootx() + c.winfo_x()
        y1 = mspaintroot.winfo_rooty() + c.winfo_y()
        x2 = x1 + c.winfo_width()
        y2 = y1 + c.winfo_height()

        PIL.ImageGrab.grab().crop((x1,y1,x2,y2)).save('C:\\Users\\piash\\PycharmProjects\\Windows95\\windows\\%s.gif' % (namefile))

        name += 1

    mspaintroot = Toplevel()
    mspaintroot.title('Paint')
    menu = Menu(mspaintroot)
    ni1 = Menu(menu,tearoff=False)
    ni1.add_command(label='New',command=lambda: c.delete('all'))
    ni1.add_command(label='Open', command=openfile)
    ni1.add_command(label='Save', command=savefile)
    ni1.add_separator()
    ni1.add_command(label='Exit', command=lambda: mspaintroot.destroy())
    menu.add_cascade(menu=ni1,label='File')
    ni2 = Menu(menu, tearoff=False)
    ni2.add_command(label='Erase', command=lambda: c.delete('all'))
    menu.add_cascade(menu=ni2, label='Edit')
    ni3 = Menu(menu, tearoff=False)
    ni3.add_command(label='Line widths', command=selectwidth)
    menu.add_cascade(menu=ni3, label='Palette')
    mspaintroot.config(menu=menu)
    imgpencil = PhotoImage(file='pencil.png')
    imgselectedpencil = PhotoImage(file="pencilselected.png")
    btnpencil = Button(mspaintroot,image=imgpencil,command=selectpencil)
    btnpencil.grid(row=0,column=0)
    imgbrush = PhotoImage(file='brush.gif.png')
    imgselectedbrush = PhotoImage(file='brushselected.png')
    btnbrush = Button(mspaintroot, image=imgbrush, command=selectbrush)
    btnbrush.grid(row=0, column=2)
    imgrubber = PhotoImage(file='rubber.png')
    imgselectedrubber = PhotoImage(file='rubberselected.png')
    btnrubber = Button(mspaintroot, image=imgrubber, command=selectrubber)
    btnrubber.grid(row=0, column=1)
    c = Canvas(mspaintroot,width=800,height=700,bg='white',cursor='pencil')
    c.grid(row=1,column=0,columnspan=6)
    mspaintroot.bind('<B1-Motion>',paint)
    mspaintroot.mainloop()

