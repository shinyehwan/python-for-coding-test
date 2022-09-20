# import sys
# input = sys.stdin.readline

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return array[mid]
#         elif array[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return -1


# result = binary_search(array, target, 0, n-1)
# count = 0
# for i in array:
#     if i == result:
#         count += 1
#     else:
#         count = -1

# print(count)


import sys
input = sys.stdin.readline

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

def binary_search_first(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if(mid == 0 or array[mid - 1] != target):
                return mid
            else:
                end = mid - 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def binary_search_end(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            if(mid == end or array[mid + 1] != target):
                return mid
            else:
                start = mid + 1
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if(binary_search_first(array, target, 0, n-1) == -1):
    print(-1)

else:
    print(binary_search_end(array, target, 0, n-1) - binary_search_first(array, target, 0, n-1) + 1)


