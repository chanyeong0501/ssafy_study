import sys
sys.stdin = open("swea_최소신장트리(11781).txt")
import heapq

def prim(v):
    # 1. 시작점 세팅(pq만들고 pq에 push 할꺼고 가중치도 0으로 함.)
    pq = []
    D[v] = 0
    total = 0
    heapq.heappush(pq, (D[v], v)) # 가중치 넣고 정점을 넣어야 함
    # 2. pq가 비어있지 않은 동안
    while pq:
        # 3. 가중치 최소값 찾기
        weight, v = heapq.heappop(pq)
        # 4. 방문 처리함. + 가중치 합을 계산도 함
        if visited[v] == 1:
            continue
        else:
            visited[v] = 1
            total += weight
        # 5. 인접한 정점의 가중치를 갱신을 함.
        for w, wt in nearby_list[v]:
            if visited[w] == 0 and wt < D[w]:
                D[w] = wt
                heapq.heappush(pq, (D[w], w))
    return total

INF = float("inf")
T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    # 0 번 부터 사용을 하니깐 인접리스트를 만듦
    nearby_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    D = [INF] * (V+1)
    for i in range(E):
        s, e, w  = map(int, input().split())
        nearby_list[s].append((e, w))
        nearby_list[e].append((s, w))
    ans = prim(0)

    print(f"#{tc} {ans}")