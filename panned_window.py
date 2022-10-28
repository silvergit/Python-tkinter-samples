from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('PanedWindow in Tk')

        main_pw = PanedWindow(self)
        side_pw = PanedWindow(self, orient=VERTICAL)
        main_pw.pack(fill='both', expand=1)

        left_label = Label(main_pw, text='Left Panel')
        top_label = Label(side_pw, text='Top Panel')
        bottom_label = Label(side_pw, text='Bottom Panel')

        main_pw.add(left_label)
        main_pw.add(side_pw)
        side_pw.add(top_label)
        side_pw.add(bottom_label)

        self.geometry('300x300')


if __name__ == "__main__":
    app = App()
    app.mainloop()
