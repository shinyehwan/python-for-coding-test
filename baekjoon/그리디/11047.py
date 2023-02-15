# 배운점
# 첫번째로 reversed를 쓸라면 배열 리스트가 있어야 한다.
n, k = map(int, input().split())

coin = list()
for i in range(n):
    coin.append(int(input()))


result = 0

# 나눌 수 있는 제일 큰 수를 찾는다.
# 리스트 자체의 값을 반복하는 수로 갖는다!
# 아니면 그냥 갯수를 반복해서 배열 값에 넣어주던가 해야지!
for i in reversed(coin):
    result += k // i
    k %= i

print(result)