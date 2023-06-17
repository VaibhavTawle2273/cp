#Problem solution : 00100 - The 3n + 1 problem


def calculate_cycle_length(n):
    cycle_length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        cycle_length += 1
    return cycle_length


def find_maximum_cycle_length(i, j):
    maximum_cycle_length = 0
    for num in range(i, j + 1):
        cycle_length = calculate_cycle_length(num)
        maximum_cycle_length = max(maximum_cycle_length, cycle_length)
    return maximum_cycle_length

while True:
    try:
        i, j = map(int, input().split())
        maximum_cycle_length = find_maximum_cycle_length(i, j)
        print(i, j, maximum_cycle_length)
    except EOFError:
        break