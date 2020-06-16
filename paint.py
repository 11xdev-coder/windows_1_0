from tkinter import *

brush_size = 3
color = 'black'

root = Tk()
root.title('Paint на Python')
btnred = Button(root,text='Красный',command=lambda: change_color('red'))
btnb = Button(root,text='Синий',command=lambda: change_color('blue'))
btnbl = Button(root,text='Черный',command=lambda: change_color('black'))
btnp = Button(root,text='Розовый',command=lambda: change_color('pink'))
btnc = Button(root,text='Голубой',command=lambda: change_color('cyan'))
btnpr = Button(root,text='Фиолетовый',command=lambda: change_color('purple'))
btng = Button(root,text='Зеленый',command=lambda: change_color('green'))
btnwhite = Button(root,text='Ластик',command=lambda: change_color('white'))
btn1 = Button(root,text='1',command=lambda: change_bs(1))
btn5 = Button(root,text='5',command=lambda: change_bs(5))
btn10 = Button(root,text='10',command=lambda: change_bs(10))
btn15 = Button(root,text='15',command=lambda: change_bs(15))
btn20 = Button(root,text='20',command=lambda: change_bs(20))
btn40 = Button(root,text='40',command=lambda: change_bs(40))
btn60 = Button(root,text='60',command=lambda: change_bs(60))
btn120 = Button(root,text='120',command=lambda: change_bs(120))
btn240 = Button(root,text='240',command=lambda: change_bs(240))
def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    canvas.create_oval(x1,y1,x2,y2,fill=color,outline=color)

def change_bs(new_brush_size):
    global brush_size
    brush_size = new_brush_size

def change_color(new_color):
    global color
    color = new_color

canvas = Canvas(root,width=1000,height=800,bg='white')
btndelete = Button(root,text='Удалить все',command=lambda: canvas.delete('all'))
canvas.grid(row=2,column=0,columnspan=9,padx=5,pady=5,sticky=E+W+S+N)
btnred.grid(row=0,column=0)
btnwhite.grid(row=0,column=1)
btnb.grid(row=0,column=2)
btnbl.grid(row=0,column=3)
btnp.grid(row=0,column=4)
btnpr.grid(row=0,column=5)
btnc.grid(row=0,column=6)
btng.grid(row=0,column=7)
btn1.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn10.grid(row=1,column=2)
btn15.grid(row=1,column=3)
btn20.grid(row=1,column=4)
btn40.grid(row=1,column=5)
btn60.grid(row=1,column=6)
btn120.grid(row=1,column=7)
btn240.grid(row=1,column=8)
btndelete.grid(row=0,column=8)
canvas.bind('<B1-Motion>',paint)
root.mainloop()