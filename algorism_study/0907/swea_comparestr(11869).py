import sys
sys.stdin = open("swea_comparestr(11869).txt")

T = int(input())
for tc in range(1, 1+T):
    str1 = input()
    str2 = input()
    count = 0
    # for i in range(len(str2)-(len(str1)-1)):
    #     if str1 == str2[i:i+len(str1)]:
    #         count += 1
    # print(f"#{tc} {count}")