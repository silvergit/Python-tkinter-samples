from tkinter import *
from tkinter import filedialog

class App(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Button in tkinter')

        Button(self, text='Open file', command=self.onOFClicked).pack()
        Button(self, text='Open files', command=self.onOFSClicked).pack()
        Button(self, text='Save file', command=self.onSFClicked).pack()
        Button(self, text='Open directory', command=self.onODClicked).pack()



    def onOFClicked(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        print(path)

    def onOFSClicked(self):
        path = filedialog.askopenfiles(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        print(path)

    def onSFClicked(self):
        path = filedialog.asksaveasfile(initialdir="/", title="Select file", filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        print(path)

    def onODClicked(self):?!?jedi=0, ?!?            (*_***options*_*) ?!?jedi?!?
        path = filedialog.askdirectory(initialdir="/", title="Select file")
        print(path)



if __name__ == '__main__':
    app = App()
    app.mainloop()
