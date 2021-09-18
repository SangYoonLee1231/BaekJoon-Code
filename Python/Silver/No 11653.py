# https://www.acmicpc.net/problem/11653
# 소인수분해 (수학, 정수론, 소수 판정) / 실버4

n = int(input())

i = 2
while n != 1:
	if n % i == 0:
		print(i)
		n = n / i
	else:
		i += 1
