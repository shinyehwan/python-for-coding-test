# 핵심 : 무게마다 볼링공이 몇개 있는지 확인
# 배열에 넣는다, 이미 계산했던 경우는 제외

# 볼링공 갯수, 최대 무게
n,m = map(int, input().split())
# 각 볼링공의 무게
k = list(map(int, input().split()))


array = [0] * 11

# 공의 무개별 갯수 확인
for i in k:
    array[i]+=1

result = 0

for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)
    


