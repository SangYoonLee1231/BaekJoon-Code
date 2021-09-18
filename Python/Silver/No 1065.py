# https://www.acmicpc.net/problem/1065
# 한수 (브루트포스 알고리즘) / 실버4

# 방법 1:
def isSequence(num):    # num은 문자열
    if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
        return 1
    return 0

n = int(input())

count = 99

if n <= 99: print(n)
elif n <= 110: print("99")
elif n <= 999:
    for i in range(111, n+1):
        count += isSequence(str(i))
    print(count)
else: print("144")


# 방법 2: (map 이용, 모듈화)
def HanSu(n):
    cnt = 99
    if n <= 99: return n
    else:
        for i in range(100, n+1):
            num_lst = list(map(int, str(i)))
            if num_lst[0] - num_lst[1] == num_lst[1] - num_lst[2]:
                cnt += 1
        return cnt

n = int(input())
print(HanSu(n))
