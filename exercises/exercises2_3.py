from random import randint
from termcolor import colored


def alg(a, i, j, x):
    if i == j:
        if a[i] >= x:
            return i
        else:
            return "non c'è"

    m = (i + j) // 2
    if a[m] < x:
        return alg(a, m + 1, j, x)
    else:
        return alg(a, i, m, x)


LIM = 15

for k in range(LIM // 2):
    array = [randint(0, LIM) for _ in (range(randint(1, LIM)))]
    array.sort()
    _n = len(array)
    if k % 2 == 0:
        _x = randint(0, LIM)
    else:
        _x = randint(0, LIM * 2)

    alg_res = alg(array, 0, _n - 1, _x)

    expected_value = "non c'è"
    for ind, el in enumerate(array):
        if el >= _x:
            expected_value = ind
            break

    print(f'array: {array}\nn : {_n}\nx: {_x}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
