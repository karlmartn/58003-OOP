from tkinter import*

win = Tk()
win.geometry("400x300+10+10")
win.title("Grid Manager")


txt1 = Entry(bd=2)
txt1.grid()
txt1.grid(row=0,column=0)
txt1.insert(0,"row 0 column 0" )

txt2 = Entry(bd=2)
txt2.grid()
txt2.grid(row=0,column=1)
txt2.insert(0,"row 0 column 1" )

txt3 = Entry(bd=2)
txt3.grid()
txt3.grid(row_=0,column=2)
txt3.insert(0,"row 0 column 2" )

txt4 = Entry(bd=2)
txt4.grid()
txt4.grid(row=1,column=0)
txt4.insert(0,"row 1 column 0" )

txt5 = Entry(bd=2)
txt5.grid()
txt5.grid(row=1,column=1)
txt5.insert(0,"row 1 column 1" )

txt6 = Entry(bd=2)
txt6.grid()
txt6.grid(row=1,column=2)
txt6.insert(0,"row 1 column 2" )

txt7 = Entry(bd=2)
txt7.grid()
txt7.grid(row=2,column=0)
txt7.insert(0,"row 2 column 0" )

txt8 = Entry(bd=2)
txt8.grid()
txt8.grid(row=2,column=1)
txt8.insert(0,"row 2 column 1" )

txt9 = Entry(bd=2)
txt9.grid()
txt9.grid(row=2,column=2)
txt9.insert(0,"row 2 column 2" )

win.mainloop()

