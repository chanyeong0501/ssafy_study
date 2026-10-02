import sys
sys.stdin = open("swea_최소합(11760).txt")

def find_sum(i, j, current_sum):
    global min_sum
    if current_sum >= min_sum:
        return
    if i == n-1 and j == n-1:
        min_sum = min(min_sum, current_sum)
        return
    for di, dj in [[0, 1], [1, 0]]:
        si, sj = i + di, j + dj
        if 0 <= si < n and 0 <= sj < n:

            find_sum(si, sj, current_sum + arr[si][sj])

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    # n * n판 받아옴.
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 10000000
    find_sum(0, 0, arr[0][0])
    print(f"#{tc} {min_sum}")