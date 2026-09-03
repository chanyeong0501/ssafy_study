import sys
sys.stdin = open("swea_partsum(4837).txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    n = 12
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    count_case = 0
    for i in range(1 << 12):
        part_sum = 0
        element_count = 0
        for j in range(12):
            if i & (1 << j):
                part_sum += A[j]
                element_count += 1
        if element_count == N and part_sum == M:
            count_case += 1
    print(count_case)

