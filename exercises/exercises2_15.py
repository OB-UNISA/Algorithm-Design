from random import randint
from termcolor import colored
import colorama

colorama.init()


def alg(a, i, j):
    if i == j:
        return "non c'è"
    if j - i == 1:
        if a[i] + 1 < a[j]:
            return j
        else:
            return "non c'è"

    m = (i + j) // 2
    if abs(a[j] - a[m]) > j - m:
        return alg(a, m, j)
    elif abs(a[m] - a[i]) > m - i:
        return alg(a, i, m)
    else:
        return "non c'è"


LIM = 15

for _ in range(LIM // 2):
    if randint(0, 2) == 1:
        r1 = randint(LIM * - 1, LIM - 1)
        array = list(range(r1, randint(r1 + 1, LIM)))
    else:
        array = [randint(LIM * -1, LIM) for _ in (range(randint(1, LIM)))]
        array.sort()
        array = list(dict.fromkeys(array))
    _n = len(array)

    alg_res = alg(array, 0, _n - 1)

    expected_value = []
    for ind in range(1, _n):
        if array[ind - 1] + 1 < array[ind]:
            expected_value.append(ind)
    if len(expected_value) == 0:
        expected_value.append("non c'è")

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res in expected_value else colored("False", "red")}\n')
