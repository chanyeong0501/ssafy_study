import sys
sys.stdin = open("swea_basicpalindrome.txt")


T = int(input())
for tc in range(1, 1+T):
    text = list(input())
    a = len(text)//2
    flag = True
    for text_str in range(a):
        if len(text) % 2 != 0:
            if text[text_str] != text[len(text)-1-text_str]:
                flag = False

        else:
         if text[text_str] != text[len(text)-1-text_str]:
            flag = False
    print(int(flag))
