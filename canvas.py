from tkinter import *


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Canvas in Tk')
        self.minsize(500, 320)

        canvas_window = Canvas(self, width=500, height=320)

        # drawing a simple line
        canvas_window.create_line(10, 20, 10, 100)

        # drawing a line with design
        canvas_window.create_line(50, 20, 50, 100, fill="red", dash=(4, 4))

        # creating rectangle
        canvas_window.create_rectangle(100, 20, 200, 100, fill="blue")

        # creating eclipse with oval
        canvas_window.create_oval(220, 20, 340, 100, fill="red")

        # creating circle with oval
        canvas_window.create_oval(350, 20, 430, 100, fill="yellow")

        # adding polygon and multiple lines to create other shapes
        canvas_window.create_polygon([10, 120, 10, 180, 80, 180], outline='gray', fill='gray', width=2)

        # adding image to the window with canvas
        # image_file = PhotoImage(file='image.png')
        # canvas_window.create_image(200, 160, image=image_file)

        # adding text inside canvas area
        canvas_window.create_text(370, 160, fill="darkblue", font="Times 20 italic bold", text="Sample text")

        # making arc in window
        canvas_window.create_arc(0, 200, 90, 300)

        canvas_window.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
