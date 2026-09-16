import sys
sys.stdin = open("swea_피자굽기(11885).txt")

T = int(input())
for tc in range(1, 1+T):
    # 화덕 크기랑 주어진 피자개수 , 문제를 보면 피자의 치즈가 1보다 작게 되면 그때 다 녹은 거임.
    N, M = map(int, input().split())
    # 피자들의 치즈양
    cheese = list(map(int, input().split()))
    # 원형 큐를 사용해보자
    queue = [None] * (N + 1)
    front = -1
    rear = -1
    # 여기서는 화덕 queue에 피자를 하나씩 넣고 인덱스를 추가함(rear)
    for i in range(N):
        if front == -1:
            front = 0
        rear += 1
        queue[rear] = cheese[i]


