# Magic Square

n = int(input("Enter the no of element: "))

if (n % 2 != 0):

    magic_square = [[0 for _ in range(n)] for _ in range(n)]

    key = 1
    i = n // 2
    j = n - 1

    magic_square[i][j] = key

    while key < n * n:
        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j] != 0:
            j = j - 1
        else:
            i, j = new_i, new_j

        key += 1
        magic_square[i][j] = key

    for row in magic_square:
        print(row)

    ans = 'n'

else:
    print("Pls enter odd no")