from tkinter import Tk, Scale, W, HORIZONTAL, Label, Button


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Scale in Tk')

        self.lbl = Label(self, text='0')
        self.lbl.pack()

        self.scale = Scale(self, from_=20, to=80)
        self.scale.pack(anchor=W)

        Scale(self, from_=0, to=10, orient=HORIZONTAL, resolution=0.1).pack(anchor=W)
        Button(self, text='Get Data', command=self.onBtnClicked).pack()

    def onBtnClicked(self):
        self.lbl.configure(text=self.scale.get())


if __name__ == '__main__':
    app = App()
    app.mainloop()
