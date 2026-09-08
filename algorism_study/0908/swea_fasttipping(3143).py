import sys
sys.stdin = open("swea_fasttipping(3143).txt")

T = int(input())
for tc in range(1, 1+T):
    text, base_text = input().split()
    print(text, base_text)
    N = len(text)
    M = len(base_text)
    count = 0
    i = 0
    while i < (len(text)-len(base_text)+1):
        flag = True
        for j in range(len(base_text)): # 패턴과 다르면 입력1증가
            if text[i+j] != base_text[j]:
                flag = False
                break
        if flag: # 패턴과 같으면 확인 후 1 증가
            count += 1
            i = i + M -1
        i += 1

    print(f"{tc} {N-(M*count)+count}")



 # def my_find(p, t):
 #     N = len(t)
 #     M = len(p)
 #     #텍스트 순회함
 #     for i in range(N-M+1):
 #         #패턴 순회함
 #        for j in ragne(M):
 #    for i in range(len(text)-len(base_text)+1):
 #        flag = True
 #        for j in range(len(base_text)): # 패턴과 다르면 입력1증가
 #            if text[i+j] != base_text[j]:
 #                flag = False
 #                count += 1
 #                break
 #        if flag: # 패턴과 같으면 확인 후 1 증가
 #            count += 1
