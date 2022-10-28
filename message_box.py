from tkinter import Tk, Button, messagebox


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Messagebox in Tk')

        btn_info = Button(self, text='Info message', command=self.show_info)
        btn_info.pack()

        btn_error = Button(self, text='Error message', command=self.show_error)
        btn_error.pack()

        btn_warning = Button(self, text='Warning message', command=self.show_warning)
        btn_warning.pack()

        btn_question = Button(self, text='Question message', command=self.ask_question)
        btn_question.pack()

        btn_ok_cancel = Button(self, text='Ok Cancel message', command=self.ask_ok_cancel)
        btn_ok_cancel.pack()

        btn_yes_no = Button(self, text='Yes No message', command=self.ask_yes_no)
        btn_yes_no.pack()

        btn_ask_retry_cancel = Button(self, text='Ask Retry Cancel message', command=self.ask_retry_cancel)
        btn_ask_retry_cancel.pack()

    def show_info(self):
        messagebox.showinfo("Show info", "showing informations")

    def show_error(self):
        messagebox.showerror("Show error", "showing error")

    def show_warning(self):
        messagebox.showwarning("Show warn", "showing warning")

    def ask_question(self):
        messagebox.askquestion("ask question", "ask question")

    def ask_ok_cancel(self):
        messagebox.askokcancel("ask question", "ask ok cancel question")

    def ask_yes_no(self):
        messagebox.askyesno("ask question", "ask yes no question")

    def ask_retry_cancel(self):
        messagebox.askretrycancel("ask question", "ask retry cancel question")


if __name__ == '__main__':
    app = App()
    app.mainloop()
