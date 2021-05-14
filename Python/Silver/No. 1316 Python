# https://www.acmicpc.net/problem/1316
# 그룹 단어 체커 (구현, 문자열) / 실버5

num = int(input())
count = 0

for i in range(num):
    lst = []
    word = input()
    for j in range(len(word)):
        if j > 0:
            if (word[j] in lst) and (word[j] != word[j-1]):
                count -= 1
                break
        lst.append(word[j])
    count += 1
    
print(count)
