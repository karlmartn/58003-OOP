from tkinter import *

class MyWindow:
    def __init__(self, win):
        # widgets start from here
        self.lbl1 = Label(win, text="Metric Units of Length")
        self.lbl1.place(x=250, y=20)
        self.lbl2 = Label(win, text="Enter the distance in Centimeter(cm): ")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="Conversion into Meter(m):")
        self.lbl3.place(x=100, y=150)
        self.lbl4 = Label(win, text="Conversion into Kilometer(km):")
        self.lbl4.place(x=100, y=200)

        self.txt1 = Entry(win, bd=1)
        self.txt1.place(x=350, y=100)
        self.txt2 = Entry(win, bd=1)
        self.txt2.place(x=350, y=150)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=350, y=200)

        self.btn1 = Button(win, text='Convert', command=self.convert)
        self.btn1.place(x=250, y=250)

    def convert(self):
            cm = float(self.txt1.get())
            m = cm / 100
            km = cm / 100000
            self.txt2.delete(0, END)
            self.txt2.insert(END, str(m))
            self.txt3.delete(0, END)
            self.txt3.insert(END, str(km))



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.mainloop()