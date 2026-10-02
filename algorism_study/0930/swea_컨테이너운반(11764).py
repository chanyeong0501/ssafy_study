import sys
sys.stdin = open("swea_컨테이너운반(11764).txt")

def move_weight(r, c):
    if r>=N and c>=M:
        return
    # 옮길 수 있는 화물의 무게의 합
    global total_weight
    # 화물과 트럭 수보다 포인터 즉 인덱스가 커짐 안됨.
    if r < N and c < M:
        # 트럭용량보다 화물의 용량이 작거나 같으면
        if W[r] <= T[c]:
            total_weight += W[r]
            # 각각 좌표를 옮겨줌
            move_weight(r+1, c+1)
        elif W[r] > T[c]:
            move_weight(r+1, c)
        else:
            return


T = int(input())
for tc in range(1, 1+T):
    N, M= map(int, input().split()) # 화물과 컨테이너 수
    # 화물의 무게들
    W = list(map(int, input().split()))
    W.sort(reverse=True)
    # 트럭의 적재 용량
    T = list(map(int, input().split()))
    T.sort(reverse=True)
    total_weight = 0
    move_weight(0, 0)
    print(f"#{tc} {total_weight} ")