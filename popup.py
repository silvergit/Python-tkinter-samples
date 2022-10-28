from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Popup in tkinter')

        self.menu = Menu(self, tearoff=0)
        self.menu.add_command(label='Undo', command=self.hello)
        self.menu.add_command(label='Redo', command=self.hello)

        frame = Frame(self, width=300, height=300)
        frame.pack()

        frame.bind('<Button-3>', self.popup)

        self.config(menu=self.menu)


    def popup(self, event):
        self.menu.post(event.x_root, event.y_root)


    def hello(self):
        print('hello')


if __name__ == '__main__':
    app = App()
    app.mainloop()
