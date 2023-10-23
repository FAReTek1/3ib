import Maf as maf
from Graphic import element, draw_object
from Util.struc import RRange as rrange

root = element.Window()
canvas = element.Canvas(root)


def gen_curve(func, *args, **kwargs):
    co_ords = []

    if kwargs.get("start") is None or kwargs.get("end") is None:
        minimum = args[0][0][0]
        maximum = minimum
        for pt in args[0]:
            if pt[0] > maximum:
                maximum = pt[0]

            if pt[0] < minimum:
                minimum = pt[0]
        start, end = minimum, maximum
    else:
        start = kwargs.get("start")
        end = kwargs.get("end")

    for x in rrange(start, end, 0.01):
        co_ords.append(a := func(x, args[0]))
    return co_ords


pts = [(15, 41),
    (-69, 69),
    (200, 23),
    (-156, -61)]
lines = draw_object.Lines(gen_curve(maf.interp.lagrange, pts, start=-240, end=240))
canvas.create(lines)

for point in pts:
    canvas.create(
        draw_object.Point(point[0], point[1],
                          draw_object.Style(fill="#FF00AA", size=7, thickness=2))
    )

canvas.pack()
root.start()
