from tkinter import Tk, Menu

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Menu in tkinter')
        
        menubar = Menu(self)
        menubar.add_command(label='Hello', command=self.hello)
        menubar.add_command(label='Quit', command=quit)

        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label='Open', command=self.open)
        file_menu.add_command(label='Save', command=self.save)
        menubar.add_cascade(label='File', menu=file_menu)

        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cut")
        editmenu.add_command(label="Copy")
        editmenu.add_command(label="Paste")
        menubar.add_cascade(label="Edit", menu=editmenu)

        self.config(menu=menubar)

    def hello(self):
        print('Hello')

    def open(self):
        print('Open')

    def save(self):
        print('Save')


if __name__ == '__main__':
    app = App()
    app.mainloop()