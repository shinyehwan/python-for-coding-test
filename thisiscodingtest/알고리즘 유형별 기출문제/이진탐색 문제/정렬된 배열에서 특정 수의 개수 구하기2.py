# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 시간 복잡도 : O(logN)

from bisect import bisect_left, bisect_right

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

count = bisect_right(array, target) - bisect_left(array, target)
if count == 0:
    print(-1)
else:
    print(count)
