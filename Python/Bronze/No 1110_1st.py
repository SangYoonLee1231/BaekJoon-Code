# https://www.acmicpc.net/problem/1110
# 더하기 사이클 (수학, 구현, 문자열) / 브론즈1
# 풀이1: 문자열로 변환하여 풀이

def cycle(n):
  count = 0

  if len(n) == 1:
    n = '0' + n

  first_num = n
  new_num = ""

  while not first_num == new_num:
    count += 1
    if count > 1:
      n = new_num
    sum_num = str(int(n[0]) + int(n[1]))
    new_num = n[-1] + sum_num[-1]
  return count

n = input()
print(cycle(n))
