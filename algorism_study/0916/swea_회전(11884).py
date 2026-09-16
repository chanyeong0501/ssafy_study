import sys
sys.stdin = open("swea_회전(11884).txt")

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split()) # 숫자 개수랑 반복 횟수
    arr = list(map(int, input().split()))

    queue = [0] * (N+1) #한칸 더 많은 빈 배열을 만듦
    front = -1
    rear = -1

    for i in range(N):
        if front == -1:
            front = 0 # 0번 인덱스로 손가락 위치 옮김
        rear += 1
        queue[i] = arr[i]
    # print(queue) queue에 순서대로 들어갔는지 확인
    for _ in range(M): # 반복횟수만큼 반복홤
        pop_item = queue[front]
        front = (front+1) % (N+1)
        rear = (rear+1) % (N+1)
        queue[rear] = pop_item
    print(f"#{tc} {queue[front]}")
