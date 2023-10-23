import math

from scipy.special import lambertw

if __name__ == '__main__':
    from const import GOLDEN_RATIO, SQRT_5, PI, TAU, E
    from Util.struc import RRange as rrange
    from exception import DomainError
    _ = rrange

def sigma(start: int, end: int, func):
    total = 0
    for n in range(start, end + 1):
        total += func(n)
    return total


def pi(start: int, end: int, func):
    product = 1
    for n in range(start, end + 1):
        product *= func(n)
    return product


def factorial(x):
    return math.gamma(x + 1)


def inv_fact(y, branch: int = 0, tol: float = 1e-8) -> complex:
    """Inverse of factorial based on stirling's approximation (far from perfect)"""
    numerator = math.log(y / (2 * math.pi))
    denominator = lambertw((1 / math.e) * math.log(y / (2 * math.pi)), branch, tol)
    return numerator / denominator


def lucas(_n) -> int:
    """Return the nth lucas number (not an extension)"""
    # https://www.desmos.com/calculator/i2ixusaqyn
    if _n == 1:
        # Catch special cases
        return 2
    if _n == 2:
        # Catch special cases
        return 1
    return round(GOLDEN_RATIO ** round(_n - 1))


def fibonacci(_n) -> float:
    """Returns the nth fibonacci number. Works with decimals"""
    # https://www.desmos.com/calculator/wcepifft6s
    if _n % 2 > 1:
        return (GOLDEN_RATIO ** _n + GOLDEN_RATIO ** -_n) / SQRT_5
    else:
        return (GOLDEN_RATIO ** _n - GOLDEN_RATIO ** -_n) / SQRT_5


def continuous_fibonacci(_n) -> float:
    """
    Return the nth fibonacci number, but the 2 graphs are oscillated to and fro by a sine wave, to make it continuous.
    """
    # https://www.desmos.com/calculator/wcepifft6s
    # https://math.stackexchange.com/questions/3821443/continuous-fibonacci-number-fn
    # No changes made, all by @J.M. ain't a mathematician
    return (GOLDEN_RATIO ** _n - math.cos(_n * PI) * GOLDEN_RATIO ** -_n) / SQRT_5

def stirling_approximation(_n) -> float:
    """"""
    if _n < 0:
        raise DomainError(f"Stirling's approximation can only take values of n ≥ 0, not {_n}")
    return math.sqrt(TAU * _n) * ((_n/E) ** _n)
