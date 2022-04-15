# # 7-1

# # 순차 탐색 소스코드 구현
# from unittest import result


# def sequential_search(n, target, array):
#     for i in range(n):
#         if array[i] == target:
#             return i+1
        

# print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
# input_data = input().split()

# n = int(input_data[0])
# target = input_data[1]

# print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기로 한 칸으로 합니다.")
# array = input().split()

# print(sequential_search(n,target,array))

# 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다. 이진탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.

# # 7-2

# # 이진 탐색 소스코드 구현(재귀 함수)
# def binary_search(array, target, start,  end):
#     if start > end:
#         return None

#     mid = (start + end) // 2

#     if array[mid] == target:
#         return mid
    
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid-1)

#     else:
#         return binary_search(array, target, mid+1, end)


# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))
# start = 0
# end = n-1
# result = binary_search(array, target, start, end)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result+1)

# 7-3
# 이진 탐색 소스 코드 구현(반복문)

# def binary_search(array, target, start, end):
#     while start <= end:
#         if start > end:
#             return None

#         mid = (start + end) // 2

#         if array[mid] == target:
#             return mid
        
#         elif array[mid] > target:
#             end = mid - 1

#         else:
#             start = mid + 1

    

# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)

# 7-4 한 줄 입력받아 출력하는 소스코드
import sys

# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip()
print(input_data)
