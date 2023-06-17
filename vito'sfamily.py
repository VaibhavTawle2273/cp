#Problem solution : 10041	Vito's Family


def calculate_min_distance(r, relatives):
    relatives.sort() 
    median = relatives[r // 2]  

    total_distance = 0
    for relative in relatives:
        total_distance += abs(relative - median)  

    return total_distance


num_test_cases = int(input())

for _ in range(num_test_cases):
    r, *relatives = map(int, input().split())  
    min_distance = calculate_min_distance(r, relatives)  
    print(min_distance)