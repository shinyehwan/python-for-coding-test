# 7-5
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None #  return 의 위치 중요하네 값이 다르게 나오잖아...


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:

    result = binary_search(array, i, 0, n-1)

    if result != None:
        print('yes', end=' ')

    else:
        print('no', end=' ') 
    
