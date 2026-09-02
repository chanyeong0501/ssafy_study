import sys
sys.stdin = open("swea_flykill(2001).txt")
T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_list = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_total = 0
            for p in range(M):
                for q in range(M):
                    sum_total += arr[i+q][j+p]
            sum_list += [sum_total]
    max_sum = 0
    for i in sum_list:
        if i > max_sum:
            max_sum = i
    print(f"{tc} {max_sum}")


