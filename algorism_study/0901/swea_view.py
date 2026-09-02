import sys

sys.stdin = open("min_max_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # for i in range(N-4):
    #     for j in range(2, N-2):
    #         arr[j]
    result = 0
    for j in range(2, N - 2):
        second_build = 0
        for i in range(j-2, j+3):
            if j == i:
                continue
            if arr[i] > second_build:
                second_build = arr[i]
        if arr[j] > second_build:
            result += arr[j]-second_build

    print(f"#{test_case} {result}")