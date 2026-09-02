import sys
sys.stdin = open("swea_numcard.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    max_v = 0
    max_k = 0
    count_dict = {}
    for i in arr:
        if str(i) not in count_dict:
            count_dict[str(i)] = 1
        else:
            count_dict[str(i)] += 1
    print(count_dict)
    for k, v in count_dict.items():
        if v >= max_v:
            max_v = v
            if int(k) > max_k:
                max_k = int(k)

    print(f"#{test_case} {max_k} {max_v}")



