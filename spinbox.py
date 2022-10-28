from tkinter import Tk, Spinbox, Button


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Spinbox in Tk')

        self.spinbox = Spinbox(self, from_=10, to=50)
        self.spinbox.pack()

        btnGet = Button(self, text='Get data', command=self.onBtnGetClicked)
        btnGet.pack()

    def onBtnGetClicked(self):
        value = self.spinbox.get()
        print(value)


if __name__ == "__main__":
    app = App()
    app.mainloop()
