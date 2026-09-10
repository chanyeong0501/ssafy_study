import sys
sys.stdin = open("swea_종이붙이기(11874).txt")

def f(N):
    if N <= 1:
        return 1 # 0이나 1이나 경우는 1개라서 만들어둠
    else:
        return f(N-1) + 2*f(N-2) # 문제에서 주어진 규칙을 찾음

T = int(input())
for tc in range(1, 1+ T):
     N = int(input())
     print(f"#{tc} {f(N//10)}")