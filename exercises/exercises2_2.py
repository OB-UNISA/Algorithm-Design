from random import randint
from termcolor import colored


def alg(a, i, j, L, U):
    if i == j:
        if L <= a[i] <= U:
            return 1
        else:
            return 0

    m = (i + j) // 2
    return alg(a, i, m, L, U) + alg(a, m + 1, j, L, U)

LIM = 15
for k in range(LIM // 2):
    array = [randint(LIM * -1, LIM) for _ in (range(randint(1, LIM)))]
    _n = len(array)
    _L = randint(1, LIM)
    _U = randint(_L, LIM)
    
    alg_res = alg(array, 0, _n - 1, _L, _U)
    
    expected_value = 0
    for el in array:
        if _L <= el <= _U:
            expected_value += 1
    
    print(f'array: {array}\nn : {_n}\nL: {_L}\nU: {_U}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
