#강사님 풀이
import sys
sys.stdin  = open("swea_노드의거리.txt")

from collections import deque

T =int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
