from random import randint
from termcolor import colored


def alg(a, i, j):
    if i == j or j - i == 1:
        return 0

    m = (i + j) // 2
    if a[m] == a[m + 1] and a[m] == a[m - 1]:
        return 1 + alg(a, i, m) + alg(a, m, j)
    elif a[m] == a[m - 1]:
        return alg(a, i, m) + alg(a, m + 1, j)
    elif a[m] == a[m + 1]:
        return alg(a, i, m - 1) + alg(a, m, j)
    else:
        return alg(a, i, m - 1) + alg(a, m + 1, j)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(LIM * - 1, LIM) for _ in range(LIM // 2)]
    for flag in range(LIM // 2):
        if flag % 2 == 0 and randint(0, 5) == 2:
            array.insert(flag, array[flag])
            array.insert(flag, array[flag])
        elif flag % 3 == 0 and randint(0, 7) == 1:
            array.insert(flag, array[flag])
            array.insert(flag, array[flag])
            array.insert(flag, array[flag])
        elif randint(0, LIM // 3) == 0:
            array.insert(flag, array[flag])
            array.insert(flag, array[flag])
    _n = len(array)

    alg_res = alg(array, 0, _n - 1)

    expected_value = 0
    for ind in range(_n - 2):
        if array[ind + 1] == array[ind + 2] and array[ind + 1] == array[ind]:
            expected_value += 1

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res == expected_value else colored("False", "red")}\n')
