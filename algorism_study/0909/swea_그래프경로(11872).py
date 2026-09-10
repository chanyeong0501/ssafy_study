import sys
sys.stdin = open("swea_그래프경로(11872).txt")\

def dfs(v):
    # 시작점을 입력하면 거기서 부터 방문 했다고 체크함
    visited[v] = 1 # 여기서 v는 결국 1번을 의미함.
    #근데 여기서 시작점에서 인접한 노드가, 방문 안한경우에 방문을 함
    for w in adj_list[v]:
        if visited[w] == 0:
            dfs(w)

T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)] # 인접 경로 위치 확인
    visited = [0]*(V+1) # 방문했는지 여부를 확인함 방문하면 1로 바꿀거임
    # 각각의 경로를 인접경로 리스트에 저장함.
    for _ in range(E): # 경로 수만큼 반복해서
        s, e = map(int, input().split()) # 값을 받아와서 저장함
        adj_list[s].append(e)
    fianl_s, final_e = map(int, input().split())
    dfs(fianl_s)
    print(f"#{tc} {visited[final_e]}")
