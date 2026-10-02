import sys
sys.stdin = open("swea_전자키트(11763).txt")
# def perm(level):
#     if level == n: # 결국 레벨의 깊이를 구한 거임.
#         print(*path)
#         return
#     for i in range(n): # n=3 이면 n은 23, 32 두가지 구하면 되는 거임.
#         if used[i]:
#             continue
#         path[level] = i
#         used[i] = 1
#         perm(level+1) #
#         path[level] = 0
#         used[i] = 0

def perm(level):
    global min_num
    if level == n-1: # 0, 1, 2 되면 종료함 종료조건을 설정함
        currnum = 0
        for j in range(len(path)-1):
            currnum += arr[path[j]- 1][path[j+1]-1]
        currnum += (arr[0][path[0]- 1] + arr[path[-1]-1][0])
        if min_num > currnum:
            min_num = currnum
        return
    for i in range(2, n+1):
        if used[i]:
            continue
        path.append(i) # 순열저장하는 것
        used[i] = 1 # 이번 레벨에서 내가 숫자 하나 뽑았으니 다음엔 그 숫자 뽑지마 하기 위해서 즉 앞에 if 문에서 컨티뉴 되
        # 기 위해서 만들어 둠
        perm(level+1) # -> 일단 하나 뽑았으니 다음으로 넘어가서 다음 꺼 뽑아
        path.pop() # 순열 끝가지 가서 저장 했으니 다음 거 오기 위해서 값을 제거 해줌.
        used[i] = 0 # 이것도 저장한거 하나 뽑았으니 그 사용함 표시 지워 임
T = int(input())
for tc in range(1, 1+ T):
     n = int(input())
     path = []
     # 경로별 전기 소모량 적힌 표 받아옴.
     arr = [list(map(int, input().split())) for _ in range(n)]
     used = [0] * 1000
     min_num = float('inf')
     # 순열
     perm(0)
     print(f"#{tc} {min_num}")