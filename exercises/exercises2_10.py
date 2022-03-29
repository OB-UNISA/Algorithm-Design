from random import randint
from termcolor import colored


def alg(a, i, j):
    if i == j:
        return "non c'è"
    if j - i == 1:
        if a[i] < 0 and a[j] > 0:
            return i
        else:
            return "non c'è"

    m = (i + j) // 2
    if a[m] < 0 and a[m + 1] > 0:
        return m
    elif a[m] > 0:
        return alg(a, i, m)
    else:
        return alg(a, m, j)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(LIM * -1, LIM) for _ in (range(randint(1, LIM)))]
    array.sort()
    _n = len(array)

    alg_res = alg(array, 0, _n - 1)
    
    expected_value = "non c'è"
    for ind in range(_n - 1):
        if array[ind] < 0 and array[ind + 1] > 0:
            expected_value = ind
            break

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res == expected_value else colored("False", "red")}\n')
