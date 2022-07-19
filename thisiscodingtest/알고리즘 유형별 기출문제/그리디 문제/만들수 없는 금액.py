# 내일 다시 풀어보자... 힘 좀 빼자
# 핵심 파악이 중요
n = input()
data = list(map(int, input().split()))

data.sort()

target = 1

for i in data:
    if target < i:
        break
    else:
        target += i

print(target)



