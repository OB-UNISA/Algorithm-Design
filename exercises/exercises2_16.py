from random import randint
from termcolor import colored
import colorama

colorama.init()


def alg(a, i, j, n, k):
    if i > n - 1 or j < 0:
        return False
    c = a[i][j]
    if k == c:
        return True
    if k > c:
        return alg(a, i, j - 1, n, k)
    else:
        return alg(a, i + 1, j, n, k)


LIM = 15

array = [[20, 17, 14, 10], 
               [18, 15, 13, 8],
               [13, 10, 9, 5],
               [7, 5, 3, 0]]
_n = len(array[0])

for _ in range(LIM // 2):
    r = randint(LIM * -1, LIM)
    for ind1 in range(_n):
        for ind2 in range(_n):
            if r % 2 == 0:
                array[ind1][ind2] = array[ind1][ind2] + r
            else:
                array[ind1][ind2] = array[ind1][ind2] - r
    
    if randint(0, 2) == 1:
        _k = array[randint(0, _n - 1)][randint(0, _n -1)]
    else:
        _k = randint(LIM * -1, LIM)
    
    alg_res = alg(array, 0, _n - 1, _n, _k)

    expected_value = False
    for v in array:
        if _k in v:
            expected_value = True
            break
        

    print(f'array: {array}\nn : {_n}\nk: {_k}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res == expected_value else colored("False", "red")}\n')
