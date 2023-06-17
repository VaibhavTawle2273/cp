def updateCell(i, j, m, n, arr):
    if i < 0 or i >= m or j < 0 or j >= n or arr[i][j] == '*':
        return
    if arr[i][j] == '.':
        arr[i][j] = '1'
    elif arr[i][j].isdigit():
        arr[i][j] = str(int(arr[i][j]) + 1)

def updateNeighbors(i, j, m, n, arr):
    for ii in range(-1, 2):
        for jj in range(-1, 2):
            updateCell(i+ii, j+jj, m, n, arr)

def solve(m, n, arr):
    for i in range(m):
        for j in range(n):
            if arr[i][j] == '*':
                updateNeighbors(i, j, m, n, arr)
            elif arr[i][j] == '.':
                arr[i][j] = '0'
    return arr

if __name__ == '__main__':
    arr = []
    while True:
        try:
            m, n = map(int, input().split())
            if m == 0 or n == 0:
                break
            fields = []
            for _ in range(m):
                cells = list(input())
                fields.append(cells)
            arr.append(fields)
        except EOFError:
            break
    for i in range(len(arr)):
        res = solve(len(arr[i]), len(arr[i][0]), arr[i])
        print('Field #{}:'.format(i+1))
        for row in res:
            print(''.join(row))
        if i != len(arr) - 1:
            print('')