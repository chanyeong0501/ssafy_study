import sys
sys.stdin = open("swea_전기버스2.txt")

def cnt_station(i, cnt):
    global min_cnt
    if cnt > min_cnt:
        return

    if i >= len(battery) -1:
        min_cnt = min(cnt, min_cnt)
        return

    for j in range(i+1, i+battery[i] + 1):
        cnt_station(j, cnt + 1)
    # global cnt
    # for j in range(i+1, arr[i]+1):
    #     if arr[j] == 0:
    #         return cnt
    #     if arr[i] <= arr[j]:
    #         i = j
    #         cnt += 1
    #         cnt_station(i)
    #     else:
    #         cnt_station(j)

T = int(input())
for tc in range(1, 1+T):
    # arr[0]은 정류장 수(출발지 정류장 포함), 나머진 베터리 용량 수(마지막도착엔 베터리 없음)
    arr = list(map(int, input().split()))
    # 정류장 길이
    N = arr[0]
    # 정류장 별 베터리 용량
    battery = arr[1:] + [0]
    i = 0
    cnt = 0
    min_cnt = float("inf")
    cnt_station(i, -1)
    print(f"#{tc} {min_cnt}")
