import sys
sys.stdin = open("swea_연산(11779).txt")

def add_one(x): return x + 1
def sub_one(x): return x - 1
def mul_two(x): return x * 2
def sub_ten(x): return x - 10

def calculator(N):
    math_tools = [add_one, sub_one, mul_two, sub_ten]
    # M이 N이랑 같을 때 끝냄
    while N != M:


T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    calculator(N)
    math_tools = [1, -1, *2, -10]