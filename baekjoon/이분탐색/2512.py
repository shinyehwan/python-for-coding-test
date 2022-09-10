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
    mid = start + end // 2
    if sum(mid) <= m:
        target = mid
        start = mid + 1
    else:
        end = mid - 1
print(end)






