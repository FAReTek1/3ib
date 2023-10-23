import abc
import tkinter

if __name__ == '__main__':
    from adjust import transpose_to_top_left_origin as transpose
    from image import Sprite
    from style import Style, PointStyle
else:
    from .adjust import transpose_to_top_left_origin as transpose
    from .image import Sprite
    from .style import Style, PointStyle


class DrawObject(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __iter__(self):
        pass

    @abc.abstractmethod
    def draw(self, canvas: tkinter.Canvas, real):
        pass


class Point(DrawObject):
    def __init__(self, x: float, y: float, style: Style = PointStyle):
        self.x = x
        self.y = y

        self.style = style

    def __iter__(self):
        yield self.x
        yield self.y

    def draw(self, canvas: tkinter.Canvas, real):
        canvas.create_oval(transpose((self.x - self.style.size, self.y - self.style.size), real),
                           transpose((self.x + self.style.size, self.y + self.style.size), real),
                           fill=self.style.fill, width=self.style.thickness, outline=self.style.outline)


class Line(DrawObject):
    def __init__(self, P1, P2, style: Style = PointStyle):
        self.x1 = P1[0]
        self.y1 = P1[1]

        self.x2 = P2[0]
        self.y2 = P2[1]

        self.style = style

    def __iter__(self):
        yield self.x1
        yield self.y1

        yield self.x2
        yield self.y2

    def draw(self, canvas: tkinter.Canvas, real):
        if self.style.arrow == "Last":
            arrow = tkinter.LAST
        elif self.style.arrow == "First":
            arrow = tkinter.FIRST
        elif self.style.arrow == "Both":
            arrow = tkinter.BOTH
        else:
            arrow = None
        canvas.create_line(
            transpose((self.x1, self.y1), real),
            transpose((self.x2, self.y2), real),
            width=self.style.thickness, capstyle=self.style.cap, fill=self.style.fill,
            arrow=arrow, arrowshape=self.style.arrowshape, dash=self.style.dash)


class Lines(DrawObject):
    def __init__(self, pts: [], style: Style = PointStyle):
        self.pts = pts

        self.style = style

    def __iter__(self):
        return (point for point in self.pts)

    def draw(self, canvas: tkinter.Canvas, real):
        pts = []

        for point in self.pts:
            pts.append(tuple(transpose(point, real)))
        pts = tuple(pts)
        canvas.create_line(pts,  # type: ignore
                           width=self.style.thickness, capstyle=self.style.cap,
                           joinstyle=self.style.join, fill=self.style.fill)


class Triangle(DrawObject):
    def __init__(self, P1, P2, P3, style: Style = PointStyle):
        self.pts = (P1, P2, P3)

        self.style = style

    def __iter__(self):
        return (point for point in self.pts)

    def draw(self, canvas: tkinter.Canvas, real):
        canvas.create_polygon(
            (transpose(self.pts[0], real), transpose(self.pts[1], real), transpose(self.pts[2], real)),  # type: ignore
            width=self.style.thickness, joinstyle=self.style.join, fill=self.style.fill, outline=self.style.outline)


class Rectangle(DrawObject):
    def __init__(self, P1, P2, style: Style = PointStyle):
        self.pts = (P1, P2)

        self.style = style

    def __iter__(self):
        return (point for point in self.pts)

    def draw(self, canvas: tkinter.Canvas, real):
        canvas.create_rectangle(
            (transpose(self.pts[0], real), transpose(self.pts[1], real)),  # type: ignore
            width=self.style.thickness, fill=self.style.fill, outline=self.style.outline)


class Poly(DrawObject):
    def __init__(self, pts: [], style: Style = PointStyle):
        self.pts = pts

        self.style = style

    def __iter__(self):
        return (point for point in self.pts)

    def draw(self, canvas: tkinter.Canvas, real):
        pts = []

        for point in self.pts:
            pts.append(tuple(transpose(point, real)))
        pts = tuple(pts)
        canvas.create_polygon(pts,  # type: ignore
                              width=self.style.thickness, outline=self.style.outline,
                              joinstyle=self.style.join, fill=self.style.fill)


class Arc(DrawObject):
    def __init__(self, x, y, start: float, extent: float, inner: float, outer: float, style: Style = PointStyle):
        self.x = x
        self.y = y

        self.start = start
        self.extent = extent

        self.inner = inner
        self.outer = outer

        self.style = style

    def __iter__(self):
        yield self.x, self.y
        yield self.start
        yield self.extent
        yield self.inner
        yield self.outer

    def draw(self, canvas: tkinter.Canvas, real):
        middle_radius = (self.inner + self.outer) / 2
        P1 = transpose((self.x - middle_radius, self.y - middle_radius), real)
        P2 = transpose((self.x + middle_radius, self.y + middle_radius), real)
        # Note that because of the bad rendering engine of tkinter, arcs with angles of 0, 90, 180 etc. will have round caps at parts. Sorry
        if self.style.thickness > 0:
            canvas.create_arc(P1, P2,
                              width=abs(self.outer - self.inner) + self.style.thickness, outline=self.style.outline,
                              start=self.start + 90, extent=0 - self.extent,
                              style=tkinter.ARC, )
        canvas.create_arc(P1, P2,
                          width=abs(self.outer - self.inner), outline=self.style.fill,
                          start=self.start + 90, extent=0 - self.extent,
                          style=tkinter.ARC, )


class Segment(DrawObject):
    def __init__(self, x, y, start: float, extent: float, radius: float, style: Style = PointStyle):
        self.x = x
        self.y = y

        self.start = start
        self.extent = extent

        self.radius = radius

        self.style = style

    def __iter__(self):
        yield self.x, self.y
        yield self.start
        yield self.extent
        yield self.radius

    def draw(self, canvas: tkinter.Canvas, real):
        P1 = transpose((self.x - self.radius, self.y - self.radius), real)
        P2 = transpose((self.x + self.radius, self.y + self.radius), real)
        canvas.create_arc(P1, P2,
                          fill=self.style.fill,
                          outline=self.style.outline, width=self.style.thickness,
                          start=self.start + 90, extent=0 - self.extent,
                          style=tkinter.CHORD, )


class Sector(DrawObject):
    def __init__(self, x, y, start: float, extent: float, radius: float, style: Style = PointStyle):
        self.x = x
        self.y = y

        self.start = start
        self.extent = extent

        self.radius = radius

        self.style = style

    def __iter__(self):
        yield self.x, self.y
        yield self.start
        yield self.extent
        yield self.radius

    def draw(self, canvas: tkinter.Canvas, real):
        P1 = transpose((self.x - self.radius, self.y - self.radius), real)
        P2 = transpose((self.x + self.radius, self.y + self.radius), real)
        canvas.create_arc(P1, P2,
                          fill=self.style.fill,
                          outline=self.style.outline, width=self.style.thickness,
                          start=self.start + 90, extent=0 - self.extent,
                          style=tkinter.PIESLICE, )


class Bitmap(DrawObject):
    def __init__(self, x, y, image: str, style: Style = PointStyle):
        self.x = x
        self.y = y

        self.image = image

        self.style = style

    def __iter__(self):
        yield self.x, self.y
        yield self.image

    def draw(self, canvas: tkinter.Canvas, real):
        if self.style.anchor == "nw":
            anchor = tkinter.NW
        elif self.style.anchor == "n":
            anchor = tkinter.N
        elif self.style.anchor == "ne":
            anchor = tkinter.NE
        elif self.style.anchor == "w":
            anchor = tkinter.W
        elif self.style.anchor == "center" or self.style.anchor == "centre":
            anchor = tkinter.CENTER
        elif self.style.anchor == "e":
            anchor = tkinter.E
        elif self.style.anchor == "sw":
            anchor = tkinter.SW
        elif self.style.anchor == "s":
            anchor = tkinter.S
        elif self.style.anchor == "se":
            anchor = tkinter.SE
        else:
            anchor = None

        canvas.create_bitmap(transpose((self.x, self.y), real),
                             bitmap=self.image, anchor=anchor)


class Image(DrawObject):
    def __init__(self, x, y, sprite: Sprite, style: Style = PointStyle):
        self.x = x
        self.y = y

        self.sprite = sprite

        self.style = style

    def __iter__(self):
        yield self.x, self.y
        yield self.sprite

    def draw(self, canvas: tkinter.Canvas, real):
        self.sprite.height = self.style.height
        self.sprite.width = self.style.width
        photo_image = self.sprite.image()

        return canvas.create_image(
            transpose((self.x, self.y), real),
            image=photo_image, anchor=self.style.anchor), photo_image
