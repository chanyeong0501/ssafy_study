import sys
sys.stdin = open("")
from collections import deque

def pizza(arr, M):
    q = []
    for i in range(N):
        q.append((i, arr[i]))
    last = N
    while len(q) != 1:
        idx, cheese = q.pop(0)
        



T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = list