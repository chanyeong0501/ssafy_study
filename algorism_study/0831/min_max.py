import sys

sys.stdin = open("min_max_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # for i in range(N-4):
    #     for j in range(2, N-2):
    #         arr[j]
    for j in range(2, N - 2):
        for i in range(j-2, j+3):
            if
    print(f"#{test_case} {result}")