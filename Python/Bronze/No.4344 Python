# https://www.acmicpc.net/problem/4344
# 평균은 넘겠지 (수학, 사칙연산) / 브론즈1

import sys

n = int(sys.stdin.readline())
for i in range(n):
  lst = list(map(int, sys.stdin.readline().split()))

  avg = 0.0; over_avg_people = 0
  
  avg = sum(lst[1:]) / lst[0]

  for k in lst[1:]:
    if avg < k:
      over_avg_people = over_avg_people + 1

  print(format(over_avg_people / lst[0] * 100, ".3f") + "%")

  # list 요소 합은 sum()함수를 통해 반복문 없이 구할 수 있다.
