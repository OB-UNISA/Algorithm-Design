from random import randint
from termcolor import colored
import colorama

colorama.init()

# it does not work when multiplying 2 negative numbers the result is N


def alg(a, i, j, N):
    if i == j:
        return False
    c = a[i] * a[j]
    if c == N:
        return True
    if c > N:
        return alg(a, i, j - 1, N)
    else:
        return alg(a, i + 1, j, N)


LIM = 15

for _ in range(LIM // 2):
    array = [randint(LIM * -1, LIM) for _ in range(randint(1, LIM))]
    array.sort()
    _n = len(array)
    if randint(0, 1) == 1:
        _N = array[randint(0, _n - 1)] * array[randint(0, _n - 1)]
    else:
        _N = randint(LIM * -2, LIM * 2)
    alg_res = alg(array, 0, _n - 1, _N)

    expected_value = False
    if _n != 1:
        for ind1 in range(0, _n):
            for ind2 in range(ind1 + 1, _n):
                if array[ind1] * array[ind2] == _N:
                    expected_value = True
                    break

    print(f'array: {array}\nn : {_n}\nN: {_N}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res == expected_value else colored("False", "red")}\n')
