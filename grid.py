from tkinter import Tk, Label, Entry

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Label in tkinter')

        labels = ['Name', 'Family', 'Site', 'Social Media']

        for item in labels:
            Label(self, text=item).grid(row=int(labels.index(item)), column=0)
            Entry(self).grid(row=int(labels.index(item)), column=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()