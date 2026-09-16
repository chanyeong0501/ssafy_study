import sys
sys.stdin = open("swea_회전(11884).txt")

def  find_maze(maze, N):
    for i in range(N):
        for j in range(N)



T = int(input())
for tc in range(1, 1+T):
    N = int(input())

    start_i, start_j = find_start(maze, N)