from PIL import Image, ImageTk
import os

class Sprite:
    def __init__(self, filepaths: [str] = None, costume_number: int = 0):
        if filepaths is None:
            filepaths = [os.path.dirname(os.path.realpath(__file__)) + "\\resources\\3Dow.png"]

        self.width = 1.0
        self.height = 1.0

        self.filepaths = filepaths
        self.costumes = []
        for filepath in filepaths:
            self.costumes.append(
                Image.open(filepath)
            )
        self.costume_number = costume_number

    def image(self) -> ImageTk.PhotoImage:
        image = self.costumes[self.costume_number % len(self.costumes)]
        image = image.resize(size=(int(self.width * image.size[0]),
                                   int(self.height * image.size[1]),))
        return ImageTk.PhotoImage(image)
