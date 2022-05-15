#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально
задействовав имеющиеся в Python средства перегрузки операторов.

Поле first — целое положительное число, числитель; поле second — целое положительное
число, знаменатель. Реализовать метод ipart() — выделение целой части дроби
first/second. Метод должен проверять неравенство знаменателя нулю.
"""


class IntegerPart:

    def __init__(self, first=0, second=0):
        self.first = first
        self.second = second
        if self.first == 0:
            raise ValueError

    def __floordiv__(self, other):
        f = self.first // self.second
        s = other.first // other.second
        return f, s


if __name__ == "__main__":
    int1 = IntegerPart(50, 20)
    int2 = IntegerPart(25, 3)
    print(f"Целочисленное деление: {int1 // int2}")
