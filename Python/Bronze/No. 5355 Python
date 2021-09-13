# https://www.acmicpc.net/problem/5355
# 화성 수학 (수학, 구현, 문자열, 사칙연산) / 브론즈2

'''
n = int(input())

for _ in range (0, n):

    A = list(map(str ,input().split()))
    result = float(A[0])

    for i in range (1, len(A)):
        if A[i] == '@': result *= 3
        elif A[i] == '%': result += 5
        elif A[i] == '#': result -= 7
    print("{:.2f}".format(result))
    #print("%0.2f" % result)

    # 소수점 이하 자릿수 표현 : https://ming-jee.tistory.com/124
'''

def calc(num, item):
    if item == '@' : return num * 3
    elif item == '%' : return num + 5
    elif item == '#' : return num - 7

n = int(input())

for _ in range(0, n):
    A = list(input().split(" "))
    num = float(A.pop(0))

    for i in A:
        num = calc(num, i)
    print("%.2f" % num)
