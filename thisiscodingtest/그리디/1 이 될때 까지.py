    # 3-5
n, k = map(int, input().split())
result = 0

# n 이 k 이상이라면 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는 다면 N에서 1씩 빼기
    while n % k !=0:
        n-=1
        result += 1
    
    # K로 나누기
    n = n / k
    result += 1

# 내가 생각하는 범위 1<n<k
# 나누어 지지 않는 다면 1을 빼기
while n > 1:
    n-=1
    result += 1

print(result)

