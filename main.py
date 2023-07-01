import tkinter
from tkinter import Tk, Button, Entry, messagebox
import tkinter.font as font


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.font_configure = font.Font(family="Consolas", size=20, weight="bold")

        self.title("Calculadora")
        self.geometry("218x287")
        self.resizable(0,0)

        self.entries()
        self.buttons()

    def entries(self):
        self.screen = Entry(self, width=14, font=self.font_configure, justify="right")
        self.screen.pack()
        self.screen.place(x=0, y=0, height=40)

    def buttons(self):
        self.seven = Button(self, text="7", width=6, height=3, command=lambda: self.event("7"))
        self.seven.pack()
        self.seven.place(x=0, y=50)

        self.eight = Button(self, text="8", width=6, height=3, command=lambda: self.event("8"))
        self.eight.pack()
        self.eight.place(x=55, y=50)

        self.nine = Button(self, text="9", width=6, height=3, command=lambda: self.event("9"))
        self.nine.pack()
        self.nine.place(x=110, y=50)

        self.division = Button(self, text="÷", width=6, height=3, command=lambda: self.event("/"))
        self.division.pack()
        self.division.place(x=165, y=50)

        self.four = Button(self, text="4", width=6, height=3, command=lambda: self.event("4"))
        self.four.pack()
        self.four.place(x=0, y=110)

        self.five = Button(self, text="5", width=6, height=3, command=lambda: self.event("5"))
        self.five.pack()
        self.five.place(x=55, y=110)

        self.six = Button(self, text="6", width=6, height=3, command=lambda: self.event("6"))
        self.six.pack()
        self.six.place(x=110, y=110)

        self.multiplication = Button(self, text="x", width=6, height=3, command=lambda: self.event("*"))
        self.multiplication.pack()
        self.multiplication.place(x=165, y=110)

        self.one = Button(self, text="1", width=6, height=3, command=lambda: self.event("1"))
        self.one.pack()
        self.one.place(x=0, y=170)

        self.two = Button(self, text="2", width=6, height=3, command=lambda: self.event("2"))
        self.two.pack()
        self.two.place(x=55, y=170)

        self.three = Button(self, text="3", width=6, height=3, command=lambda: self.event("3"))
        self.three.pack()
        self.three.place(x=110, y=170)

        self.division = Button(self, text="-", width=6, height=3, command=lambda: self.event("-"))
        self.division.pack()
        self.division.place(x=165, y=170)

        self.cero = Button(self, text="0", width=6, height=3, command=lambda: self.event("0"))
        self.cero.pack()
        self.cero.place(x=0, y=230)

        self.point = Button(self, text=".", width=6, height=3, command=lambda: self.event("."))
        self.point.pack()
        self.point.place(x=55, y=230)

        self.equals = Button(self, text="=", width=6, height=3, command=lambda: self.evaluate())
        self.equals.pack()
        self.equals.place(x=110, y=230)

        self.plus = Button(self, text="+", width=6, height=3, command=lambda: self.event("+"))
        self.plus.pack()
        self.plus.place(x=165, y=230)

    def event(self, number):
        self.screen.insert(tkinter.END, number)

    def evaluate(self):
        try:
            aux = self.screen.get()
            self.screen.delete(0, tkinter.END)
            self.screen.insert(tkinter.END, str(eval(aux)))
        except:
            return messagebox.showerror("Error", "Error en operación")

#https://icon-icons.com/es/download/72046/ICO/256/


window = Window()
window.mainloop()
