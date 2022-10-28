from tkinter import Tk, Checkbutton, Button, Label, IntVar


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.male = IntVar()
        self.female = IntVar()

        self.title('Checkbutton in Tk')
        self.chk_male = Checkbutton(self, text='Male', variable=self.male)
        self.chk_male.pack()
        self.chk_female = Checkbutton(self, text='Female', variable=self.female)
        self.chk_female.pack()
        Button(self, text='Check', command=self.onBtnClicked).pack()
        self.lbl = Label(self)
        self.lbl.pack()

    def onBtnClicked(self):
        gender = 'unknown'
        if self.male.get() == 1 and self.female.get() == 0:
            gender = 'male'
        elif self.male.get() == 0 and self.female.get() == 1:
            gender = 'female'
        else:
            gender = 'unknown'

        self.lbl.configure(text=gender)


if __name__ == '__main__':
    app = App()
    app.mainloop()
