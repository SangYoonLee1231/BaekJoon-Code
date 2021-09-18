# https://www.acmicpc.net/problem/2530
# 인공지능 시계 (수학, 사칙연산) / 브론즈4

hr, min = map(int, input().split())
time = int(input())

hr, min, sec = map(int, input().split())
time = int(input())

hr += time // 3600
min += (time // 60) % 60
sec += time % 60

if sec >= 60:
    min += sec // 60
    sec = sec % 60

if min >= 60:
    hr += min // 60
    min = min % 60

if hr >= 24:
    hr = hr % 24

print(hr, min, sec)


# 다른 방법 (아직 이해 못한 코드)

h,m,s = map(int,input().split(" "))
sec = int(input())

# h:시각, m:분, s:초, sec:추가된 초
#고려요소 1번째
s1 = (s+sec)%60  #최종 초
m1 = (s+sec)//60
#고려요소 2번째
m2 = (m+m1)%60 # 최종 분
h1 = (m+m1)//60
#고려요소 3번째
h2 = (h+h1)%24 # 최종 시각

print(h2,m2,s1)  #출력
