from tkinter import Tk, Listbox, END, Scrollbar, RIGHT, BOTH, LEFT


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Scrollbar in Tk')

        # making scroller on the right side of window
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)

        self.listbox = Listbox(self, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH)

        for i in range(1, 100):
            self.listbox.insert(END, 'item {}'.format(i))

        # making the scroll by the contents in list
        self.scrollbar.configure(command=self.listbox.yview)

        self.geometry("300x300")


if __name__ == '__main__':
    app = App()
    app.mainloop()
