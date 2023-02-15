# n = int(input())
# m = list(map(int, input().split()))

# result = 0
# # 일단 분류를 한다.
# # [1,2,3,3,4]
# m.sort()

# for i in range(n):
#     result += sum(m[:i+1])

# print(result)

n = int(input())
times = list(map(int, input().split()))
times.sort()

sum = 0
prev = 0

# [1,2,3,3,4]
for time in times:
    sum += prev + time
    prev += time

print(sum)

