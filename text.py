from tkinter import Tk, Text, INSERT, END, Button


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Text in Tk')

        self.text = Text(self)
        self.text.insert(INSERT, "Hello....")
        self.text.pack()

        Button(self, text='Save', command=self.onSaveBtnClicked).pack()
        Button(self, text='Load', command=self.onLoadBtnClicked).pack()

    def onSaveBtnClicked(self):
        # print(self.text.get(1.0, END))
        with open('text_output.txt', 'w') as f:
            f.write(self.text.get(1.0, END))

    def onLoadBtnClicked(self):
        with open('text_output.txt', 'r') as f:
            data = f.read()
            self.text.insert(INSERT, data)


if __name__ == '__main__':
    app = App()
    app.mainloop()
