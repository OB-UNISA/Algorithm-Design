from random import randint
from termcolor import colored


def alg(a, i, j):
    if i == j:
        return i

    m = (i + j) // 2
    if a[m] == 0:
        return m
    elif a[m] > 0:
        return alg(a, i, m - 1)
    else:
        return alg(a, m + 1, j)


LIM = 15
arrays = [[-2, -1, 0, 1, 2, 3, 4], [0, 1, 1, 1, 1, 1],
          [0, 0, 0, 0, 1], [-1, -1, 0, 1, 2, 2, 3], [0, 1]]

# the code below always place the '0' at a[n-2]
for _ in range(LIM // 2):
    array = []
    flag = False
    r = randint(LIM // 2 * -1, 0)
    array.append(r)
    l = 0
    while True:
        if l == LIM // 2:
            flag = True
        if not flag:
            r = randint(r - 1, r + 1)
            array.append(r)
        else:
            r += 1
            array.append(r)
        if r > 0:
            break
        l += 1
    arrays.append(array)

for array in arrays:
    _n = len(array)

    alg_res = alg(array, 0, _n - 1)

    expected_value = []
    for ind in range(_n):
        if array[ind] == 0:
            expected_value.append(ind)

    print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if alg_res in expected_value else colored("False", "red")}\n')
