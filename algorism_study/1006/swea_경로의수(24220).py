import sys
sys.stdin = open("swea_경로의수(24220).txt")

def find_route(S):
    global count
    visited[S] = 1
    # 간선 수 만큼 확인함
    # 저장한 경로에서 시작위치에 있는 것들을 가져옴
    if S == G:
        count += 1
    for i in path[S]:
        # 방문 안햇으면
        if visited[i] == 0:
            find_route(i)
        # 이후 그거 초기화 해줌
        visited[i] = 0




T = int(input())
for tc in range(1, 1+T):
    # 간선과 노드의 개수를 받아옴
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    path = [[] for _ in range(N+1)]
    # 방문체크 리스트 만듦
    visited = [0] * (N+1)
    # 각각 졍로를 튜플로 저장함
    for i in range(E):
        k, j = arr[i*2], arr[i*2+1]
        # 경로 정보 저장
        path[k].append(j)
        # print(f"#{tc} {k} {j}")
    # 출발 S와 도착 G를 받아옴
    S, G = map(int, input().split())
    count = 0
    find_route(S)
    print(f"#{tc} {count}")