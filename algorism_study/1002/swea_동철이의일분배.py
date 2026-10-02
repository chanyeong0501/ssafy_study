import sys
sys.stdin = open("swea_동철이의일분배.txt")

def calculate_price(level, cur_price):
    global max_price
    if cur_price <= max_price:
        return
    if level == N:
        max_price = max(max_price, cur_price)
        return
    for i in range(N):
        if check_table[i] != 1:
            price_check[level] = arr[i]
            check_table[i] = 1
            calculate_price(level+1, cur_price * arr[level][i])
            check_table[i] = 0


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    #2차원 배열 받아옴
    # arr = [[float(x) * 0.01 for x in input().split()] for _ in range(N)]
    arr = [list(map(float, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] * (0.01)
    price_check = [0] * N
    check_table = [0] * N
    max_price = float("-inf")
    calculate_price(0, 1) # 여기서 주의 확률을 구한거라서 1이 최대 이고 각 확률을 곱할 때 마다 작아진다.
    print(f"#{tc} {max_price*100:6f}")