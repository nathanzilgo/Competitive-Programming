def greedy(wine_list):
    n = len(wine_list)
    total_work = 0
    for i in range(n-1):
        wine_list[i+1] += wine_list[i]
        total_work += abs(wine_list[i])
    return total_work

while True:
    num = int(input())
    if num != 0:
        arr = [int(i) for i in input().strip().split()]
        print(greedy(arr))
    else:
        break