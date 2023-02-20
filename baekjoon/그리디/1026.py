# 결국 할 수 있는 것은...
# b의 가장큰값과 a의 가장 작은 값을 곱하면 된다.
# n = int(input())

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# a_sorted = sorted(a)
# b_sorted = sorted(b, reverse = True)

# result = 0

# for i in range(n):
#     result += a_sorted[i] * b_sorted[i]

# print(result)


n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0

for i in range(n):
    result += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(result)