# https://www.acmicpc.net/problem/2163
# 초콜릿 자르기 (수학, 사칙연산) / 브론즈3

def solve(n, m) :
    return m*n -1

n, m = map(int, input().split())

print(solve(n, m))
