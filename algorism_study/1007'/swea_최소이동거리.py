import sys
sys.stdin = open("swea_최소이동거리.txt")

import heapq
def dijkstra(v):
    # 시작접 세팅
    pq = []
    D[v] = 0
    heapq.heappush(pq, (D[v], v))
    # 2. pq가 비어있지 않은 동안 계속 돌림(while)
    while pq:
        # 3. 가중치가 최소인 정점
        weight, v = heapq.heappop(pq)
        # 4. 방문체크 와 + 하고 싶은 일 하기(v에 도착함? 이거 확인 하려고 함)
        if visited[v] ==1:
            continue
        if v == V:
            return D[v]
        # 5. 인접정점 가중치 갱신
        for w in range(V+1):
            if nearby_matrix[v][w] and visited[w] == 0:
                if D[w] > D[v] + nearby_matrix[v][w]:
                    D[w] = D[v] + nearby_matrix[v][w]
                    heapq.heappush(pq, (D[w], w))

# 다익스트라 최단 경로로 품
T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    # 인접행렬
    nearby_matrix = [[0] *(V+1) for _ in range(V+1)]
    # 방문체크
    visited = [0] * (V+1)
    # 가중치
    D = [float("inf")] *(V+1)
    for i in range(E):
        s, e, w = map(int, input().split())
        nearby_matrix[s][e] = w
    print(f"#{tc} {dijkstra(0)}")