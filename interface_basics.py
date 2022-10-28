from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('First TK app with python')
        self.minsize(400, 300)
        self.maxsize(640, 450)
        # self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    app.mainloop()
