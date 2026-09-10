import sys
sys.stdin = open("swea_pascaltriangle(2005).txt")
def pascal(N):
    arr = [[0] * N for _ in range(N)]
    print(f"#{tc}")
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
            print(arr[i][j], end=" ")
        print()
    return
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    pascal(N)