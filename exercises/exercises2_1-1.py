from random import randint
from termcolor import colored

def alg(a, i, j):
	if i ==j:
		if a[i] >= 0:
			return 1
		else:
			return 0
	
	c = (i + j) // 2
	return alg(a, i, c) + alg(a, c +1, j)
	
array = [randint(-30, 30) for _ in (range(randint(1, 30)))]
_n = len(array)

alg_res = alg(array, 0, _n - 1)

expected_value = 0
for el in array:
	if el >= 0:
		expected_value += 1

print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
