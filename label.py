from tkinter import Tk, Label, Pack

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Label in tkinter')
        
        Label(self,text="This is a sample text",font="Tahoma").pack()
        Label(self,text="This is a sample text",font=("Tahoma",18)).pack()
        Label(self,text="This is a sample text",foreground="red").pack()
        Label(self,text="This is a sample text",background="blue",fg="white").pack()


if __name__ == '__main__':
    app = App()
    app.mainloop()