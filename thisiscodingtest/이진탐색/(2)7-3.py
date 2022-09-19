# 왜 안되는거야 
# 피곤하다 졸리다. 
# 여기서 start, end는 자리수(값이 아니라)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if start > end:
            return None
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        
# 원소의 갯수와 타겟을 입력받기!!!
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:    
    print(result+1)
            


        





