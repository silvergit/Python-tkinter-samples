from tkinter import Tk, Label, Entry, Button


class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Entry in Tk')

        Label(self, text='First Name').pack()
        self.entry_fn = Entry(self)
        self.entry_fn.pack()
        Label(self, text='Last Name').pack()
        self.entry_ln = Entry(self)
        self.entry_ln.pack()
        Button(self, text='Sign in', command=self.on_btn_clicked).pack()
        self.lbl_result = Label(self)
        self.lbl_result.pack()

    def on_btn_clicked(self):
        first_name = self.entry_fn.get()
        last_name = self.entry_ln.get()
        self.lbl_result.configure(text='welcome mr/ms {} {}'.format(first_name, last_name))


if __name__ == '__main__':
    app = App()
    app.mainloop()
