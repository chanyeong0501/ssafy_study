import sys
sys.stdin = open("swea_tree(11926).txt")
 # 예시가 시작하는 노드의 값이 들어오면 예를 들어 1이라면
 # 카운트 하나 올리고 LEFT[1] RIGHT[1]에 값이 있는지 확인
 # 그게다시 함수에 N으로 들어가면서 0이면 그냥 0으로 값이 있으면 그 값으로
 #계속 계산함.
def count_node(N):
    if N == 0:
        return 0
    return 1 + count_node(left[N]) + count_node(right[N])

T = int(input())
for tc in range(1, 1+T):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    # 노드 반복을 하면서 그 개수 만큼 2개씩 받아옴
    for i in range(E):
        p, c = temp[i*2], temp[i*2+1]
        # 만약 이진트리이기 때문에 자식을 저장하는 left에 부모(인덱스)에 자식의 값이 없으면
        if left[p] == 0:
            left[p] = c
        # 값이 left에 있으면 right에 넣음
        else:
            right[p] = c
    print(f"#{tc} {count_node(N)}")
