from tkinter import Tk, IntVar, Radiobutton, W, StringVar


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Radio Button in Tk')

        MODES = [('ali', 'name'), ('pazhouhesh', 'family'), ('lidora.com', 'site')]


        # v1 = IntVar()
        # v2 = IntVar()
        #
        # Radiobutton(self, text='One', variable=v1, value=1).pack(anchor=W)
        # Radiobutton(self, text='Two', variable=v2, value=2).pack(anchor=W)

        v = StringVar()
        v.set('name')

        for text, mode in MODES:
            b = Radiobutton(self, text=text, variable=v, value=mode)
            b.pack(anchor=W)


if __name__ == '__main__':
    app = App()
    app.mainloop()
