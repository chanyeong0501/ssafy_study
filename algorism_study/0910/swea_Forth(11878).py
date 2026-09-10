import sys
sys.stdin = open("swea_Forth(11878).txt")

T = int(input())
for tc in range(1, 1+T):
    arr = list(map(str, input().split()))
    sum_list = []
    is_error = False
    for x in arr:
        if x == '.':
            break
        elif x not in "(/*+-":
            sum_list.append(int(x))
        else:
            if len(sum_list)<2:
                is_error = True
                break
            num2 = sum_list.pop()
            num1 = sum_list.pop()
            if x == '+':
                num3 = num1 + num2
                sum_list.append(num3)
            elif x == '-':
                num4 = num1 - num2
                sum_list.append(num4)
            elif x =='*':
                num5 = num1 * num2
                sum_list.append(num5)
            elif x == '/':
                num6 = num1 / num2
                sum_list.append(num6)
    if is_error:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {sum_list[0]}')

        #문제 확인 필요함