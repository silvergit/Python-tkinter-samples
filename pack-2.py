from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Pack in Tk')

        bottom_frame = Frame(self)
        bottom_frame.pack(side=BOTTOM)

        middle_frame = Frame(self)
        middle_frame.pack(side=TOP)

        Label(middle_frame, text='Enter anything').pack(side=TOP, padx=5, pady=10)

        name_entry = Entry(middle_frame)
        name_entry.pack(side=LEFT)

        btn_send = Button(middle_frame, text='Send')
        btn_send.pack(side=LEFT)

        listbox = Listbox(bottom_frame)
        listbox.pack(expand=True)

        btn_clear = Button(bottom_frame, text='Clear List')
        btn_clear.pack(expand=True)



if __name__ == "__main__":
    app = App()
    app.mainloop()
