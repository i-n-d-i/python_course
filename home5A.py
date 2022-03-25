from math import *
from decimal import *


def chudnovsky():
    getcontext().prec += 2
    pi = Decimal(0)
    k = 0
    while k < 100:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3 * k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    getcontext().prec -= 2
    return pi


def sin_taylor(x):
    answer, div = 0, 1
    elem = x
    while div < 2000:
        answer += elem
        elem *= -x * x / ((div + 1) * (div + 2))
        div += 2
    return answer


def cos_taylor(x):
    answer, div = 0, 0
    elem = 1
    while div < 2000:
        answer += elem
        elem *= -x * x / ((div + 1) * (div + 2))
        div += 2
    return answer


a = input()
e = int(input())
if e <= 15:
    getcontext().prec = e
    a = float(a) * pi * 0.005
    print(Decimal(tan(a)) / Decimal(1))
else:
    getcontext().prec = e + 2
    a = Decimal(a) * Decimal(chudnovsky()) / Decimal(200)
    answer = sin_taylor(a) / cos_taylor(a)
    getcontext().prec -= 2
    print(answer / Decimal(1))
