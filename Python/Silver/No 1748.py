# https://www.acmicpc.net/problem/1748
# 수 이어 쓰기1 (수학, 구현) / 실버3

def solution(n):
    ret, k = 0, len(str(n))
    for i in range (1, k): ret += i * (10**i - 10**(i-1))
    ret += (n - 10**(k-1) + 1) * k
    return ret

num = int(input())
print(solution(num))
