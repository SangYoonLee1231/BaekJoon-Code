# https://www.acmicpc.net/problem/1978
# 소수 찾기 (수학, 정수론, 소수 판정, 에라토스테네스의 체) / 실버4
# 에라토스테네스의 체는 이용X

def isPrime(n):
  if n == 1: return 0
  if n == 2: return 1
  i = 2
  while i*i <= n:
    if n % i == 0: return 0
    i += 1
  return 1

n = int(input()) # 사실상 의미 없는 코드
lst = list(map(int, input().split()))

count = 0
for i in lst:
  count += isPrime(i)

print(count)
