if __name__ == '__main__':
    import helpful as util
else:
    from . import helpful as util


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def lagrange(x, pts):
    """
    Interpolates a group of points according to lagrange polynomial interpolation.
    Beware of Runge's phenomenon.
    :param pts: Points to interpolate
    :param x: get lagrange at this x (lagrange is function like y = f(x))
    :return: Point at x
    """
    n = len(pts)

    def pj(j):
        def inner(k):
            return (
                    (x - pts[k - 1][0]) /
                    (pts[j - 1][0] - pts[k - 1][0])
            )

        p1 = pts[j - 1][1]
        p2 = util.pi(1, j - 1, inner)

        p3 = util.pi(j + 1, n, inner)

        return p1 * p2 * p3

    return x, util.sigma(1, n, pj)

