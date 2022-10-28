from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Event & Bind in Tk')

        btn = Button(self, text='Click')
        btn.pack()

        btn.bind('<Button-1>', self.hello)
        btn.bind('<Double-1>', self.quit)

        text = 'This is a sample text, Move mouse on this text'
        msg = Message(self, text=text)
        msg.config(bg='lightgreen', font=('times', 24, 'italic'))
        msg.bind('<Motion>', self.motion)
        msg.pack()

        self.geometry("300x300")

    def hello(self, event):
        print("Single click, Button 1")

    def quit(self, event):
        print("Double Click, so let's stop")
        self.quit()

    def motion(self, event):
        print("Mouse position: (%s %s)" % (event.x, event.y))
        return


if __name__ == '__main__':
    app = App()
    app.mainloop()
