import tkinter
from tkinter import N, S, E, W
from os import getcwd

from GUI.img_loader.loader import Loader
from PiCameraServer.main import ConnectionManager


class MainFrame(tkinter.Tk):

    def __init__(self, height: int = 450, width: int = 400) -> object:
        super().__init__()
        self. _display = self._Display(master=self, row=1, size=(400, 400))
        self._menu_bar(self)
        self._sub_buttons()
        self.geometry("%sx%s" % (width, height))
        #  Change location in loader to where the images are going to be saved
        self.pictures = Loader(getcwd())

        #  loads first image found
        self._display.change_picture(self.pictures)

        self.connection_manager = self.__load_server()

    def run(self):
        super().mainloop()

    def quit(self):
        super().quit()

    def _sub_buttons(self, start_column=0, start_row=0) -> object:
        def _next(master, move=0):
            master.pictures.change_index(move)
            master._display.change_picture(master.pictures)
        button_left = self._button(self, label="Prev", command=lambda: _next(self, -1))
        button_center = self._button(self, label="Quit", command=self.quit)
        button_right = self._button(self, label="Next", command=lambda: _next(self, 1))
        button_left.grid(row=5+start_row, column=0+start_column)
        button_center.grid(row=5+start_row, column=1+start_column)
        button_right.grid(row=5+start_row, column=2+start_column)

    def _set_canvas_image(self, image: object)->None:
        self.canvas_image = image

    def _menu_bar(self, master=None, *args, **kwargs)->object:
        menubar = tkinter.Menu(master=self)
        filemenu = tkinter.Menu(master=menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=master.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        tkinter.Tk.config(master, menu=menubar)

    @staticmethod
    def __load_server()->object:
        manager = ConnectionManager()
        return manager

    @staticmethod
    def _button(master=None, label=None, command=None, anchor=None,
                bg=None, **kwargs)->object:

        def __default_callback()->object:
            return None

        button = tkinter.Button(
            master=master,
            text=label if label is not None else "test",
            command=command if command is not None else __default_callback,
            anchor=anchor if anchor is not None else "w",
            bg=bg if bg is not None else "grey",
            **kwargs
        )
        return button

    class _Display:
        def __init__(self, master: object=None, row: int = 0, column: int = 0, sticky: object = (N + W),
                     size: tuple = (400, 450), bg="grey")->None:
            self.size = size
            self.window = tkinter.Frame(master, height=size[0], width=size[1])
            self.picture = tkinter.Canvas(self.window, height=size[0] - 5, width=size[1] - 5)
            self.picture.pack()
            self.picture.image = None
            self.picture.create_image(0, 0, image=self.picture.image, anchor="nw")
            self.window.grid(row=row, column=column, sticky=sticky, columnspan=4, rowspan=4)
            self.picture.configure(bg=bg)

        def change_picture(self, image)->None:
            self.picture.image = image(self.size)
            self.picture.create_image(0, 0, image=self.picture.image, anchor="nw")


if __name__ == "__main__":
    main = MainFrame()
    main.run()
