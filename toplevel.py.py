from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Main Window')

        toplevel = Toplevel(self)
        toplevel.title("Toplevel Window")

        
if __name__ == "__main__":
    app = App()
    app.mainloop()
