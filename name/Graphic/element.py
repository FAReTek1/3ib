import abc
import os
import tkinter

from PIL import ImageTk

if __name__ == '__main__':
    import draw_object
    from image import Sprite
else:
    from . import draw_object
    from .image import Sprite


class Element(abc.ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.resize(width, height)

    @abc.abstractmethod
    def resize(self, width: int, height: int):
        pass

    @abc.abstractmethod
    def real(self):
        pass


class Window(Element):
    def __init__(self, width: int = 480, height: int = 360,
                 title: str = "Window", icon: str = None):
        if icon is None:
            icon = os.path.dirname(os.path.realpath(__file__)) + "\\resources\\3Dow.png"
        self.__window = tkinter.Tk()
        self.__window.title(title)

        self.title = title
        self.icon = Sprite([icon])
        self.__window.wm_iconphoto(False, self.icon.image())  # type: ignore

        super().__init__(width, height)

    def real(self):
        return self.__window

    def resize(self, width: int, height: int):
        self.__window.geometry(f"{width}x{height}")

    def start(self):
        self.__window.mainloop()


class Canvas(Element):
    def __init__(self, parent, width: int = 480, height: int = 360, bg_col: str = "white"):
        self.__canvas = tkinter.Canvas(parent.real(), bg=bg_col)
        self._image_scope = []

        super().__init__(width, height)

    def clear(self):
        self._image_scope.clear()
        self.__canvas.delete("all")

    def real(self):
        return self.__canvas

    def resize(self, width: int, height: int):
        self.__canvas.config(width=width, height=height)

    def pack(self):
        self.real().pack()

    def create(self, draw_obj: draw_object.DrawObject):
        draw_id = draw_obj.draw(self.__canvas, self)
        if isinstance(draw_id, tuple):
            if len(draw_id) == 2:
                if isinstance(draw_id[1], ImageTk.PhotoImage):
                    self._image_scope.append(draw_id[1])
                    return draw_id[0]
        return draw_id


if __name__ == '__main__':
    program = Window()

    canvas = Canvas(program)
    canvas.pack()

    sprite = Sprite()

    image = draw_object.Image(0, 0, sprite, style=draw_object.Style(anchor="center", height=1, width=2))
    image2 = draw_object.Image(240, 90, sprite, style=draw_object.Style(anchor="center", height=0.5, width=4))

    canvas.create(image)
    canvas.create(image2)

    program.start()
