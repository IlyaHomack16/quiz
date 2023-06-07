import tkinter

windows = tkinter.Tk()
windows.title("Samsung Galaxy S23 Ultra")
windows.geometry("310x490")
windows.resizable(False, False)


def press_command():
    button.destroy()
    lbl1.destroy()
    lbl2 = tkinter.Label(windows, text="1 вопрос", height=1, width=11, background="#70ff57", foreground="#5e8fff",
                         font=("", 20))
    lbl2.place(x=65, y=140)
    lbl3 = tkinter.Label(windows, text="", height=1, width=11, background="#70ff57", foreground="#5e8fff",
                         font=("", 20))
    lbl3.place(x=60, y=50)


c = tkinter.Canvas(windows, width=310, height=490, bg="black")
c.place(x=0, y=0)
c1 = tkinter.Canvas(windows, width=288, height=468, bg="#70ff57")
c1.place(x=10, y=10)
lbl1 = tkinter.Label(windows, text="Чат викторина", height=1, width=11, background="#70ff57", foreground="#5e8fff", font=("", 20))
lbl1.place(x=60, y=50)
button = tkinter.Button(windows, text="Начать", height=1, width=10, background="#a1a1a1", activebackground="#70ff57", font=("", 10), command=press_command) # height - высота в таблицах width - ширина в таблицах, foreground - цвет текста, background - заливка
button.place(x=110, y=100)

windows.mainloop()