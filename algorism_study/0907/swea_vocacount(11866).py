import sys
sys.stdin = open("swea_vocacount(11866).txt")
T = int(input())
for tc in range(1, 1+T):
    str1 = list(input())
    str2 = list(input())
    count_dict = {}
    for i in str1:
        count = 0
        for j in str2:
            if i == j:
                count += 1
        if i not in count_dict:
            count_dict[i] = count
    max_value = 0
    for value in count_dict.values():
        if value > max_value:
            max_value = value
    print(f"#{tc} {max_value}")