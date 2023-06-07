import tkinter

windows = tkinter.Tk()
windows.title("Samsung Galaxy S23 Ultra")
windows.geometry("310x490")
windows.resizable(False, False)

c = tkinter.Canvas(windows, width=310, height=490, bg="black")
c.place(x=0, y=0)
c1 = tkinter.Canvas(windows, width=288, height=468, bg="#70ff57")
c1.place(x=10, y=10)

windows.mainloop()