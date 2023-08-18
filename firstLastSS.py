def search_first(a, k, i, j):
    if i == j:
        if a[i].startswith(k):
            return i
        return -1

    m = (i + j) // 2
    if a[m].startswith(k):
        return search_first(a, k, i, m)
    return search_first(a, k, m + 1, j)


def search_last(a, k, i, j):
    two_el = j - i == 1
    if two_el:
        if a[j].startswith(k):
            return j
    if i == j or two_el:
        if a[i].startswith(k):
            return i
        return -1

    m = (i + j) // 2
    if a[m].startswith(k):
        return search_last(a, k, m, j)
    return search_last(a, k, i, m - 1)


array = ['a', 'air', 'airplane', 'airport', 'airport', 'albert']
n = len(array) - 1
_k = 'air'

s = search_first(array, _k, 0, n)
if s != -1:
    d = search_last(array, _k, s, n)
    print(array, s, d, sep='\n')
else:
    print('No results')
