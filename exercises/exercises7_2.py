def alg(SOL, k, c, n, tot):
    if k == n - 1:
        print(SOL)
    else:
        SOL[k + 1] = 0
        alg(SOL, k + 1, c, n, tot)
        if tot < c:
            SOL[k + 1] = 1
            alg(SOL, k + 1, c, n, tot + 1)


_n = int(input('n: '))
_c = int(input('c: '))
alg([0 for _ in range(_n)], -1, _c, _n, 0)
