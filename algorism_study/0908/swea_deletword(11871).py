import sys
sys.stdin = open("swea_deletword(11871).txt")
T = int(input())

for tc in range(1, 1+T):
    text = list(input())
    s = []
    for i in text:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
    print(f"#{tc} {len(s)}")