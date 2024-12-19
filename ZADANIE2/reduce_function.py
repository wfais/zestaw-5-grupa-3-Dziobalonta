from fractions import Fraction
from functools import reduce


def product(fracs):
    result = Fraction(1, 1)

    for frac in fracs:
        result *= frac

    return result.numerator, result.denominator


if __name__ == "__main__":
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
