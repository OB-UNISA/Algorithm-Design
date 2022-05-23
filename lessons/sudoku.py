# need to be fixed, there are some bugs because the solution is partially wrong
R = []
C = []
B = []
x = [0 for _ in range(81)]


def rigaColonnaBlocco(l):
    i = l // 9
    j = l % 9
    k = 3 * (i // 3) + (j // 3)

    return i, j, k


def print_grid(grid):
    for i in range(0, 81, 9):
        print(grid[i:i+9])

    print()


def inizializza(a):
    for i in range(9):
        R.append(set())
        C.append(set())
        B.append(set())

    for l in range(81):
        if a[l] != 0:
            i, j, k = rigaColonnaBlocco(l)
            R[i].add(a[l])
            C[j].add(a[l])
            B[k].add(a[l])


def sudoku(a, l):
    print(l)
    if l == 81:
        return x
    else:
        if a[l] != 0:
            x[l] = a[l]
            sudoku(a, l + 1)
        else:
            i, j, k = rigaColonnaBlocco(l)
            scelta = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - \
                set().union(R[i], C[j], B[k])
            print(scelta)
            for y in scelta:
                R[i].add(y)
                C[j].add(y)
                B[k].add(y)
                x[l] = y

                sudoku(a, l + 1)

                try:
                    R[i].remove(y)
                except Exception:
                    pass
                try:
                    C[j].remove(y)
                except Exception:
                    pass
                try:
                    B[k].remove(y)
                except Exception:
                    pass


def main():

    game = [5, 3, 0, 0, 7, 0, 0, 0, 0,
            6, 0, 0, 1, 9, 5, 0, 0, 0,
            0, 9, 8, 0, 0, 0, 0, 6, 0,
            8, 0, 0, 0, 6, 0, 0, 0, 3,
            4, 0, 0, 8, 0, 3, 0, 0, 1,
            7, 0, 0, 0, 2, 0, 0, 0, 6,
            0, 6, 0, 0, 0, 0, 2, 8, 0,
            0, 0, 0, 4, 1, 9, 0, 0, 5,
            0, 0, 0, 0, 8, 0, 0, 7, 9]

    inizializza(game)
    print_grid(game)

    sudoku(game, 0)
    print_grid(x)


main()
