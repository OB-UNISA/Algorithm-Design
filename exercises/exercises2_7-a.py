from random import randint
from termcolor import colored
from collections import deque

def alg(a, i, j, k):
    if i == j or k ==0:
        return a[i]
    else:
        return a[j - k + 1]


LIM = 15

for _ in range(LIM // 2):
    array = [randint(0, LIM) for _ in (range(randint(1, LIM)))]
    array.sort()
    _n = len(array)
    array = deque(array)
    _k = randint(0, _n)
    array.rotate(_k * -1)

    alg_res = alg(array, 0, _n - 1, _k)

    expected_value = min(array)

    print(f'array: {array}\nn : {_n}\nk: {_k}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
