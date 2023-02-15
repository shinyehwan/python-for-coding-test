n = int(input())

# 3, 5
# 최소 봉지의 갯수
result = 0

while n >= 3:
    if n % 5 == 0:
        result += n // 5
        break

    if n % 5 != 0:
        n -= 3
        result += 1

    if n == 1:
        result = -1
        break

print(result)