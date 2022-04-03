from random import randint
from termcolor import colored
import colorama

colorama.init()


def alg(a, i, j):
    if j - i == 1:
        return j

    m = (i + j) // 2
    if a[m] > a[j]:
        return alg(a, m, j)
    else:
        return alg(a, i, m)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(0, LIM) for _ in range(randint(2, LIM))]
    array[-1] = array[0] - randint(1, LIM)
    _n = len(array)

    alg_res = alg(array, 0, _n - 1)

    expected_value = []
    for ind in range(1, _n):
        if array[ind] < array[ind - 1]:
            expected_value.append(ind)

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res in expected_value else colored("False", "red")}\n')
