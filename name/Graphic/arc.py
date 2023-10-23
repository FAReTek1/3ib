import tkinter as tk
import math
import time

root = tk.Tk()
canvas = tk.Canvas(root, width=480, height=360)
start = time.time()

mx = 90
my = 90


def mouse(event):
    global mx, my
    mx = event.x
    my = event.y


def render():
    global mx, my, start

    canvas.delete("all")
    if my == 180:
        angle = 90
    else:
        angle = math.atan((mx - 240) / (my - 180)) * (180 / math.pi)
        if my > 180:
            angle += 180

    inner = 50 + math.sin(5 * (time.time() - start)) * 10
    outer = 70 + math.cos(2.5 * (time.time() - start)) * 15

    draw_arc(canvas, 240, 180, inner, outer, angle, 135 + math.sin(3 * (time.time() - start)) * 10, "#00FFFF")
    canvas.create_oval(240 - inner, 180 - inner, 240 + inner, 180 + inner)
    canvas.create_oval(240 - outer, 180 - outer, 240 + outer, 180 + outer)

    root.after(1, render)


def draw_arc(canvas: tk.Canvas, x, y, inner_radius, outer_radius, start, extent, colour):
    middle_radius = (inner_radius + outer_radius) / 2
    canvas.create_arc(x - middle_radius, y - middle_radius, x + middle_radius, y + middle_radius,
                      width=abs(outer_radius - inner_radius), style=tk.ARC, start=start + 90, extent=0 - extent,
                      outline=colour)


root.bind("<Motion>", mouse)
canvas.pack()
root.after(1, render)

root.mainloop()