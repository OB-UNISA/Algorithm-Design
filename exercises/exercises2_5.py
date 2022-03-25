from random import randint
from termcolor import colored

def alg(a, i, j):
	if i == j:
		return False
	
	m = (i + j) // 2
	if a[m] == a[m +1]:
		return True
	else:
		return  alg(a, i, m) or alg(a, m + 1, j)

LIM = 15

for k in range(7):
	array = [randint(0, LIM) for _ in (range(randint(1, LIM)))]
	array.sort()
	_n = len(array)
	
	alg_res = alg(array, 0, _n - 1)
	
	expected_value = False
	for ind in range(_n - 1):
		if array[ind] == array[ind + 1]:
			expected_value = True
			break
	
	print(f'array: {array}\nn : {_n}\nexpected result: {expected_value}\nalg result: {alg_res}\nsame results: {colored("True", "green") if expected_value == alg_res else colored("False", "red")}\n')
	