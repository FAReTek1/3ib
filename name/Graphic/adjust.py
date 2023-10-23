def HSV_to_RGB(h: float, s: float, v: float) -> tuple:
    h = h % 360
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c
    if 0 <= h < 60:
        r, g, b = c, x, 0
    elif 60 <= h < 120:
        r, g, b = x, c, 0
    elif 120 <= h < 180:
        r, g, b = 0, c, x
    elif 180 <= h < 240:
        r, g, b = 0, x, c
    elif 240 <= h < 300:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x
    r = (r + m) * 255
    g = (g + m) * 255
    b = (b + m) * 255
    return r, g, b


def RGB_to_HSV(r: float, g: float, b: float) -> tuple:
    r /= 255
    g /= 255
    b /= 255

    cmax = max(r, g, b)
    cmin = min(r, g, b)
    delta = cmax - cmin

    if delta == 0:
        h = 0
    elif cmax == r:
        h = 60 * (((g - b) / delta) % 6)
    elif cmax == g:
        h = 60 * (((b - r) / delta) + 2)
    else:
        h = 60 * (((r - g) / delta) + 4)

    if cmax == 0:
        s = 0
    else:
        s = delta / cmax

    v = cmax

    return h, s, v


def RGB_to_HEX(r: float, g: float, b: float) -> str:
    r, g, b = int(r), int(g), int(b)
    r = str(hex(r)).removeprefix("0x")
    g = str(hex(g)).removeprefix("0x")
    b = str(hex(b)).removeprefix("0x")

    if len(r) == 1:
        r = '0' + r
    if len(g) == 1:
        g = '0' + g
    if len(b) == 1:
        b = '0' + b

    return f"#{r + g + b}"


def HEX_to_RGB(HEX: str) -> tuple:
    r = int(HEX[1:3], 16)
    g = int(HEX[3:5], 16)
    b = int(HEX[5:7], 16)
    return r, g, b


def transpose_to_centre_origin(pt: tuple, element):
    return (
        pt[0] - element.width / 2,
        -1 * pt[1] + element.height / 2
    )


def transpose_to_top_left_origin(pt, element):
    return (
        pt[0] + element.width / 2,
        -1 * (pt[1] - element.height / 2)
    )
