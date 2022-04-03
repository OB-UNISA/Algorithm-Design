from random import randint
from termcolor import colored
import colorama

colorama.init()


def alg(a, i, j):
    if i == j:
        return a[i]
        
    m = (i + j) // 2
    if a[m] == m:
        return alg(a, m + 1, j)
    else:
        return alg(a, i, m)


LIM = 15

for _ in range(LIM // 2):
    _n = randint(2, LIM)
    array = list(range(_n))
    r = randint(1, _n - 1)
    array.insert(r, r)
    _n += 1
    
    alg_res = alg(array, 0, _n - 1)

    expected_value = -1
    for ind in range(_n - 1):
        if array[ind] == array[ind+1]:
            expected_value = array[ind]

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res == expected_value else colored("False", "red")}\n')
