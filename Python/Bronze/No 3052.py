# https://www.acmicpc.net/problem/3052
# 나머지 (수학, 사칙연산) / 브론즈2

# 파이썬 리스트 중복 제거 방법

# 방법1. 반복문을 통해 새로운 리스트에 중복 요소만 빼고 새로 저장

lst = []
new_lst = []

for i in range(10):
  lst.append(int(input())%42)

for j in lst:
  if j not in new_lst:
    new_lst.append(j)

print(len(new_lst))


# 방법2. set을 이용하여 리스트 중복 제거 (list -> set -> list)

lst = []
for i in range (10):
    lst.append(int(input())%42)

lst_set = set(lst)
lst = list(lst_set)

print(len(lst))


# 학습 내용: 파이썬 리스트 중복 제거 방법, 리스트 len(list이름)함수 이용
