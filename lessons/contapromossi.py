from random import randint


def contapromossi(a, k, n, i, j):
    if i == j:
        if k < a[i]:
            return n - i
        return 0

    m = (i + j) // 2
    if k >= a[m]:
        return contapromossi(a, k, n, m + 1, j)
    return contapromossi(a, k, n, i, m)


array = [randint(0, 30) for _ in range(randint(5, 20))]
array.sort()
_n = len(array)
_k = randint(0, 30)

alg_res = contapromossi(array, _k, _n, 0, _n - 1)

expected_value = 0
for ind, el in enumerate(array):
	if el > _k:
		expected_value = _n - ind
		break

print(f'array: {array}\nk: {_k}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {expected_value == alg_res}')
