import sys
sys.stdin = open("swea_4waypractice(14889_.txt")

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_sum = 0
    for i in range(N):
        for j in range(N):
            s = 0 # 내 주위 값과 계산한거(얘는 1개를 기준으로 한거임)
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                ni, nj = i + di, j + dj # 기준 주변의 원소들의 인덱스(주소)
                if 0 <= ni < N and 0 <= nj < N:
                    s += abs(arr[i][j]-arr[ni][nj])
            total_sum += s
    print(f"#{tc} {total_sum}")