import sys
sys.stdin = open("swea_퀵정렬(11770).txt")

def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    a = start + 1
    b = end
    # 스타트 위치
    while 1:
        # 일단 우리가 a를 이동시켜서 값을 비교하려는데 전체 범위를 벗어나면 안되니깐
        # 그리고 a보다 큰 값을 찾으려고 하니. 그리고 피봇이랑 같은 값이면 그 값을 왼쪽으로 보내버림
        while a <= end and arr[a] <= arr[pivot]:
            a += 1
        # 위와 마찬가지인 조건과 b위치의 값이 피봇 보다 작은 값일때를 찾고 싶다
        # b의 값의 범위가 만약 피봇이 최소 수라면, 그다음 넘겨주는게 0, -1 일 수도 있어서 이거때문에 주의 해야함
        while b > start and arr[b] > arr[pivot]:
            b -= 1
        # 그리고 여기서 이동하다가 a랑 b랑 서로 엇갈려 지나가면 반복 중단하고 피봇의 위치와 b의 위치를 바꾸어서
        # 피봇의 위치를 고정 시킴
        if a>b:
            break
        # 아니면 계속 a, b위치를 바꾸어서 결국 피봇의 위치를 찾음.
        arr[a], arr[b] = arr[b], arr[a]
    # 다 끝나고 나선 피봇의 위치와 b의 위치를 바꿔서 피봇의 위치를 고정 시킴
    arr[pivot], arr[b] = arr[b], arr[pivot]
    quick_sort(start, b-1)
    quick_sort(b+1, end)

T = int(input())
for tc in range(1, 1+T):
    N =  int(input())
    arr = list(map(int, input().split()))
    start = 0
    end = N-1
    quick_sort(start, end)
    print(f"#{tc} {arr[N//2]}")
    # 계속 실행되다가 내부의 끝내는 조건에서 끝남.

