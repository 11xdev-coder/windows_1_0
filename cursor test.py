import tkinter as tk
from tkinter import Tk
def one():
    root = tk.Tk()
    text = tk.Text(root, blockcursor=True)
    text.insert('insert', 'cursor appearance test')
    text.pack()
    text.focus_set()
    root.mainloop()

def two():

    root = Tk()
    root.config(cursor='watch red')  # красный watch-курсор
    tk.Button(root, text="Button", cursor="heart").pack()
    tk.Button(root, text="Button2", cursor="arrow").pack()
    tk.Button(root, text="Button3", cursor="circle").pack()
    tk.Button(root, text="Button4", cursor="clock").pack()
    tk.Button(root, text="Button5", cursor="cross").pack()
    tk.Button(root, text="Button6", cursor="dotbox").pack()
    tk.Button(root, text="Button7", cursor="exchange").pack()
    tk.Button(root, text="Button62", cursor="fleur").pack()
    tk.Button(root, text="Button63", cursor="man").pack()
    tk.Button(root, text="Button64", cursor="mouse").pack()
    tk.Button(root, text="Button65", cursor="pirate").pack()
    tk.Button(root, text="Button66", cursor="plus").pack()
    tk.Button(root, text="Button672", cursor="shuttle").pack()
    tk.Button(root, text="Button673", cursor="sizing").pack()
    tk.Button(root, text="Button674", cursor="spider").pack()
    tk.Button(root, text="Button675", cursor="spraycan").pack()
    tk.Button(root, text="Button676", cursor="star").pack()
    tk.Button(root, text="Button677", cursor="target").pack()
    tk.Button(root, text="Button6762", cursor="tcross").pack()
    tk.Button(root, text="Button6772", cursor="trek").pack()
    root.mainloop()

two()