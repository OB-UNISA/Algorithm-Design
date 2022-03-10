# Precontidion: n >= 1

def maxSommaConsecutiva1(a, n):
	sommaMassima = a[0]
	for i in range(n):
		for j in range(n):
			sommaCorrente = 0
			for k in range(i, j + 1):
				sommaCorrente += a[k]
		if sommaCorrente > sommaMassima:
			sommaMassima = sommaCorrente
			
	return sommaMassima
	
array = [3, -4, 5, 4]
len_array = len(array)

print('maxSommaConsecutiva1: ', maxSommaConsecutiva1(array, len_array))


def maxSommaConsecutiva2(a, n):
	sommaMassima = a[0]
	for i in range(n):
		sommaCorrente = 0
		for j in range(i, n):
			sommaCorrente += a[j]
			if sommaCorrente > sommaMassima:
				sommaMassima = sommaCorrente
	
	return sommaMassima
	
print('maxSommaConsecutiva2: ', maxSommaConsecutiva2(array, len_array))


def maxSommaConsecutiva4(a, n):
	sommaMassima = a[0]
	sommaMassimaFAQ = a[0]
	
	for i in range(1, n):
		if sommaMassimaFAQ + a[i] > a[i]:
			sommaMassimaFAQ = sommaMassimaFAQ + a[i]
		else:
			sommaMassimaFAQ = a[i]
		if sommaMassimaFAQ > sommaMassima:
			sommaMassima = sommaMassimaFAQ
			
	return sommaMassima
	
print('maxSommaConsecutiva4: ', maxSommaConsecutiva4(array, len_array))
