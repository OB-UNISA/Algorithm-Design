def alg(SOL, k, n):
    if k == n - 1:
        print(SOL)
    else:
        print(SOL)
        for x in ['a', 'b', 'c']:
            SOL.append(x)
            alg(SOL, k + 1, n)
            SOL.pop()
            
            

_n = int(input('n: '))
alg([], -1, _n)
    