# https://www.acmicpc.net/problem/2562
# 최댓값 (구현) / 브론즈2

# 풀이1 : 내장 함수 이용하지 않고 최댓값 찾는 로직 직접 구현
lst = []; max_num = 0; max_i = -1
for i in range(9):
  num = int(input())
  lst.append(num)
  if i == 0:
    max_num = num
    max_i = i

for i in range(1, 9):
  if lst[i] > max_num:
    max_num = lst[i]
    max_i = i

print(max_num)
print(max_i+1)


# 풀이2 : 내장 함수 이용
lst = []
for i in range(9):
  lst.append(int(input()))

print(max(lst))
print(lst.index(max(lst))+1)


# 파이썬의 리스트에는 최댓값을 출력해주는 내장함수 max(list이름)가 있다.
