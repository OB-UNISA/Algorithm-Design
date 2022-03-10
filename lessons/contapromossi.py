def contapromossi(a, k, n, i, j):
    if i == j:
        if k < a[i]:
            return n - i
        return 0

    m = (i + j) // 2
    if k >= a[m]:
        return contapromossi(a, k, n, m + 1, j)
    return contapromossi(a, k, n, i, m)


array = [10, 15, 16, 17, 18, 19, 20, 25, 27, 30]
len_array = len(array)

print(contapromossi(array, 17, len_array, 0, len_array - 1))
