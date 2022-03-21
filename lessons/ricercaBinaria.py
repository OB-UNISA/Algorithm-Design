from random import randint


def RicercaBinaria(a, k, s, d):
    if s == d:
        if k == a[s]:
            return s
        return "non c'è"

    c = (s + d) // 2
    if k <= a[c]:
        return RicercaBinaria(a, k, s, c)
    return RicercaBinaria(a, k, c + 1, d)


LIM = 10

for i in range(7):
    array = [randint(0, LIM) for _ in range(randint(5, LIM))]
    array.sort()
    _n = len(array)
    if i % 2 == 0:
        _k = array[randint(0, _n - 1)]
    else:
        _k = randint(0, LIM * 2)

    alg_res = RicercaBinaria(array, _k, 0, _n - 1)

    expected_value = "non c'è"
    for ind, el in enumerate(array):
        if array[ind] == _k:
            expected_value = ind
            break

    print(f'array: {array}\nk: {_k}\nn : {_n - 1}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {expected_value == alg_res}\n')
