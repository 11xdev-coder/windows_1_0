from tkinter import filedialog
from tkinter import messagebox


def start_load():
    f = filedialog.askopenfilename(filetypes=(('Text files','*.txt'),('Calendar files','*.cal'),('Card files','*.crd'),('Paint files','*.msp'),('Terminal files','*.trm')))

    messagebox.showwarning('Unkown format','File %s has got unkown format' % (str(f)))