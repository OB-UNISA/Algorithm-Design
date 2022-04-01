from random import randint
from termcolor import colored
import colorama

colorama.init()


def findL(a, i, j, L):
    if i == j:
        if a[i] > L:
            return i
        else:
            return "non c'è"

        m = (i + j) // 2
        if a[m] > L:
            return findL(a, i, m, L)
        else:
            return findL(a, m + 1, j, L)


def findU(a, i, j, U):
    if i == j:
        if a[i] < U:
            return i
        else:
            return "non c'è"

    m = (i + j) // 2
    if a[m] < U:
        return findU(a, m, j, U)
    else:
        return findU(a, i, m - 1, U)


def alg(a, i, j, L, U):
    if i == j:
        if L <= a[i] <= U:
            return 1
        else:
            return 0

    indL = findL(a, i, j, L)
    indU = findU(a, i, j, U)

    if indL == "non c'è" or indU == "non c'è":
        return 0
    else:
        return indU - indL


LIM = 15
for k in range(LIM // 2):
    array = [randint(LIM * -1, LIM) for _ in (range(randint(1, LIM)))]
    array.sort()
    array = list(dict.fromkeys(array))
    _n = len(array)
    _L = randint(LIM * -1, LIM)
    _U = randint(_L, LIM)

    alg_res = alg(array, 0, _n - 1, _L, _U)

    expected_value = 0
    for el in array:
        if _L <= el <= _U:
            expected_value += 1

    print(f'array: {array}\nn : {_n}\nL: {_L}\nU: {_U}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
