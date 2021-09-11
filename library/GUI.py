import tkinter as tk
from PIL import Image, ImageTk


class MainGui(tk.Tk):
    """This class will contain the main GUI for the """

    def __init__(self):
        super().__init__()
        self.width, self.height = 750, 600
        self.geometry(f"{self.width}x{self.height}")
        self.title("Library of Error and Terror")
        self.minsize(self.width, self.height)
        self.maxsize(self.width, self.height)

        F = StartingFrame(self).place(x=0, y=0)
        F2 = StartWidgetsFrame(self, height=400, width=400).place(x=0, y=300)


class StartingFrame(tk.Frame):
    """This class is for the image in the background"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image1 = Image.open('images/lib.png')
        new_image = image1.resize((750, 600), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(new_image)
        # photo_label = tk.Label(self, image=new_image)
        # photo_label.img = new_image
        # photo_label.pack()
        pic_canva = tk.Canvas(width=750, height=600)
        pic_canva.place(x=0, y=0)
        pic_canva.img = new_image  # this is important in order to avoid garbage collection

        pic_canva.create_image(0, 0, image=new_image, anchor='nw')
        pic_canva.create_text(350, 70, text="WELCOME TO THE LIBRARY", fill='white',
                              font='Times 30 bold')
        pic_canva.create_text(250, 200, text="Login as", fill='white',
                              font='Times 20 bold')


class StartWidgetsFrame(tk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        radiobutton1 = tk.Radiobutton(self, text="Librarian").place(x=100, y=100)
        radiobutton2 = tk.Radiobutton(self, text="Member").place(x=100, y=200)


if __name__ == '__main__':
    gui = MainGui()
    gui.mainloop()
