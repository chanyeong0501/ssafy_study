import sys
sys.stdin = open("swea_괄호문제(11870).txt")

T = int(input())

# for tc in range(1, 1+T):
#     text = list(input())
#     s = []
#     flag = True
    # for char in text:
    #     if char == '(' or char == '{':
    #         s.append(char)
    #     elif s and char == ')':
    #         if s[-1] == '(':
    #             s.pop()
    #         else:
    #             flag = False
    #             break
    #     elif s and char == '}':
    #         if s[-1] == '{':
    #             s.pop()
    #         else:
    #             flag = False
    #             break
    #     elif not s and (char == '}'or char == ')'):
    #         flag = False
    # print(f"#{tc}", end=" ")
    # if flag and not s:
    #     print(1)
    # else:
    #     print(0)

    # 딕서너리 풀이
for tc in range(1, 1+T):
    text = list(input())
    s = [0] *100
    base_dict = {')': '(','}': '{'}
    top = -1
    ans = 1
    for char_spec in text:
        if char_spec in '({':
            top += 1
            s[top] = char_spec
        elif char_spec in ')}':
            if top == -1: # 아에 괄호가 들어가지 않은 경우
                ans = 0
                break
            else: # 괄호를 확인 하는 경우
                top -= 1
                old = s[top+1]
                if old != base_dict[char_spec]:
                    ans = 0
                    break
    if top != -1:
        ans = 0
    print(f"{tc} {ans}")
