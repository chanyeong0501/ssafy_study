import sys
sys.stdin = open("swea_미로(11879).txt")

def dfs(r, c):
    global flag
    if flag == 1:
        return
    if arr[r][c] == 3:
        flag = 1
        return
    visited[r][c] = 1
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    for d in range(4):
        di = r + dr[d]
        dj = c + dc[d]
        if 0 <= di < N and 0 <= dj < N and visited[di][dj] == 0 and arr[di][dj] != 1:
            dfs(di, dj)

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for r in range(N):
        for c in range(N):
        # 배열 돌면서 시작점 좌표와 끝점 좌표를 찾음.
            if arr[r][c] == 2:
                start_r, start_c = r, c
            if arr[r][c] == 3:
                end_r, end_c = r, c
    # 방문 확인을 위한 배열 만듦
    flag = 0
    visited = [[0]*N for _ in range(N)]
    dfs(start_r, start_c)
    print(f"{tc} {flag}")
