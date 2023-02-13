# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()

# first = data[n-1]
# second = data[n-2]

# result = 0
# # k만큼 반복

# while True:
#     if m == 0:
#         break
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     result += second
#     m -= 1

# print(result)


n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

# 세트의 갯수
count = ( m // (k+1) )
# 혹시 나머지가 있으면 나머지의 갯수
remain = ( m % (k+1) )

result = count * (first * k + second) + remain * first

print(result) 


