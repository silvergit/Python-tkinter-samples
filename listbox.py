from tkinter import Tk, Listbox, Entry, Button, END


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('ListBox in Tk')

        self.entry = Entry(self)
        self.entry.pack()

        self.btnAdd = Button(self, text='Add to list', command=self.insertToList)
        self.btnAdd.pack()
        self.btnDell = Button(self, text='Clear list', command=self.clearList)
        self.btnDell.pack()

        self.listbox = Listbox(self)
        self.listbox.pack()

        self.listbox.insert(1, 'Python')
        self.listbox.insert(2, 'C++')
        self.listbox.insert(3, 'Java')

    def insertToList(self):
        if self.entry.get() != '':
            self.listbox.insert(END, self.entry.get())

    def clearList(self):
        self.listbox.delete(0, END)


if __name__ == '__main__':
    app = App()
    app.mainloop()
