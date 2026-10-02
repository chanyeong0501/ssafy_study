import sys
sys.stdin = open("swea_병합정렬(11768).txt")

def merge(left, right):
    pass
    new_sort_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            new_sort_list.append(left[i])
            i+=1
        else:
            new_sort_list.append(right[j])
            j+=1
    if left:
        new_sort_list.extend(left[i:])
    if right:
        new_sort_list.extend(right[j:])
    return new_sort_list



def divide_arr(arr):
    global count
    if len(arr) == 1:
        # print(f"{tc}{arr}")
        return arr
    # 길이 만큼 반 잘라서 잘개 쪼갬
    mid = len(arr)//2
    left = divide_arr(arr[:mid])
    right = divide_arr(arr[mid:])

    if left[-1] > right[-1]:
        count += 1
    return merge(left, right)

T = int(input())
for tc in range(1, 1+T):
    # 배열의 크기 받아옴
    N = int(input())
    # 배열 받아옴
    arr = list(map(int, input().split()))
    count = 0
    sorted_arr = divide_arr(arr)

    print(f"#{tc} {sorted_arr[len(sorted_arr)//2]} {count}")
