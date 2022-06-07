def alg(SOL, k, n):
    if k == n - 1:
        print(SOL)
    else:
        print(SOL[:k + 1])
        for x in ['a', 'b', 'c']:
            SOL[k + 1] = x
            alg(SOL, k + 1, n)
            


_n = int(input('n: '))
alg([None for _ in range(_n)], -1, _n)
