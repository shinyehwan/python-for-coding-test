n, k = map(int, input().split())
result = 0

# n 이 k 이상이라면 계속 나누기
while n >= k:
    while n % k !=0:
        n-=1
    n = n / k
    result += 1

# 나누어 지지 않는 다면 1을 빼기
while n > 1:
    n-=1
    result += 1

print(result)

