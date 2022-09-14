import sys
input = sys.stdin.readline

n = int(input())
arrays = list(map(int, input().split()))
m = int(input())

def sum(upper_bound):
    result = 0
    for array in arrays:
        if upper_bound <= array:
            result += upper_bound
        else:
            result += array
    return result

start = 0
end = max(arrays)
target = -1

while start <= end:
    mid = (start + end) // 2
    if sum(mid) <= m:
        target = mid
        start = mid + 1
    else:
        end = mid - 1
print(end)


# answer = -1
# for array in arrays:
#     given = min(array, target)
#     answer = max(answer, given)
# print(answer)

# import sys
# input = sys.stdin.readline

# n = int(input())
# arrays = list(map(int, input().split()))
# m = int(input())

# start = 0
# end = max(arrays)
# while start <= end:
#     mid = (start + end) // 2
#     result = 0

#     for i in arrays:
#         if i <= mid:
#             result += i
#         else:
#             result += mid

#     if result <= m:
#         start = mid + 1
#     else:
#         end = mid - 1

# print(end)




