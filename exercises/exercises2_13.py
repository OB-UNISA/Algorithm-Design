from random import randint
from termcolor import colored


def alg(a, i, j, n):
    if i == j:
        if a[i] == 1:
            return n - i
        else:
            return 0

    m = (i + j) // 2
    if a[m] == 0:
        return alg(a, m + 1, j, n)
    else:
        return alg(a,i, m, n)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(0, 1) for _ in (range(randint(1, LIM)))]
    array.sort()
    _n = len(array)

    alg_res = alg(array, 0, _n - 1, _n)

    expected_value = 0
    for ind in range(_n):
        if array[ind] == 1:
            expected_value = _n - ind
            break

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res == expected_value else colored("False", "red")}\n')
