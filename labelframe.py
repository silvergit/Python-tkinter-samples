from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Labelframe in Tk')

        labelframe = LabelFrame(self, text='This is a labelframe')
        labelframe.pack(fill='both', expand='yes')

        label = Label(labelframe, text='Label inside Frame')
        label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
