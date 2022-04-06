from random import randint
from termcolor import colored
import colorama

colorama.init()


def alg(a, i, j, n):
    m = (i + j) // 2
    if (m == 0 or a[m] <= a[m - 1]) and (m == n - 1 or a[m] <= a[m + 1]):
        return m
    elif m > 0 and a[m - 1] < a[m]:
        return alg(a, i, m - 1, n)
    else:
        return alg(a, m + 1, j, n)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(0, LIM) for _ in range(1, randint(2, LIM))]
    _n = len(array)

    print(array)
    alg_res = alg(array, 0, _n - 1, _n)

    expected_value = []
    if _n == 1:
        expected_value.append(0)
    else:
        if array[0] <= array[1]:
            expected_value.append(0)
        if array[_n - 1] <= array[_n - 2]:
            expected_value.append(_n - 1)

        for ind in range(1, _n - 1):
            if array[ind] <= array[ind - 1] and array[ind] <= array[ind + 1]:
                expected_value.append(ind)

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res in expected_value else colored("False", "red")}\n')
