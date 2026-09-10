# import sys
# sys.stdin = open("swea_계산기.txt")

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    stack = [0] * N *N
    top = -1

    icp = {'(':3, '*':2, '/':2, '+':1, '-':1}   # 밖에 있을때의 우선 순위 (클수록 높음)
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1}   # 스택안에서의 우선 순위 ( " )

    infix = input() # 수식들어옴
    postfix = '' # 피연산자 저장

    for token in infix:
        if token == ' ': # 공백 무시하기 위해서 씀
            continue
        if token not in '(+-*/)':   # 피연산자면 후위식에 추가
            postfix += token
        elif token == ')':          # 여는 괄호를 만날 때까지 pop
            while top>-1 and stack[top] != '(':
                top -= 1
                postfix += stack[top+1]
            if top != -1:   # 전체 수식이 괄호로 둘러 쌓이지 않은경우 대비
                top -= 1    # '(' 버림...
        else:                      # 연산자인 경우
            if top == -1 or isp[stack[top]] < icp[token]:  # 토큰의 우선순위가 더 높으면
                top += 1  # push
                stack[top] = token
            elif isp[stack[top]] >= icp[token]: # 토큰과 같거나 더 높으면
                while top > -1 and isp[stack[top]] >= icp[token]:
                    postfix += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = token  # 처리 단계별로 상태 출력
    while top > -1:                 # 바깥 괄호가 없는 경우 '6+5*(2-8)/2'
        top -= 1                    # 스택의 모든 연산자 pop
        postfix += stack[top + 1]
    for sm in postfix:
        if sm not in '(*/-+': # 연산자 아닌 숫자들만 스텍에 저장계속함
            top += 1
            stack[top] = sm
        else: # 근데 저장하다가 연산자가 들어오면
            top -= 1 # 위치하나 빼주고
            num1 = int(stack[top +1]) # 뺴준 값에서 하나 더해서 원래 값을 가저옴
            top -= 1
            num2 = int(stack[top +1]) # 값을 두개 가지고 옴.
            if sm == '+': # 두 값을 더해줌
                top += 1  # 그리고 그 값을 스택의 최 상단에 저장함
                stack[top] = num2 + num1
            elif sm == '-':
                top += 1
                stack[top] = num2 - num1
            elif sm == '/':
                top += 1
                stack[top] = num2 / num1
            elif sm == '*':
                top += 1
                stack[top] = num2 * num1
    print(f"#{tc} {stack[0]}")


