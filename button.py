from tkinter import Pack,Button,Tk

class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Button in tkinter')

        Button(self, text='Click me', command=self.onButtonClick).pack()

    def onButtonClick(self):
        print('Button clicked')

if __name__ == '__main__':
    app = App()
    app.mainloop()