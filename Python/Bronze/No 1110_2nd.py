# https://www.acmicpc.net/problem/1110
# 더하기 사이클 (수학, 구현, 문자열) / 브론즈1
# 풀이2: 정수 자료형으로만 풀이

def cycle(n):
  first_num = n
  count = 0
  new_num = -1

  while not first_num == new_num:
    count += 1
    if count > 1: n = new_num
    new_num = ((n%10)*10) + (n//10 + n%10)%10

  return count

n = int(input())
print(cycle(n))
