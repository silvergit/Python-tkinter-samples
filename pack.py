from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Pack in Tk')
        self.minsize(400, 300)

        y_frame = Frame(self, bg='yellow')
        y_frame.pack(expand=True, fill='both', side=TOP)
        Label(y_frame, text='Hello').pack(anchor='w')

        bottom_frame = Frame(self)
        bottom_frame.pack(expand=True, fill='both')

        Frame(bottom_frame, bg='blue').pack(expand=True, fill='both', side=LEFT)

        Frame(bottom_frame, bg='red').pack(expand=True, fill='both', side=LEFT)

        g_frame = Frame(bottom_frame, bg='green')
        g_frame.pack(expand=True, fill='both', side=LEFT)
        Label(g_frame, text='Word').pack(anchor='e')


if __name__ == "__main__":
    app = App()
    app.mainloop()
