# https://www.youtube.com/watch?v=QHdU1XRB9uw
# https://github.com/Supreme-Sector/Python-Perlin-Noise/blob/master/perlin_noise/perlin.py
import json
import random
import time

from Graphic import element, draw_object
from Maf.interp import lerp
from Util.struc import RRange as rrange


def ease(x) -> float:
    return (6 * x ** 5) \
        - (15 * x ** 4) \
        + (10 * x ** 3)


seed = time.time()
generator = random.Random()

generator.seed(seed)
random.seed(seed)

# values = [generator.uniform(-1, 1), generator.uniform(-1, 1)]

with open(r"test\noise.json", "rb") as file:
    values = json.load(fp=file)

lower_bound = 0
upper_bound = 2


def get_value_at(t: float):
    global upper_bound, lower_bound

    if t < lower_bound:
        raise Exception(f"Value {t} out of bounds")

    while t > upper_bound - 2:
        values.append(generator.uniform(-1, 1))
        upper_bound = len(values)

    d1 = t - int(t)
    d2 = d1 - 1

    a1 = values[int(t)] * d1
    a2 = values[int(t) + 1] * d2

    amt = ease(d1)

    print("D1:", d1, "D2:", d2, "A1:", a1, "A2:", a2, "AMT:", amt, "lerp", lerp(a1, a2, amt))
    return lerp(a1, a2, amt)


curve = []
for x in rrange(0, 20, 0.1):
    print(f"{x}: {get_value_at(x)}")
    curve.append(
        ((x - 10) * 24, get_value_at(x) * 180)
    )

root = element.Window()
canvas = element.Canvas(root)

canvas.pack()

canvas.create(
    draw_object.Lines(curve, draw_object.Style(
        thickness=1, fill="#FF8800"
    ))
)

root.start()
