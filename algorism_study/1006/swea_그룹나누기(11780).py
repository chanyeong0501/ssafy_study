import sys
sys.stdin = open("swea_그룹나누기(11780).txt")

def find_group(i):
    # 방문체크

    if visited[i] == 0:
        visited[i] = 1
    for w in path[i]:
        # 방문 안했을때
        if visited[w] == 0:
            find_group(w)

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    path = [[] for _ in range(N+1)]
    visited = [0] *(N+1)
    for i in range(M):
        s, e = arr[i*2], arr[i*2 + 1]
        path[s].append(e)
        path[e].append(s)
    cnt = 0
    for i in range(1, 1+N):
        if visited[i] == 0:
            cnt += 1
            find_group(i)
    # 여기까지 해서 지금 각 짝을 지은 애들 끼리 연결을 해준걸 path에 저장을 일단 했어
    print(f"#{tc} {cnt}")

