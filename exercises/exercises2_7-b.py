from random import randint
from termcolor import colored
from collections import deque


def alg(a, i, j):
    if i == j:
        return a[i]
    if j - i == 1:
        return min(a[j], a[i])
    m = (i + j) // 2
    if a[m-1] > a[m]:
        return a[m]
    if a[m] > a[j]:
        return alg(a, m + 1, j)
    else:
        return alg(a, i, m)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(0, LIM) for _ in (range(randint(1, LIM)))]
    array.sort()
    _n = len(array)
    array = deque(array)
    _k = randint(0, _n)
    array.rotate(_k * -1)

    alg_res = alg(array, 0, _n - 1)

    expected_value = min(array)

    print(f'array: {array}\nn : {_n}\nk: {_k}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
