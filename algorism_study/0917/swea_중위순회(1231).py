import sys
sys.stdin = open("swea_중위순회(1231).txt")

def inorder(node_list):


T = 10
for tc in range(1, 1+T):
    N = int(input())
    # 0, 1, 2, 3, 4, 5, 6, 7, 8을 저장 할 빈리스트를 만들기 위해서
    node_list = [0]*(N+1)
    #반복해서 값을 가져와서 더해줌 node_list에 정보를 저장함/인덱스 별로
    for i in range(N):
        arr_node = list(map(str, input().split()))
        node_list[i+1] = arr_node[1]
    print(f"{tc} {inorder[node_list]}")

