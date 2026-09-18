import sys
sys.stdin = open("swea_이진수2(11753).txt")

T = int(input())
for tc in range(1, 1+T):
    N = float(input())
    count = 0
    # 정수가 되기 전까지 반복하세요
    print(f"{tc}", end=' ')
    while N != 0:
        if count <= 12:
            if count >= 13:
                print("overflow")
                break
            N = N*2
            p = int(N)
            N = N-p
            count += 1
            print(f"{p}", end="")
    print()