import sys
sys.stdin = open("swea_화물도크(11765).txt")

def work_time_table(time_table):
    count = 0
    last_work_time = 0
    for i in range(len(time_table)):
        # 끝나는 시간 보다 시작 시간이 더 크다면 ...
        if last_work_time <= time_table[i][0]:
            # 시간이 안겹쳐서 일할 수 있는 거니깐
            count += 1
            # 끝나는 시간을 갱신 해줌
            last_work_time = time_table[i][-1]
        else:
            continue
    return count

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    time_table = []
    for _ in range(N):
        # 반복하면서 각 차마다 시작 끝 시간을 받아와서 저장함
        s, e = map(int, input().split())
        time_table.append((s, e))
    # 뒤에 끝나는 시간을 기준으로 해서 정렬함
    time_table.sort(key=lambda x: x[1])
    ans = work_time_table(time_table)
    print(f"#{tc} {ans}")
