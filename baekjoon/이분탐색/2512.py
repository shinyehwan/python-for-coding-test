import sys
input = sys.stdin.readline

n = int(input())
arrays = list(map(int, input().split()))
m = int(input())

def sum(upper_bound : int):
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
    mid = start + end // 2
    if sum(mid) <= m:
        target = mid
        start = mid + 1
    else:
        end = mid - 1

answer = -1
for array in arrays:
    given = min(array, target)
    answer = max(answer, given)

print(answer)






