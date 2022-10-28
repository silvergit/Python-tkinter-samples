from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Combobox in tkinter')

        list = ['Item1', 'Item2', 'Item3', 'Item4', 'Item5']

        self.combo = ttk.Combobox(self, values=list)
        self.combo.set('Pick as option')
        self.combo.pack(padx=5, pady=5)

        Button(self, text='Submit', command=self.submit).pack()

        self.geometry('300x300')


    def submit(self):
        print(self.combo.get())


if __name__ == '__main__':
    app = App()
    app.mainloop()
