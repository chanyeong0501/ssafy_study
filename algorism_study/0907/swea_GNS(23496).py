import sys
sys.stdin  = open("swea_GNS(23496).txt")

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    texts = list(input().split())
    print(f"#{tc}", end=" ")
    base_texts = {'ZRO': 0,
                  'ONE':0,
                  'TWO':0,
                  'THR':0,
                  'FOR':0,
                  'FIV':0,
                  'SIX':0,
                  'SVN':0,
                  'EGT':0,
                  'NIN':0}
    for text in texts:
        if text in base_texts:
            base_texts[text] += 1
    for key in base_texts.keys():
        if base_texts[key] == 0:
            continue
        while base_texts[key] != 0:
                print(key, end=" ")
                base_texts[key] -= 1
    print()