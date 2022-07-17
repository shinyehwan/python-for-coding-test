# 핵심 : 현재 포함되어 있는 그룹의 모험가의 수가 현재의 공포도 보다 크거나 같으면 그룹 결성
n =  int(input())
data = list(map(int, input().split()))

# 오름차순
data.sort

# 현재 그룹에 결성될 모험가 수
count = 0
# 현재 그룹수
result = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)

