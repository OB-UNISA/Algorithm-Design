from random import randint
from termcolor import colored


def alg(a, i, j):
    if i == j:
        return 0
    if j - i == 1:
        if a[i] * a[i + 1] > 0:
            return 1
        else:
            return 0

    m = (i + j) // 2
    if a[m] * a[m + 1] > 0:
        return 1 + alg(a, i, m) + alg(a, m + 1, j)
    else:
        return alg(a, i, m) + alg(a, m + 1, j)


LIM = 15

for k in range(LIM // 2):
    array = [randint(LIM * - 1, LIM) for _ in (range(randint(1, LIM)))]
    _n = len(array)

    alg_res = alg(array, 0, _n - 1)

    expected_value = 0
    for ind in range(_n - 1):
        if array[ind] * array[ind + 1] > 0:
            expected_value += 1

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
