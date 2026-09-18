import sys
sys.stdin = open("swea_2진수를10진수로출력하기(20317).txt")
# 파일명 잘못 적음 이거 이진수 1 문제이다!!!
T = int(input())
for tc in range(1, 1+T):
    N, M = input().split()
    hexa_mapping = {
        '0': '0000', '1':'0001', '2':'0010', '3': '0011',
        '4': '0100', '5':'0101', '6': '0110', '7':'0111',
        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'
    }
    print(f'#{tc}', end=" ")
    for i in M:
        print(f"{hexa_mapping[i]}", end='')
    print()
