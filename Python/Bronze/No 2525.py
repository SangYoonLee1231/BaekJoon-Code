# https://www.acmicpc.net/problem/2525
# 오븐 시계 (수학, 사칙연산) / 브론즈4

hr, min = map(int, input().split())
time = int(input())

hr += time // 60
min += time % 60

if min >= 60:
    hr += min // 60
    min = min % 60

if hr >= 24:
    hr = hr % 24

print(hr, min)
