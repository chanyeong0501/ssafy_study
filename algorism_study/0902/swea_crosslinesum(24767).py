import sys
sys.stdin = open("swea_crosslinesum(24767).txt", "r")

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_num = 0
    for i in range(N): #어짜피 N*N의 배열이라서 한번만 하면 됨.
        sum_num += arr[i][i] + arr[i][N-1-i]
    if N%2: # 홀수인 경우에만 적용함
        sum_num = sum_num - arr[N//2][N//2]

    print(f"{tc} {result}")