import sys
sys.stdin = open("swea_flatten.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_box = arr[0]
    min_box = arr[0]
    for num in range(834):
        for i in range(100):
            if arr[i] > max_box:
                max_box = arr[i]
            arr[i] = max_box -1
        for j in range(100):
            if arr[j] < min_box:
                min_box = arr[j]
            arr[j] = min_box + 1
        print(arr)
    # final_box_max = arr[0]
    # final_box_min = arr[0]
    # result = 0
    # for num2 in range(100):
    #     if arr[i] > final_box_max:
    #         final_box_max = arr[i]
    #     if arr[i] < final_box_min:
    #         final_box_min = arr[i]
    #
    # result = final_box_max - final_box_min
    # print(f"#{test_case} {result}")
