from random import randint
from termcolor import colored
from collections import deque


def alg(a, i, j, n):
    if i == j:
        return 1
    if j - i == 1:
        if a[i] > a[j]:
            return n - j
        else:
            return n - i

    m = (i + j) // 2
    if a[m-1] > a[m]:
        return n - m
    if a[m] > a[j]:
        return alg(a, m + 1, j, n)
    else:
        return alg(a, i, m, n)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(0, LIM) for _ in (range(randint(1, LIM)))]
    array.sort()
    _n = len(array)
    array = deque(array)
    _k = randint(0, _n)
    array.rotate(_k * -1)

    alg_res = alg(array, 0, _n - 1, _n)

    if _k in (0, _n):
        expected_value = [0, _n]
    elif array.count(array[0]) == _n:
        # if the array has all elements equal, any answer 0...n is right
        expected_value = list(range(0, _n + 1))
    else:
        expected_value = [_k]

    print(f'array: {array}\nn : {_n}\nk: {_k}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res in expected_value else colored("False", "red")}\n')
