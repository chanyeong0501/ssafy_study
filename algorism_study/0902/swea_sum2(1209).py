import sys
sys.stdin = open("swea_sum2(1209).txt")
T=10
for tc in range(1, T+1):
    tc_num = int(input())
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    final_sum_horizontal = 0
    final_sum_vertical = 0
    final_sum_cross = 0
    final_sum_reverse_cross = 0
    for i in range(N):
        sum_horizontal = 0
        sum_vertical = 0
        for j in range(N):
            sum_horizontal += arr[i][j]
            sum_vertical += arr[j][i]
            if sum_horizontal > final_sum_horizontal:
                final_sum_horizontal = sum_horizontal
            if sum_vertical > final_sum_vertical:
                final_sum_vertical = sum_vertical
        final_sum_cross += arr[i][i]
        final_sum_reverse_cross += arr[i][N-1-i]
    total_max = 0
    total_list = [final_sum_horizontal, final_sum_vertical, final_sum_cross, final_sum_reverse_cross]
    for num in total_list:
        if num > total_max:
            total_max = num
    print(f"#{tc_num} {total_max}")


