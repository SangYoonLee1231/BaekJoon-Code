# https://www.acmicpc.net/problem/2839
# 설탕 배달 (수학, 다이나믹 프로그래밍, 그리디 알고리즘) / 브론즈1


# 첫 번째 풀이

n = int(input())

max_5 = n // 5
max_3 = n // 3
min_num = -1
count = 0

for i in range (max_5+1):
  for j in range (max_3+1):
    if n == (i*5 + j*3):
      if count > 0:
        if min_num < (i+j): continue
      min_num = i+j
      count = 1

print(min_num)



# 두 번째 풀이
# (다음의 논리 반영 -> 봉지 개수를 최소화 하려면 5kg봉지를 최대한으로 싸야한다.
# 즉, 5kg볼지를 가장 많이 쓰는 방법부터 5kg볼지를 줄이고 3kg봉지 개수를 늘려가는 순서대로 찾으면
# 가장 먼저 나오는 경우가 최소로 봉지를 쓰는 경우일 것이다.)

def bag_count(n):
  bag = 0
  while not n % 5 == 0:
    n = n-3
    bag = bag + 1
    if n < 0 : return -1
  return bag + n//5

n = int(input())
print(bag_count(n))
