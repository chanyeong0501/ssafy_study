import sys
sys.stdin = open("swea_colorprint(4836).txt")
T=int(input())
for tc in range(1, T+1):
    N = int(input()) # 색칠 횟수
    # 빈 도화지 만들기
    arr = [[0]*10 for _ in range(10)]
    # 왼쪽 위 좌표, 오른쪽 위 좌표 색받아서 칠하기
    for _ in range(N):
        r1, r2, c1, c2, color = map(int, input().split())
        #for문으로 색칠하기
        for i in range(r1, c1+1):
            for j in range(r2, c2+1):
                arr[i][j] += color
    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1
    print(f"#{tc} {count}")