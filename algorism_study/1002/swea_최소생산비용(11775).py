import sys
sys.stdin = open("swea_최소생산비용(11775).txt")

def calculate_price(level, cur_price):
    global min_price
    if cur_price >= min_price:
        return
    if level == N:
        min_price = min(min_price, cur_price)
        return
    for i in range(N):
        if check_table[i] != 1:
            price_check[level] = arr[i]
            check_table[i] = 1
            calculate_price(level+1, cur_price + arr[level][i])
            check_table[i] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    #2차원 배열 받아옴
    arr = [list(map(int, input().split())) for _ in range(N)]
    price_check = [0] * N
    check_table = [0] * N
    min_price = float("inf")
    calculate_price(0, 0)
    print(f"#{tc} {min_price}")